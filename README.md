# rabbitmq-consumer-example

Minimal RabbitMQ consumer for Cartrack that connects to a queue and prints incoming messages.

## Setup

1. Create a virtual environment and install dependencies:

```bash
chmod +x ./setup_venv.sh # You can also run the commands in the script manually
./setup_venv.sh
```

Or manually:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

1. Copy `.env.example` to `.env` and populate it with the credentials Cartrack provides during onboarding:

```bash
cp .env.example .env
# then edit .env with values provided by Cartrack
```

## Environment variables (provided by Cartrack)

- USER_NAME
- QUEUE_NAME
- QUEUE_HOST
- QUEUE_PASSWORD

Keep `.env` private and do not commit real credentials.

## Run

```bash
source .venv/bin/activate
python consumer.py
```

## Notes

- `consumer.py` uses `python-dotenv` to load variables from `.env`.
- Dependencies are listed in `requirements.txt`.

That's all — the consumer will connect to the configured queue and print messages as they arrive.
