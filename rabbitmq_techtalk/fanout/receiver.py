#!/usr/bin/env python
import pika
import time
import sys

from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'leaderboard'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='fanout')


# Exclusive Queue for consumer
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name)

consumer_name = sys.argv[1] if sys.argv else "Consumer"

print(
    '[*] {name} Waiting for messages! '
    'To exit press CTRL+C'.format(name=consumer_name))


def callback(ch, method, properties, body):
    print("[x] %r" % body)


channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True)

channel.start_consuming()
