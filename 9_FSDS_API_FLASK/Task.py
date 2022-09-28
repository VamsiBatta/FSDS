import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="12345")
c = mydb.cursor()
c.execute("show databases")
x = c.fetchall()
[print(i) for i in x]

