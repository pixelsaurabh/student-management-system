from database.database import get_connection


def get_all_students():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    return students


def insert_student(name, roll_number, branch, year, section, email, phone):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (
            name,
            roll_number,
            branch,
            year,
            section,
            email,
            phone
        )

        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?
        )
        """,
        (
            name,
            roll_number,
            branch,
            year,
            section,
            email,
            phone
        )
    )

    connection.commit()

    connection.close()
