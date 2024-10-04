import json
import psycopg2
from random import randint
import time

conn = psycopg2.connect(
    host="188.225.78.44",
    database="default_db",
    user="gen_user",
    password="nH6j_tXfvdfqYAV4p"
)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS numbers (id SERIAL PRIMARY KEY, number INT, eventTime INT);")
conn.commit()

while True:
    flag = randint(0, 100)
    if flag < 80:
        number = 50 + randint(-5, 5)
    else:
        number = 50 + randint(-30, 30)
    
    print("write", number)
    cur.execute("INSERT INTO numbers (number, eventTime) VALUES (%s, %s)", (number,time.time()))
    conn.commit()
    time.sleep(1)

cur.close()
conn.close()
