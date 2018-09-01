import mysql.connector

mydb = mysql.connector.connect(
	host = "local host",
	user = "root",
	paswd = "Mudah222,",
	database = "Swahilibox"
	)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customer(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")