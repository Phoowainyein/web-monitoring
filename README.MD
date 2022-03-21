## Setup Installation ##


#### For Apache Kafka
```php
pip3 install kafka-python
```
#### For PostgreSQL
```php
pip install psycopg2-binary
```

---
## Task Description ##

Your task is to implement a system that monitors website availability over the network, produces metrics about this and passes these events through an Aiven Kafka instance into an Aiven PostgreSQL database.

For this, you need a Kafka producer which periodically checks the target websites and sends the check results to a Kafka topic, and a Kafka consumer storing the data to an Aiven PostgreSQL database. For practical reasons, these components may run in the same machine (or container or whatever system you choose), but in production use similar components would run in different systems.

The website checker should perform the checks periodically and collect the HTTP response time, status code returned, as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the page.

For the database writer we expect to see a solution that records the check results into one or more database tables and could handle a reasonable amount of checks performed over a longer period of time.
Even though this is a small concept program, returned homework should include tests and proper packaging. If your tests require Kafka and PostgreSQL services, for simplicity your tests can assume those are already running, instead of integrating Aiven service creation and deleting.

Aiven is a Database as a Service vendor and the homework requires using our services. Please register to Aiven at https://console.aiven.io/signup.html at which point you'll automatically be given $300 worth of credits to play around with. The credits should be enough for a few hours of use of our services. If you need more credits to complete your homework, please contact us.

The solution should NOT include using any of the following:
Database ORM libraries - use a Python DB API compliant library and raw SQL queries instead
Extensive container build recipes - rather focus your effort on the Python code, tests, documentation, etc.

---

## MY SOLUTION ##

* functionality.py has two funtion for kafka prouducer.Function called list_to_csv will generate lists of target websites to csv and monitor funtion will return status code and response time.

* kafka_website_checker.py python file has producer and consumer.Producer will send lists of target websites from csv file and consumer fetching the messages from the same topic .After that,the status code and response time will be stored into the same csv file that has been sent .

    Expected kafka_website_checker  Output as below! 
    ![Kafka Output](kafkaf_website_monitor.PNG?raw=true "Kafka website monitor python output")

* data_writer.py will first prepare the data for creating the table,then it will read the csv data and create table into Aiven PostgreSQL database.

    Expected Data Writer Output as below! 
    ![Data Writer Output](data_writer.PNG?raw=true "Data Writer output")

    All the python file should be working properly ,therefore if some errors occurs please contact me :) 
---

## To Run ##

* Run kafka_website_checker.py first and follow up with data_writer.py

## Helpul links for solving this task 
* https://help.aiven.io/en/articles/5343895-python-examples-for-testing-aiven-for-apache-kafka
* https://aiven.io/blog/create-your-own-data-stream-for-kafka-with-python-and-faker
* https://stackoverflow.com/questions/31841191/how-to-stop-python-kafka-consumer-in-program
* https://stackoverflow.com/questions/27193002/insert-tuple-into-table-psycopg2
