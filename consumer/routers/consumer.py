import json

from gateway.kafka import Kafka
from models.message import Message
from utils.kafka import get_kafka_consumer_instance
from fastapi import APIRouter, Depends
import logging

router = APIRouter()


@router.post("")
async def send(data: Message, server: Kafka = Depends(get_kafka_consumer_instance)):
    try:
        topic_name = server._topic
        await server.aioconsumer.send_and_wait(topic_name, json.dumps(data.dict()).encode("ascii"))
    except Exception as e:
        await server.aioconsumer.stop()
        raise e
    return 'Message sent successfully'



async def consume(kafka_server):
    consumer = kafka_server.aioconsumer
    await consumer.start()
    try:
        async for message in consumer:
            print("Received",message.value.decode())
            logging.debug("Received",message.value.decode())
    finally:
        await consumer.stop()