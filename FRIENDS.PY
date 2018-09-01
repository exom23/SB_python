import mysql.connector


con = mysql.connector.connect(host = 'localhost',
                              database = 'mysql',
                              user = 'root',
                              password = 'Mudah222.')

cur = con.cursor() 
mydb = '''CREATE TABLE ARIF(
            FIRST_NAME VARCHAR(20) NOT NULL, 
            LAST_NAME VARCHAR(20),
            AGE INT,
            SEX VARCHAR(1),
            INCOME FLOAT)'''
cur.execute(mydb) 
con.close() 

print('Database Created successfully')
