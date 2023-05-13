import asyncio

from aiokafka import AIOKafkaProducer,AIOKafkaConsumer


class Kafka:
    instance = None

    def __init__(
        self,
        topic,
        port,
        servers
    ) -> None:
        self._topic = topic
        self._port = port
        self._servers = servers
        self.aioproducer = self.create_kafka_producer()
        Kafka.instance = self

    def create_kafka_producer(self):
        loop = asyncio.get_event_loop()
        return AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=f'{self._servers}:{self._port}'
        )
    def create_kafka_consumer(self, topic_name, group_id):
        loop = asyncio.get_event_loop()
        return AIOKafkaConsumer(
            topic_name,
            group_id=group_id,
            loop=loop,
            bootstrap_servers=f'{self._servers}:{self._port}'
        )