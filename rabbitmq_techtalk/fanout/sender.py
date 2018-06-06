#!/usr/bin/env python
import pika
from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'leaderboard'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='fanout')



def publish(message):
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key='',
        body=message,
    )
    print("[x] Sent %r" % message)


if __name__ == "__main__":
    while True:
        message = raw_input("[x] Message to publish Or exit [y]: ")
        if message == "y":
            break
        publish(message)
    connection.close()
