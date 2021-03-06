#! conding: utf-8
"""consumer for rabbitmq"""

import pika

credentials = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('192.168.99.100',
                                        credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange='hello-exchange',
                         type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)

channel.queue_declare(queue='hello-queue')
channel.queue_bind(queue='hello-queue',
                   exchange='hello-exchange',
                   routing_key='hola')


def msg_consumer(channel, method, header, body):
    """msg_consumer"""
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == 'quit':
        channel.basic_cancel(consumer_tag='hello-consumer')
        channel.stop_consuming()
    else:
        print body

channel.basic_consume(msg_consumer,
                      queue='hello-queue',
                      consumer_tag='hello-consumer')
channel.start_consuming()
