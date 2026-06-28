import sqlite3

connection = sqlite3.connect("database/student_management.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS admins(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL

)
""")

cursor.execute("""
INSERT OR IGNORE INTO admins
(name, email, password)

VALUES
(
'Administrator',
'admin@camp.com',
'admin123'
)
""")

connection.commit()

connection.close()

print("Database initialized successfully.")
