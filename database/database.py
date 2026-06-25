import sqlite3

DATABASE_NAME = "database/student_management.db"


def create_database():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        student_id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        roll_number TEXT UNIQUE,

        branch TEXT,

        year TEXT,

        section TEXT,

        email TEXT,

        phone TEXT

    )
    """)

    conn.commit()

    conn.close()

    print("Database Created Successfully")


if __name__ == "__main__":
    create_database()