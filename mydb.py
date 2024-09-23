import mysql.connector

dataBase = mysql.connector.connect(
    host   = 'localhost',
    user   = 'userpython',
    passwd = 'Nourgs#1',
    database='dcrm'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")