from confluent_kafka import Consumer, KafkaError, KafkaException
from pydantic import BaseModel
import json

# 1) define Pydantic class for Consumer
class Message(BaseModel):
    text: str

# 2) config Consumer
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(config)

# 3) subscribe to topic
consumer.subscribe(['hello-world'])

# 4) error handling, if all successful deserialize msg and close connection
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        else:
            # Deserialize the message using Pydantic
            deserialized_msg = Message.parse_raw(msg.value().decode('utf-8'))
            print("Received message: ", deserialized_msg.text)
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
