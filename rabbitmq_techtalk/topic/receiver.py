#!/usr/bin/env python
import pika
import time
import sys

from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'geographic-info'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='topic')


# Exclusive Queue for consumer
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

consumer_name = sys.argv[1] if sys.argv else "Consumer"

locations = sys.argv[2:]
if not locations:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for location in locations:
    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue=queue_name,
        routing_key=location)

print(
    '[*] {name} Waiting for messages. Bindings={locations} !'
    ' To exit press CTRL+C'.format(
        name=consumer_name,
        locations=",".join(locations)))


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    callback,
    queue=queue_name, no_ack=True)

channel.start_consuming()
