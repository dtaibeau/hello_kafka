# Kafka Producer and Consumer

This project demonstrates a simple Kafka producer and consumer using both synchronous and asynchronous implementations with `confluent-kafka` and `aiokafka`.

## Features

- Synchronous Kafka producer and consumer using `confluent-kafka`
- Asynchronous Kafka producer and consumer using `aiokafka`
- Data validation and serialization using Pydantic

## Requirements

- [confluent-kafka](https://github.com/confluentinc/confluent-kafka-python) for synchronous Kafka operations
- [aiokafka](https://aiokafka.readthedocs.io) for asynchronous Kafka operations
- [Pydantic](https://pydantic-docs.helpmanual.io) for data validation
- [Poetry](https://python-poetry.org) for dependency management

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hello-kafka.git
    cd hello-kafka
    ```

2. **Install Poetry if you haven't already:**
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. **Install the dependencies:**
    ```bash
    poetry install
    ```

## Usage

### Synchronous Implementation

1. **Activate the virtual environment:**
    ```bash
    poetry shell
    ```

2. **Run the synchronous producer:**
    ```bash
    poetry run python src/producer.py
    ```

3. **Run the synchronous consumer:**
    ```bash
    poetry run python src/consumer.py
    ```

### Asynchronous Implementation

1. **Activate the virtual environment:**
    ```bash
    poetry shell
    ```

2. **Run the asynchronous producer:**
    ```bash
    poetry run python src/async_producer.py
    ```

3. **Run the asynchronous consumer:**
    ```bash
    poetry run python src/async_consumer.py
    ```

## Project Structure

```plaintext
├── README.md                # Project README file
├── pyproject.toml           # Poetry configuration file
├── poetry.lock              # Poetry lock file
├── src/
│   ├── producer.py          # Synchronous Kafka producer script
│   ├── consumer.py          # Synchronous Kafka consumer script
│   ├── async_producer.py    # Asynchronous Kafka producer script
│   └── async_consumer.py    # Asynchronous Kafka consumer script
```

## How to Contribute
- Fork the repository:
```bash
git clone https://github.com/yourusername/hello-kafka.git
cd hello-kafka
```

- Create your feature branch:
```bash
git checkout -b feature/awesome_feature
```

- Commit your changes:
```bash
git commit -m 'Add feature'
```

- Push to branch:
```bash
git push origin feature/awesome_feature
```

- Open a pull request: Go to the forked repository on GitHub and click on the "New Pull Request" button!

:P