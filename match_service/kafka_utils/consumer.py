from kafka import KafkaConsumer
import json

def get_kafka_consumer(topic: str):
    return KafkaConsumer(
        topic,
        bootstrap_servers="kafka:9092",
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )
