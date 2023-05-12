import json

from gateway.kafka import Kafka
from models.message import Message
from utils.kafka import get_kafka_producer

from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("")
async def send(data: Message, server: Kafka = Depends(get_kafka_producer)):
    try:
        topic_name = server._topic
        await server.aioproducer.send_and_wait(topic_name, json.dumps(data.dict()).encode("ascii"))
    except Exception as e:
        await server.aioproducer.stop()
        raise e
    return 'Message sent successfully'
