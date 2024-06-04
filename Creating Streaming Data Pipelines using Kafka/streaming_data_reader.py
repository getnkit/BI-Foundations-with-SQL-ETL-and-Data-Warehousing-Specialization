"""
Streaming data consumer for ingesting toll data from Kafka and loading it into MySQL.
"""
from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

# Configuration
TOPIC='toll'
DATABASE = 'tolldata'
USERNAME = 'root'
PASSWORD = 'MTcxMTktdTYzMDEw'

# Connect to MySQL database
print("Connecting to the database")
try:
    connection = mysql.connector.connect(host='localhost', database=DATABASE, user=USERNAME, password=PASSWORD)
except Exception:
    print("Could not connect to database. Please check credentials")
else:
    print("Connected to database")
cursor = connection.cursor()

# Connect to Kafka consumer
print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC)
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")
for msg in consumer:

    # Extract information from kafka
    message = msg.value.decode("utf-8")

    # Transform the date format to suit the database schema
    (timestamp, vehcile_id, vehicle_type, plaza_id) = message.split(",")

    dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
    timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

    # Loading data into the database table
    sql = "insert into livetolldata values(%s,%s,%s,%s)"
    result = cursor.execute(sql, (timestamp, vehcile_id, vehicle_type, plaza_id))
    print(f"A {vehicle_type} was inserted into the database")
    # Commit the transaction to ensure data persistence
    connection.commit()

# Close the database connection when done
connection.close()
