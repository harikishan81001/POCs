#!/usr/bin/env python
import pika
from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

# Durable queues
channel.queue_declare(queue='task_queue', durable=True)


def publish(message):
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode = 2)
    )
    print("[x] Sent '{message}'".format(message=message))


if __name__ == "__main__":
    while True:
        message = raw_input("[x] Message to publish Or exit [y]: ")
        if message == "y":
            break
        publish(message)

    connection.close()
