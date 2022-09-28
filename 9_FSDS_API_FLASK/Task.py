import mysql.connector as conn

db = conn.connect(host="localhost", user="root", passwd="12345")

c = db.cursor()

#c.execute("drop database example")

c.execute("show databases")

x = c.fetchall()
[print(i) for i in x]

print("\n\n")
c.execute("use exampledb")


c.execute("show tables")

x = c.fetchall()
[print(i) for i in x]
print("\n\n")

c.execute("")
x = c.fetchall()
[print(i) for i in x]
print("\n\n")


