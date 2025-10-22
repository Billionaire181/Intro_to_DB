import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "1607"
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")

if mydb.is_connected:
    print("Connected successfully")
else:
    print("Connection Error")

cursor.close()
mydb.close()

