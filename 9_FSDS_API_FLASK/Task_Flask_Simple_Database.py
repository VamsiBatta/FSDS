import mysql.connector as conn
import pymongo
from flask import Flask, request, jsonify

app = Flask(__name__)

# MySQL Connection
mydb = conn.connect(host="localhost", user="root", passwd="12345")
c = mydb.cursor()

c.execute("use exampledb")

# MongoDB Connection
client = pymongo.MongoClient("mongodb+srv://Vamsi:12345@cluster0.9qjcg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['ABC']
coll1 = db['abcd_collection']

"""list1 = [
    {"item": "journal", "instock": [{"warehouse": "A", "qty": 5}, {"warehouse": "C", "qty": 15}]},
    {"item": "notebook", "instock": [{"warehouse": "C", "qty": 5}]},
    {"item": "paper", "instock": [{"warehouse": "A", "qty": 60}, {"warehouse": "B", "qty": 15}]},
    {"item": "planner", "instock": [{"warehouse": "A", "qty": 40}, {"warehouse": "B", "qty": 5}]},
    {"item": "postcard", "instock": [{"warehouse": "B", "qty": 15}, {"warehouse": "C", "qty": 35}]}
]
coll1.insert_many(list1)"""


@app.route("/task1", methods=['GET', 'POST'])
def task1():
    if request.method == "GET":
        c.execute("select * from glass_data")
        x = c.fetchall()
        return jsonify(str(x))


@app.route("/task2", methods=['GET', 'POST'])
def task2():
    if request.method == "GET":
        return jsonify(str([i for i in coll1.find()]))


if __name__ == "__main__":
    app.run()
