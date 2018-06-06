#!/usr/bin/env python
import pika
from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'geographic-info'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='topic')



def publish(message, location):
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=location,
        body=message,
    )
    print(
        "[x] Sent '{message}' with "
        "routing_key={location}".format(message=message, location=location))


if __name__ == "__main__":
    while True:
        message = raw_input("[x] Location:Message to publish Or exit [y]: ")
        if message == "y":
            break
        message = message.split(":")
        if len(message) > 1:
            location = message[0]
            message = message[1]
        else:
            message = message[0]
            location = "anonymous"
        publish(message, location)
    connection.close()
