import sys
from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    try: 
        consumer = KafkaConsumer(
        bootstrap_servers='kafka-1ac287d-phoowai1995-bc35.aivencloud.com:17205',
        security_protocol="SSL",
        ssl_cafile="./ca.pem",
        ssl_certfile="./service.cert",
        ssl_keyfile="./service.key",
        value_deserializer = lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='earliest',
        )
        consumer.subscribe(topics="test-topic")
        for message in consumer:
            print(message.key ,message.value)
    
    except KeyboardInterrupt:
        sys.exit("key board interrupting!")
    except:
        sys.exit("No broker available")
            
