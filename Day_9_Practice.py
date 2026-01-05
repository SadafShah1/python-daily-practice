import sqlite3

conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("Sadaf", "sadaf.bibi.dev@gmail.com")
)

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
