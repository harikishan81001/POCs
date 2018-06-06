#!/usr/bin/env python
import pika
from common.connection import RabbitConnect

connection = RabbitConnect()
channel = connection.connect()

EXCHANGE_NAME = 'direct_logs'

# Durable queues
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='direct')



def publish(message, severity):
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=severity,
        body=message,
    )
    print(
        "[x] Sent '{message}' with "
        "routing_key={severity}".format(message=message, severity=severity))


if __name__ == "__main__":
    while True:
        message = raw_input("[x] Severity:Message to publish Or exit [y]: ")
        if message == "y":
            break
        message = message.split(":")
        if len(message) > 1:
            severity = message[0]
            message = message[1]
        else:
            message = message[0]
            severity = "info"

        publish(message, severity)

    connection.close()
