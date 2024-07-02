#!/usr/bin/env python
# coding=utf-8
import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters('ampq://rmuser:rpassword@localhost:5672/'))
params = pika.URLParameters('amqp://test:test@localhost:5672/')

'''
params = pika.ConnectionParameters(host="localhost",
port=5672, 
credentials = pika.credentials.PlainCredentials(
	username='rmuser',
	password='rpassword'))
'''	
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello_netology')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(on_message_callback=callback, queue='hello_netology', auto_ack=True,)
channel.start_consuming()
