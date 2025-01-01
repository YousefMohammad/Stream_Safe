from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['bank_transactions']
collection = db['transactions']

def insert_transaction_to_db(transaction):
    """Insert transaction data into MongoDB."""
    collection.insert_one(transaction)
    print(f"Transaction {transaction['transaction_id']} inserted into MongoDB.")

def get_transactions_from_db():
    """Retrieve all transactions from MongoDB."""
    transactions = collection.find()  # Retrieves all documents from the collection
    return list(transactions)  # Convert cursor to a list    