import sys
import json
from kafka import KafkaProducer

if __name__ == '__main__':
    try: 
        producer = KafkaProducer(
        bootstrap_servers='kafka-1ac287d-phoowai1995-bc35.aivencloud.com:17205',
        security_protocol="SSL",
        ssl_cafile="./ca.pem",
        ssl_certfile="./service.cert",
        ssl_keyfile="./service.key",
        key_serializer=lambda v: json.dumps(v).encode('ascii'),
        value_serializer= lambda v:json.dumps(v).encode('ascii')
        )
        producer.send("test-topic",
                    key={"key": 1},
                    value={"message": "hello world"}
                )
        producer.flush()    
    except:
        sys.exit("No broker available")
