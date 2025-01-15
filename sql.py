import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="ccc",
    password="passw"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
print(mydb)