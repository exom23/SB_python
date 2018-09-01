import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",  
    user = "root",    # use your username
    passwd = "Mudah222."   #use your password
       )
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE  swahilibox") #print mydb
