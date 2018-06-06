import pika
import urlparse

import config


class RabbitConnect(object):
    def connect(self):
        url = urlparse.urlparse(config.AMQP_HOST_URL)
        print("[#] Parsed URL Details:{}".format(url))
        params = pika.ConnectionParameters(
            host=url.hostname,
            virtual_host=url.path[1:],
            credentials=pika.PlainCredentials(url.username, url.password)
        )
        params.socket_timeout = config.AMQP_SOCKET_TIMEOUT
        self.connection = pika.BlockingConnection(params)
        channel = self.connection.channel()
        return channel

    def close(self):
        self.connection.close()
