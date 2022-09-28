import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="12345")
c = mydb.cursor()
c.execute("use exampledb")


@app.route("/abc", methods=['GET', 'POST'])
def task1():
    if request.method == "GET":
        c.execute("select * from glass_data")
        x = c.fetchall()
        return jsonify(str(x))


if __name__ == "__main__":
    app.run()
