from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "users.db"


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
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    if not data or "name" not in data or "email" not in data:
        return jsonify(error="Name and email required"), 400

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (data["name"], data["email"])
    )
    conn.commit()
    conn.close()

    return jsonify(message="User added successfully"), 201


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return jsonify([dict(user) for user in users])


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
