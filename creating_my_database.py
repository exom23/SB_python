import mysql.connector

## CREATE A CONNECTION TO THE DATABASE
con = mysql.connector.connect(host = 'localhost',database = 'mysql',user = 'root',password = 'Mudah222.')
# CREATE A CURSOR 
cur = con.cursor() 
#EXECUTE QUERY 
mydb = '''CREATE TABLE FRIENDS(
				FIRST_NAME CHAR(20) NOT NULL, 
				LAST_NAME CHAR(20),
				AGE INT,
				SEX CHAR(1),
				INCOME FLOAT)'''
cur.execute(mydb) # THIS WILL EXECUTE THE QUERY
con.close() # WILL CLOSE THE CONNECTION BETWEEN THE DATABASE
#PRINT A STATEMENT
print('Database Created successfully')