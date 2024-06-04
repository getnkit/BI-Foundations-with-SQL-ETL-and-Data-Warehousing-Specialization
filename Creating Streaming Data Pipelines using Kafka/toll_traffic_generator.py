"""
Top Traffic Simulator: This script simulates vehicle traffic passing through toll plazas and sends this data to a Kafka topic.
"""
from time import sleep, time, ctime
from random import random, randint, choice
from kafka import KafkaProducer

# Kafka Configuration
producer = KafkaProducer(bootstrap_servers='localhost:9092')
TOPIC = 'toll'

# Simulation Parameters
VEHICLE_TYPES = ("car", "car", "car", "car", "car", "car", "car", "car",
                 "car", "car", "car", "truck", "truck", "truck",
                 "truck", "van", "van")

# Main Simulation Loop
for _ in range(100000):
    vehicle_id = randint(10000, 10000000)  # Generate a random vehicle ID
    vehicle_type = choice(VEHICLE_TYPES)   # Choose a random vehicle type
    now = ctime(time())                    # Get the current time in a human-readable format
    plaza_id = randint(4000, 4010)         # Generate a random toll plaza ID
    
    # Construct the message to be sent to Kafka
    message = f"{now},{vehicle_id},{vehicle_type},{plaza_id}"
    
    # Encode the message as bytes since Kafka requires byte arrays
    message = bytearray(message.encode("utf-8"))
    print(f"A {vehicle_type} has passed by the toll plaza {plaza_id} at {now}.")
    
    # Send the message to the Kafka topic
    producer.send(TOPIC, message)
    
    # Implement a random delay to simulate real-world traffic patterns.
    sleep(random() * 2)  # Sleep for 0 to 2 seconds (randomly)
