from kafka import KafkaConsumer
import json
from db_connection import insert_transaction_to_db
from time import sleep
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='activity-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def real_time_analysis(transaction):
    """Process the transaction to detect suspicious activity."""
    if transaction['amount'] > 30_000:
        print(f"""
        Suspicious activity in transaction {transaction['transaction_id']} 
        with amount {transaction['amount']}
        recorded in {transaction['timestamp']}""")
        transaction['suspicious'] = 1
    else:
        transaction['suspicious'] = 0
    return transaction
def plot_template():
    plt.title('Real-Time Transaction Volume')
    plt.xlabel('Timestamp')
    plt.ylabel('Amount ($)')
    plt.tick_params(axis='x', rotation=10)  # Rotate x-axis labels for readability
    plt.grid(True)

plot_template()
timestamps = []
amounts = []

def plot_recent(timestamps, amounts, recents_):
    recent_stamps = timestamps[len(timestamps) - recents_:] if len(timestamps) >= recents_ else timestamps 
    recent_amounts = amounts[len(amounts) - recents_:] if len(amounts) >= recents_ else amounts
    plt.cla()
    plot_template()
    return recent_stamps, recent_amounts
def update_plot(frame):
    transaction = next(consumer).value
    timestamps.append(transaction['timestamp'])
    amounts.append(transaction['amount'])
    recent_stamps , recent_amounts = plot_recent(timestamps,amounts,10)
    processed_transaction = real_time_analysis(transaction)
    insert_transaction_to_db(processed_transaction)
    sleep(1)  # To avoid overloading the system with rapid inserts
    plt.plot(recent_stamps, recent_amounts, marker='o', linestyle='-', color='b')
    

if __name__ == "__main__":
    ani = FuncAnimation(plt.gcf(), update_plot, frames=None,interval=100, cache_frame_data=False)
    plt.tight_layout()
    plt.show()
