from gateway.kafka import Kafka


def get_kafka_producer():
    if Kafka.instance:
        return Kafka.instance
    return Kafka()

# def get_kafka(instance_type):
#     if instance_type == "consumer":
#         return Kafka(topic="consumer_topic", groupId="consumer_group", port=9092, servers="localhost")
#     elif instance_type == "producer":
#         return Kafka(topic="producer_topic", groupId="producer_group", port=9092, servers="localhost")
#     else:
#         raise ValueError(f"Invalid instance type: {instance_type}")