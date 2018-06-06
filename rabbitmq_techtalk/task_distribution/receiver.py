#!/usr/bin/env python
import pika
import time
import sys

from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

channel.queue_declare(queue='task_queue', durable=True)


consumer_name = sys.argv[1] if sys.argv else "Consumer"
print(
    '[*] {name} Waiting for messages. '
    'To exit press CTRL+C'.format(name=consumer_name))

def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    callback,
    queue='task_queue')

channel.start_consuming()
