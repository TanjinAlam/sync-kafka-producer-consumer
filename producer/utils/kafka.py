from gateway.kafka import Kafka


def get_kafka_producer():
    if Kafka.instance:
        return Kafka.instance
    return Kafka()