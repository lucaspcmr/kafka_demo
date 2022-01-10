from kafka import KafkaConsumer
from json import loads

consumer1 = KafkaConsumer('kafka_demo',
                          bootstrap_servers=['localhost:9093'],
                          enable_auto_commit=False,
                          value_deserializer=lambda x: x.decode('utf-8'),
                          group_id='group1',
                          auto_offset_reset='earliest',
                          consumer_timeout_ms=1000,
                          fetch_max_wait_ms=1000)
for message in consumer1:
    print(message.value)


consumer2 = KafkaConsumer('kafka_demo',
                          bootstrap_servers=['localhost:9093'],
                          enable_auto_commit=False,
                          value_deserializer=lambda x: x.decode('utf-8'),
                          group_id='group2',
                          auto_offset_reset='earliest',
                          consumer_timeout_ms=1000,
                          fetch_max_wait_ms=1000)
for message in consumer2:
    print(message.value)