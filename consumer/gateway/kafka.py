import asyncio

from aiokafka import AIOKafkaConsumer


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
        print(self._servers)
        self.aioconsumer = self.create_kafka()
        Kafka.instance = self

    def create_kafka(self):
        loop = asyncio.get_event_loop()
        return AIOKafkaConsumer(
            self._topic,
            loop=loop,
            bootstrap_servers=f'{self._servers}:{self._port}'
        )