import mysql.connector

def connect_dbs():
    try:
        mydb = mysql.connector.connect(
            host="host",
            user="user",
            passwd="password",
            database="db"
        )
        return mydb

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
