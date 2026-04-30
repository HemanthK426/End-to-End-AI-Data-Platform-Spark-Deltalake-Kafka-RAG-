from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = {"transaction_id": 1, "amount": 5000, "type": "payment"}

while True:
    producer.send("transactions", value=data)
    time.sleep(1)