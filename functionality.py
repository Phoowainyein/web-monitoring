#!/usr/bin/python3
import pandas as pd
import requests
import datetime
from django.http import JsonResponse


"""
Here we can add / remove our desired target websites before creating csv!
"""
website_lists=["https://www.google.com","https://dma.org/",
                "https://pandas.pydata.org/","https://github.com/","https://console.aiven.io/"
                ,'https://www.kaggle.com/','https://www.theconstructsim.com/',
                'https://grabcad.com/library/','https://medium.com/','http://gordonua.com/','https://www.5.ua/',
                'https://humanrights.org.ua/','http://www.example.com'
                ]


def lst_to_csv(csv_file_name,list):#for producer
    print("This python function create csv file from list!")
    df=pd.DataFrame(website_lists)
    return df.to_csv(f'{csv_file_name}',header=['target_websites'],index=False)


def monitor_(url):#for producer
    print("we are in website monitoring function")
    req_ = requests.get(url)
    respTime = round(req_.elapsed.total_seconds(),2)
    return  respTime,req_.status_code
    



