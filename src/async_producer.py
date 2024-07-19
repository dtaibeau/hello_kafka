import asyncio
from aiokafka import AIOKafkaProducer
from pydantic import BaseModel
import json

class Message(BaseModel):
    text: str

async def send_msg():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    # cluster + initial topic info
    await producer.start()
    try:
        msg = Message(text="Hello World")
        serialized_msg = msg.model_dump_json().encode('utf-8')
        # produce msg
        await producer.send_and_wait("hello-world", serialized_msg)
        print("Message sent: ", serialized_msg)
    finally:
        # wait for pending messages to be delivered else expire
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(send_msg())
