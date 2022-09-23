from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/xyz", method = ['GET'])


def test(a, b):
    print(a + b)
    return a+b

test(3, 3)


if __name__ == __main__:
    app.run()






