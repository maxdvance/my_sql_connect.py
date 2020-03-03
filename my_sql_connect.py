import mysql.connector

def connect_dbs():
    mydb = mysql.connector.connect(
        host="host",
        user="username",
        passwd="password",
        database="db"
    )
    return mydb
