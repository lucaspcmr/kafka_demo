from kafka import KafkaProducer
from json import dumps
producer = KafkaProducer(bootstrap_servers='localhost:9093',
                         value_serializer=lambda x: dumps(x).encode('utf-8')
                         )
for i in range(5):
    producer.send('kafka_demo', {"message": i})

for i in range(5, 10):
    producer.send('kafka_demo', {"message": i})


for i in range(10, 15):
    producer.send('kafka_demo', {"message": i})

producer.flush()