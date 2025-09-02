import os
import pika
from dotenv import load_dotenv

# Load environment from .env (if present)
load_dotenv()

# Configuration from environment with defaults matching previous values
USER_NAME = os.environ.get("USER_NAME")
QUEUE_NAME = os.environ.get("QUEUE_NAME")
QUEUE_HOST = os.environ.get("QUEUE_HOST")  # Ensure the right host is set based on the country where your Cartrack account is hosted
QUEUE_PASSWORD = os.environ.get("QUEUE_PASSWORD")


def _require_env(var_name: str, var_value: str) -> str:
    """Return var_value or raise a helpful error if missing/empty."""
    if var_value is None or str(var_value).strip() == "":
        raise RuntimeError(
            f"Missing required environment variable '{var_name}'.\n"
            f"Please create a .env file (see .env.example) or export {var_name} in your environment."
        )
    return var_value


# Validate required environment variables are set
USER_NAME = _require_env("USER_NAME", USER_NAME)
QUEUE_NAME = _require_env("QUEUE_NAME", QUEUE_NAME)
QUEUE_HOST = _require_env("QUEUE_HOST", QUEUE_HOST)
QUEUE_PASSWORD = _require_env("QUEUE_PASSWORD", QUEUE_PASSWORD)

credentials = pika.PlainCredentials(USER_NAME, QUEUE_PASSWORD)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=QUEUE_HOST, credentials=credentials)
)
channel = connection.channel()


def callback(ch, method, properties, body):
    print(body)


# Use named arguments for clarity and compatibility with newer pika versions
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)


def _run_consumer():
    try:
        print(f"Starting consumer for queue '{QUEUE_NAME}' on host '{QUEUE_HOST}' (user={USER_NAME})")
        channel.start_consuming()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nShutdown requested (KeyboardInterrupt). Closing connection...")
        try:
            if channel.is_open:
                channel.close()
        except Exception:
            pass
        try:
            if connection.is_open:
                connection.close()
        except Exception:
            pass
        print("Consumer stopped.")


if __name__ == "__main__":
    _run_consumer()
