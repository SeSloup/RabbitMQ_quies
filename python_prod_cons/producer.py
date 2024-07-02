#!/usr/bin/env python
# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",
port=5672, 
credentials = pika.credentials.PlainCredentials(
	username='test',
	password='test')))
channel = connection.channel()
channel.queue_declare(queue='hello_netology')
channel.basic_publish(exchange='', routing_key='hello_netology', body='Hello Netology!')
connection.close()
