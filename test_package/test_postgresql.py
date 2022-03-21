import psycopg2


if __name__ == '__main__':
    print('Initializing test connection...')
    connection=psycopg2.connect('postgres://avnadmin:cLxWxhIA7k6FoQdI@pg-1223551b-phoowai1995-bc35.aivencloud.com:17203/defaultdb?sslmode=require')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS test_table")
    print("creating table!")
    cursor.execute("""CREATE TABLE users (
                    userId serial PRIMARY KEY ,
                    firstName VARCHAR(255),
                    lastName  VARCHAR(255),
                    email    VARCHAR(255));
                    """)
    print("inserting ...")
    cursor.execute("INSERT INTO users(userId,firstName,lastName) VALUES (1,'danny','dine')")
    cursor.execute("SELECT * FROM users")
    print("fetching ...")
    result=cursor.fetchall()
    for row in result:
        print(row)
        
