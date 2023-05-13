import json

from gateway.kafka import Kafka
from models.message import Message
from utils.kafka import get_kafka_producer

from fastapi import APIRouter,BackgroundTasks, Depends

router = APIRouter()


@router.post("")
async def send(data: Message,background_tasks: BackgroundTasks, server: Kafka = Depends(get_kafka_producer)):
    try:
        # topic_name = server._topic
        # group_id = server._group_id
        background_tasks.add_task(producer, server,data)
        # producer_consumer = server.create_kafka_consumer('back','test')
        # await producer_consumer.start()
        # await server.aioproducer.send_and_wait(topic_name, json.dumps(data.dict()).encode("ascii"))
    except Exception as e:
        await server.aioproducer.stop()
        raise e
    return 'Message sent successfully'


async def producer(server, data):
    topic_name = server._topic
    producer_consumer = server.create_kafka_consumer('back','test')
    producer = server.aioproducer
    await producer_consumer.start()
    await producer.start()

    # consumer = AIOKafkaConsumer(
    # topicAKG,
    # bootstrap_servers='localhost:9092',group_id='test',
    # session_timeout_ms=60000,
    # rebalance_timeout_ms=30000,
    # max_poll_interval_ms=600000,
    # max_poll_records=100)
    # await consumer.start()

    try:
        for i in range(1, 6):
            # await producer.send_and_wait(topic, value='from producer'.encode())
            await server.aioproducer.send_and_wait(topic_name, json.dumps(data.dict()).encode("ascii"))
            print(f"Iteration: {i}")
            async for message in producer_consumer:
                print("Received ========== ", message.value.decode())
                await producer_consumer.commit()
                break
    finally:
        await producer.stop()
        await producer_consumer.stop()

