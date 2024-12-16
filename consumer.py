import pika

USER_NAME = "u_username"
QUEUE_NAME = "q_queuename"
QUEUE_HOST = "fleetmq-id.cartrack.com"  # Ensure the right host is set based on the country where your Cartrack account is hosted
QUEUE_PASSWORD = "acb1234"

credentials = pika.PlainCredentials(
    f"{USER_NAME}",
    f"{QUEUE_PASSWORD}",
)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=f"{QUEUE_HOST}",
        credentials=credentials,
    )
)
channel = connection.channel()


def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(
    f"{QUEUE_NAME}",
    callback,
    auto_ack=True,
)
channel.start_consuming()
