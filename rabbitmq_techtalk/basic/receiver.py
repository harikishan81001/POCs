#!/usr/bin/env python

from common.connection import RabbitConnect

connection = RabbitConnect()

channel = connection.connect()
channel.queue_declare(queue='basic-poc')


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)

channel.basic_consume(
    callback,
    queue='basic-poc',
    no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
