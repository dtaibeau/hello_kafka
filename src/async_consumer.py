import asyncio
from aiokafka import AIOKafkaConsumer
from pydantic import BaseModel
import json

class Message(BaseModel):
    text: str

async def consume_msg():
    consumer = AIOKafkaConsumer(
        'hello-world',
        bootstrap_servers='localhost:9092',
        group_id='my-group',
        auto_offset_reset='earliest'
    )
    # cluster layout + join group id `my-group`
    await consumer.start()
    try:
        async for msg in consumer:
            deserialized_msg = Message.parse_obj(json.loads(msg.value.decode('utf-8')))
            print("Received message: ", deserialized_msg.text)
    finally:
        # leave consumer group
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume_msg())
