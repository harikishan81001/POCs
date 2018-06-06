#!/usr/bin/env python
import pika
import time
import sys

from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'direct_logs'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='direct')


# Exclusive Queue for consumer
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

consumer_name = sys.argv[1] if sys.argv else "Consumer"

severities = sys.argv[2:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue=queue_name,
        routing_key=severity)

print(
    '[*] {name} Waiting for messages. Bindings={bindings} !'
    ' To exit press CTRL+C'.format(
        name=consumer_name,
        bindings=",".join(severities)))


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    callback,
    queue=queue_name, no_ack=True)

channel.start_consuming()
