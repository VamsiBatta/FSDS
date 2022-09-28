from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/xyz", methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        a = request.json["num1"]
        b = request.json["num2"]
        r = a+b
        result = "The Sum of " + str(a) + " and " + str(b) + " is " + str(r)
        return jsonify(str(result))


@app.route("/xyz1", methods=['GET', 'POST'])
def test1():
    if request.method == "POST":
        a = request.json["num1"]
        b = request.json["num2"]
        r = a - b
        result = "The Substraction of " + str(a) + " and " + str(b) + " is " + str(r)
        return jsonify(str(result))


@app.route("/xyz2", methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        a = request.json["num1"]
        b = request.json["num2"]
        r = a * b
        result = "The Multplication of " + str(a) + " and " + str(b) + " is " + str(r)
        return jsonify(str(result))


@app.route("/xyz3", methods=['GET', 'POST'])
def test3():
    if request.method == "POST":
        a = request.json["num1"]
        b = request.json["num2"]
        r = a / b
        result = "The Quotient of " + str(a) + " and " + str(b) + " is " + str(r)
        return jsonify(str(result))


if __name__ == "__main__":
    app.run()


# TASK

# 1. Write a Function to fetch data from sql table via api
# 2. Write a function to fetch data from a mongodb file
