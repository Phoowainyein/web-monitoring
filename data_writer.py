import psycopg2
from psycopg2 import extras
import pandas as pd 


"""preparation for database ! """
data=pd.read_csv('target_websites.csv')
data.reset_index(inplace=True)
renaming_cols={  'index': 'websiteId INTEGER PRIMARY KEY NOT NULL',
                'target_websites': 'target_websites TEXT'
                ,'status_code': 'status_code INTEGER',
                'response_time': 'response_time REAL'
                }

data.rename(columns=renaming_cols,inplace=True)
data.to_csv('website_list.csv',index=False)

print('Connecting to the PostgreSQL database called website-monitor...')
connection=psycopg2.connect('your database engine here')
cursor = connection.cursor()

def table_fields(file):
    my_fields=[]
    my_files =open(file)
    table_fields = my_files.readline()
    table_fields=table_fields.replace("\n","")
    my_fields.append(table_fields) 
    for i in my_fields:
        return i

file='website_list.csv'
def fetch_rows(file):
    fetch_rows_=[]
    for i in open(file):
        i=i.replace("\n","").split(",")
        fetch_rows_.append(i)
    fetch_rows_.pop(0)
    return fetch_rows_


def dropAndCreateTable(table_name,*fields):
    print("We are in drop and CreateTable function")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    fields_=list(fields)
    fields_str = ",".join(fields)
    return cursor.execute("CREATE TABLE {} ({});".format(table_name,fields_str))

def insertData(*table_data):
    print("We are in insertData function")
    tab_name=table_data[0]
    tab_values=table_data[1]
    table_value=[tuple(z) for z in tab_values]
    return extras.execute_values(cursor,"INSERT INTO website_list (websiteId,target_websites,status_code,response_time) VALUES %s",table_value) 
     
        
  

if __name__ == '__main__':
    table_name=lambda tab_name: tab_name[:len(tab_name) - 4]
    print(table_fields(file))
    dropAndCreateTable(table_name(file),table_fields(file))
    insertData(table_name(file),fetch_rows(file))
    print("print the table")
    cursor.execute("SELECT * FROM website_list")
    table_data=cursor.fetchall()
    for row in table_data:
        print(row)
    connection.commit()
    connection.close()
    print("Data writer run successfully!")
    
        

        
