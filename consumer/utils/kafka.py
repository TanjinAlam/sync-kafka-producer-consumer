from gateway.kafka import Kafka


def get_kafka_consumer_instance():
    if Kafka.instance:

        print("INSTANCDE")
        return Kafka.instance
    print("ELSE")
    return Kafka()