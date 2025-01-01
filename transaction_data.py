import random
from faker import Faker
# Initialize Faker
fake = Faker()

# Function to generate fake transaction data
def generate_transactions():
    transaction = {
            'transaction_id': fake.uuid4(),
            'user_name': fake.name(),
            'email': fake.email(),
            'amount': round(random.randint(1_000.0, 60_000.0)),  # Random amount between 1 and 10000
            'timestamp': fake.date_time_this_year().strftime('%Y-%m-%d %H:%M'),  # Random timestamp this year
        }
    return transaction

