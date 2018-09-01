import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table people (name_last, age)")

who = "Kamapua"
age = 21

#This is the qmark style:
cur.execute("insert into people values (?, ?)", (who, age))

#And this is the named style:
cur.execute("select * from people where name_last=:who and age:=age", {"who": who, "age": age})


print cur.fetchone()

#ilileta error