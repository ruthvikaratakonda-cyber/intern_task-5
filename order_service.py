import json
import pika

def create_order(order):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='orders')

    channel.basic_publish(
        exchange='',
        routing_key='orders',
        body=json.dumps(order)
    )

    connection.close()

    return {"message": "Order placed", "order": order}