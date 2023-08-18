import json
import socket
import sys
from confluent_kafka import Consumer, KafkaError, KafkaException
MIN_COMMIT_COUNT = 1

conf = {'bootstrap.servers': 'be19eb3f48f6:9092',
        'group.id': 'test_group',
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)

running = True

def msg_process(msg):
    print(json.loads(msg.value().decode('utf-8')))
def consume_loop(consumer, topics):
    # try:
    consumer.subscribe(topics)

    msg_count = 0
    while running:
        msg = consumer.poll(timeout=1.0)
        if msg is None: continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            msg_process(msg)
            msg_count += 1
            if msg_count % MIN_COMMIT_COUNT == 0:
                consumer.commit(asynchronous=False)
    # finally:
        # Close down consumer to commit final offsets.
        # consumer.close()

def shutdown():
    running = False

consume_loop(consumer, ['numbers'])