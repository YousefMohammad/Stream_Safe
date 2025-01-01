# Stream Safe

A robust and scalable system for real-time transaction monitoring using Kafka, MongoDB, and Matplotlib. This project generates synthetic transaction data, processes it for suspicious activity detection, and provides real-time visualizations of transaction trends.

## Features

- **Data Generation**: Uses the Faker library to generate realistic synthetic transaction data.
- **Real-Time Processing**: Kafka-based producer-consumer architecture ensures seamless transaction streaming.
- **Suspicious Activity Detection**: Automatically flags transactions with amounts exceeding $30,000.
- **Database Integration**: Stores processed transactions in MongoDB for further analysis.
- **Live Visualization**: Dynamic Matplotlib charts visualize transaction trends in real time.

## Installation

1. Install **[Kafka](https://kafka.apache.org/downloads)**, **[Zookeeper](https://zookeeper.apache.org/releases.html)**, and **[Kafka Manager](https://github.com/yahoo/kafka-manager)**.
2. Install **MongoDB**.
3. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/transmon.git
    cd transmon
    ```
4. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Starting the Application

1. Start the Kafka producer:
    ```bash
    python producer.py
    ```

2. Start the Kafka consumer with real-time visualization:
    ```bash
    python consumer.py
    ```

## Project Architecture

- **Producer**: Generates and streams transaction data to Kafka.
- **Consumer**: Processes data, detects anomalies, and stores results in MongoDB while updating live visualizations.
- **Database**: MongoDB stores transaction data for persistence and analytics.

![Architecture](https://via.placeholder.com/800x400?text=System+Architecture)

## Requirements

- Python 3.8+
- Kafka and Zookeeper
- MongoDB
- Python dependencies listed in [`requirements.txt`](requirements.txt)

## Usage

1. Modify `transaction_data.py` (or equivalent) to customize the data schema or generation logic.
2. Adjust thresholds for suspicious activity detection in `consumer.py` if needed.
3. Use `db_connection.py` for database querying and analytics.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[YousefMohammad](https://github.com/YousefMohammad)  
Contact: ymanger34@gmail.com

