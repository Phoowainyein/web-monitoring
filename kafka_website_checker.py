#!/usr/bin/python3

# Importing  libraries
import sys
import time
from kafka import KafkaProducer
import json
from functionality import *
import pandas as pd
from pydoc_data.topics import topics
from urllib import response
from kafka import KafkaConsumer,TopicPartition


if __name__ == '__main__':
    lst_to_csv('target_websites.csv',website_lists)#from functionality.py
    time.sleep(2.5)
    data=pd.read_csv('target_websites.csv')

    
    for websites in data.target_websites:
        
        producer = KafkaProducer(
        bootstrap_servers='kafka-1ac287d-phoowai1995-bc35.aivencloud.com:17205',
        security_protocol="SSL",
        ssl_cafile="./ca.pem",
        ssl_certfile="./service.cert",
        ssl_keyfile="./service.key",
        value_serializer= lambda value:json.dumps(value).encode('utf-8')
        )
        producer.send('website-checker',monitor_(websites))
        producer.flush()    
                      
    print("Producer  run successfully!") 
    time.sleep(5)
    consumer = KafkaConsumer(
    bootstrap_servers='kafka-1ac287d-phoowai1995-bc35.aivencloud.com:17205',
    security_protocol="SSL",
    ssl_cafile="./ca.pem",
    ssl_certfile="./service.cert",
    ssl_keyfile="./service.key",
    value_deserializer = lambda value: json.loads(value.decode('utf-8')),
    auto_offset_reset='earliest',
    )
    consumer.subscribe(topics='website-checker')
    
    status_code_= []
    response_time=[]
    #I could have use message.offset  or other method to stop the loop ,however I like to keep it simple to break the loop with the number
    #of rows from our dataframe
    count=0
    for message in consumer:
        count+=1
        response_time.append(message.value[0])
        status_code_.append(message.value[1])
        if count==len(data):
            break
    print(status_code_,response_time)
    print("Consumer run successfully!")

    #storing the data  consumer has fetched into csv file
    data['status_code']=status_code_
    data['response_time']=response_time
    data.to_csv('target_websites.csv',index=False)
    print("Successfully store the data into csv !")




