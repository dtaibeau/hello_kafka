# dependency: poetry add confluent-kafka pydantic

from confluent_kafka import Producer
from pydantic import BaseModel
import json

# 1) define Pydantic class
class Message(BaseModel):
	text: str
	
# 2) configure Kafka producer
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

# 3) create hello world msg
msg = Message(text="Hello World")

# 4) convert msg to json
serialized_msg = msg.json()

# 5) produce msg!
producer.produce('hello-world', key="key", value=serialized_msg)
producer.flush()

print("Producer message sent: ", serialized_msg)