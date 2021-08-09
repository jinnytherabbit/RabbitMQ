import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('10.54.2.47'))
channel = connection.channel()

# channel.queue_declare(queue='A', durable='true')
for i in range(50000):
    channel.basic_publish(exchange='',
                          routing_key='A',
                          body='Vi prodaete ribov?')
print(" [x] Sent 'Hello !'")

connection.close()