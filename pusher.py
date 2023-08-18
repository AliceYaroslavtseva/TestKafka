import json
import socket
from confluent_kafka import Producer

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
for index in range(100000):
        data ={'data': index, 'test': index * 10000}
        producer.produce('numbers', key="test_group", value=json.dumps(data))
        producer.flush()