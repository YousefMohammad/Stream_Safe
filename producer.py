from kafka import KafkaProducer
import json
import time
from transaction_data import generate_transactions

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Function to send data to Kafka
def send_to_kafka(transaction_data):
    producer.send('transactions', value=transaction_data)

# Send fake data every 2 seconds
while True:
    transaction = generate_transactions()
    print(transaction)
    send_to_kafka(transaction)
    time.sleep(1)  # Adjust frequency as needed
