from flask import Flask, jsonify, request

import sqlite3

db = sqlite3.connect("Task.db")

c = db.cursor()

"""#c.execute("CREATE TABLE std(name TEXT, id INT, avg_mark REAL)")
#c.execute("SHOW TABLES")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
c.execute("insert into std values('Vamsi', 5636, 674.4)")
"""
c.execute("drop table std")


# mydb = conn.connect(host="localhost", user="root", passwd="12345")

# c = mydb.cursor()


app = Flask(__name__)

# 1. Write a Function to Fetch data from sql table via API
