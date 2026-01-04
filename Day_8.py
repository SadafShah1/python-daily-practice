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
