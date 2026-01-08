from flask import Flask, request, jsonify
import sqlite3
import jwt
import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "change_this_secret"

DB_NAME = "users.db"


#  DATABASE 
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()



#  JWT DECORATOR 

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify(error="Token missing"), 401

        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify(error="Token expired"), 401
        except jwt.InvalidTokenError:
            return jsonify(error="Invalid token"), 401

        return f(*args, **kwargs)
    return decorated
# ---------- REGISTER ----------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data or len(data.get("password", "")) < 6:
        return jsonify(error="Password must be at least 6 characters"), 400

    hashed_password = generate_password_hash(data["password"])

    try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (data["name"], data["email"], hashed_password)
        )
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return jsonify(error="Email already exists"), 409

    return jsonify(message="User registered successfully"), 201
