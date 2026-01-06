@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    if not data or "name" not in data or "email" not in data:
        return jsonify(error="Name and email required"), 400

    conn = get_db_connection()
    cursor = conn.execute(
        "UPDATE users SET name=?, email=? WHERE id=?",
        (data["name"], data["email"], user_id)
    )
    conn.commit()
    conn.close()
if cursor.rowcount == 0:
        return jsonify(error="User not found"), 404

    return jsonify(message="User updated successfully")

             # performing deletion

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )
    conn.commit()
    conn.close()
