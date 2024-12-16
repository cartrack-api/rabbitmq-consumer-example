
# RabbitMQ Consumer

This repository provides a simple RabbitMQ consumer example using the `pika` library in Python. The script connects to a RabbitMQ queue, consumes messages, and prints the message content.

You may refer to RabbitMQ's website and their documentation.

RabbitMQ offers support for other languages.

---

## **Prerequisites**

Before running the script, ensure you have the following:

- **RabbitMQ Credentials**:
  - **Username**: Provided by your Cartrack administrator.
  - **Password**: Provided by your Cartrack administrator.
  - **Host**: Ensure you are using the correct host for your region (e.g., `fleetmq-id.cartrack.com`).
  - **Queue Name**: The queue you want to consume messages from.

- **Required Packages**:
  - **Python 3.x** installed on your system.
  - **pika** Python package. Install via pip:

    ```bash
    pip install pika
    ```

---

## **Usage**

1. **Configure Environment Variables**  
   Replace the following variables in `consumer.py` with your RabbitMQ credentials:

   ```python
   USER_NAME = "your_username"
   QUEUE_NAME = "your_queue_name"
   QUEUE_HOST = "your_queue_host"
   QUEUE_PASSWORD = "your_queue_password"
   ```

2. **Run the Consumer**  
   Execute the script to start consuming messages from RabbitMQ:

   ```bash
   python consumer.py
   ```

3. **Message Handling**  
   By default, the script prints the message body to the console. Update the `callback` function in `consumer.py` to customize how you handle incoming messages:

   ```python
   def callback(ch, method, properties, body):
       print(body)
   ```

---

## **Code Breakdown**

- **Connection Setup**  
  The script establishes a connection to RabbitMQ using credentials and the host URL.

  ```python
  connection = pika.BlockingConnection(
      pika.ConnectionParameters(
          host=QUEUE_HOST,
          credentials=credentials,
      )
  )
  ```

- **Queue Subscription**  
  It subscribes to the specified queue and begins listening for messages.

  ```python
  channel.basic_consume(
      queue=QUEUE_NAME,
      on_message_callback=callback,
      auto_ack=True,
  )
  ```

- **Message Processing**  
  Each message is handled by the `callback` function. It processes and prints the message contents.

  ```python
  def callback(ch, method, properties, body):
      print(body)
  ```

---

## **Customization**

- **Message Acknowledgment**  
  To ensure reliable processing, you may want to set `auto_ack=False` and manually acknowledge messages after processing.

- **Custom Message Handling**  
  Update the `callback` function to process messages according to your use case.

---

## **Security Notes**

- **Environment Variables**  
  Avoid hardcoding sensitive credentials in the script. Instead, store them in environment variables or a secure configuration file.

- **Access Control**  
  Limit access to the RabbitMQ queue to avoid exposing sensitive data.

---

## **Run the Script**

To consume messages, run:

```bash
python consumer.py
```

This will connect to RabbitMQ, listen for new messages, and print them to the console.
