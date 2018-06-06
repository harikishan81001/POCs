#!/usr/bin/env python

from common.connection import RabbitConnect

connection = RabbitConnect()

channel = connection.connect()
channel.queue_declare(queue='basic-poc')

channel.queue_declare(queue='basic-poc')

channel.basic_publish(
    exchange='',
    routing_key='basic-poc',
    body='Hello World!')

print("[x] Sent 'Hello World!'")

connection.close()
