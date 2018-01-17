from os import getenv
from socket import gethostname
import pika

# TODO: resolve before extracting to package
from proto.events import *

CONTAINER_ID = gethostname()
PB_CONTENT_TYPE = 'application/vnd.google.protobuf'


class PubSub(object):
    @staticmethod
    def _build_ampq_url():
        return 'amqp://{user}:{password}@{host}:5672/%2F?connection_attempts=3&heartbeat_interval=3600'.format(
            user=getenv('RABBITMQ_USER', 'guest'),
            password=getenv('RABBITMQ_PASS', 'guest'),
            host=getenv('RABBITMQ_HOST', 'rabbitmq'))

    def __init__(self, ampq_url=None):
        if not ampq_url:
            ampq_url = self._build_ampq_url()

        parameters = pika.connection.URLParameters(ampq_url)
        self.channel = pika.BlockingConnection(parameters).channel()
        self.channel.confirm_delivery()

        self.process_functions = {}

    def publish(self, event_name, event):
        # from google.protobuf.message import Message
        # assert parent class is Message
        exchange = f'{event_name}.{event.__class__.__name__}'

        channel.exchange_declare(exchange_type='fanout', exchange=event_name)

        properties = pika.BasicProperties(
            app_id=CONTAINER_ID, content_type=PB_CONTENT_TYPE)
        channel.basic_publish(
            exchange=event_name,
            body=event.SerializeToString(),
            properties=properties)

    def on_message_callback(self, channel, method_frame, header_frame, body):
        print("on_message_callback", channel, method_frame, header_frame, body)
        # TODO: if content_type !== PB_CONTENT_TYPE

        # TODO: maybe use google.protobuf.reflection ?
        # https://developers.google.com/protocol-buffers/docs/reference/python/google.protobuf.reflection-module#MakeClass
        event_name, event_cls = channel.split('.')

        # imported by: `from proto.events import *`
        Event = type(event_cls, (), {})
        event = Event()

        event.ParseFromString(body)

        self.process_functions[channel](event)

    def listen(self, channel):
        """A decorator that is used to register events listener function for a
        given channel.
        """

        def decorator(func):
            event_name, _ = channel.split('.')
            queue_name = f"{CONTAINER_ID}.{event_name}"
            self.channel.queue_declare(
                queue=queue_name,
                durable=True,
                exclusive=False,
                auto_delete=False)

            # TODO: except pika.exceptions.ChannelClosed
            # TODO: raise PermamentException - event has not been published (yet?)
            self.channel.queue_bind(queue=queue_name, exchange=event_name)

            self.process_functions[event_name] = func
            self.channel.basic_consume(self.on_message_callback, queue=queue_name)

            return func

        return decorator

    def run(self):
        print('PubSub.run', self)
        self.channel.start_consuming()
