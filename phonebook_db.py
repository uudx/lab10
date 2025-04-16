import psycopg2
import csv

database = "phonebook_db"
user = "postgres"
password = "pilot010407"

conn = psycopg2.connect(host = "localhost", database = database, user=user, password=password, port = "5432")
cur = conn.cursor()

#cur.execute(f'CREATE DATABASE phonebook_db')

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(f"INSERT INTO {database} (first_name, phone) VALUES (%s, %s)", (name, phone))

def insert_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(f"INSERT INTO {database} (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))

def query_all():
    cur.execute(f"SELECT * FROM {database}")
    for row in cur.fetchall():
        print(row)

def query_by_name(name):
    cur.execute(f"SELECT * FROM {database} WHERE first_name ILIKE %s", ('%' + name + '%',))
    for row in cur.fetchall():
        print(row)

def delete_by_name(name):
    cur.execute(f"DELETE FROM {database} WHERE first_name=%s", (name,))

conn.commit()
cur.close()
conn.close()
