@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data or "name" not in data or "email" not in data or "password" not in data:
        return jsonify(error="All fields required"), 400

    hashed_password = generate_password_hash(data["password"])
    
try:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (data["name"], data["email"], hashed_password)
        )
