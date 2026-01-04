pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello API"

app.run(debug=True)
@app.route("/users")
def users():
    return {"users": ["Ali", "Sara"]}


# practicing
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Day 8 Flask Practice")

@app.route("/skills")
def skills():
    return jsonify(skills=["Python", "AI", "Problem Solving"])

app.run(debug=True)
