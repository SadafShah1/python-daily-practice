pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello API"

app.run(debug=True)
@app.route("/users")
def users():
    return {"users": ["Ali", "Sadaf"]}


# practicing
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello World")

@app.route("/skills")
def skills():
    return jsonify(skills=["Python", "AI", "Problem Solving"])

app.run(debug=True)
