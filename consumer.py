import pika
import json

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"📩 Sending notification for order: {order}")

def start_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue='orders')
    channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)

    print("Waiting for messages...")
    channel.start_consuming()