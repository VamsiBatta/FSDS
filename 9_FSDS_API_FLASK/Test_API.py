from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/xyz', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(result)


@app.route('/xyz1', methods=["GET", "POST"])
def test1():
    if request.method == "POST":
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify(result)


@app.route('/xyz2', methods=["GET", "POST"])
def test2():
    if request.method == "POST":
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(result)


@app.route('/xyz3', methods=["GET", "POST"])
def test3():
    if request.method == "POST":
        a = request.json['num1']
        b = request.json['num2']
        result = a // b
        return jsonify(result)


if __name__ == '__main__':
    app.run()

# 1. Write a Function to Fetch data from sql table via API
# 2. write a Function to fetch data from mongodb table
