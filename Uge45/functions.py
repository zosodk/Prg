import sqlite3
from sqlite3 import Error

def connect_to_db(db_name="students.db"):
    """
    Opretser og returnerer en forbindelse til SQLite databasen.
    """
    try:
        # opretter forbindelsen
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(f"Fejl ved forbindelse til databasen: {e}")
        return None

def create_table(conn):
    """
    Opret en tabel hvis den ikke allerede findes.
    """
    cursor = conn.cursor()
    # Eksempel på en tabel til studerende
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade_point REAL
        )
    """)
    conn.commit()
    return cursor

def insert_student(conn, name, age, grade_point):
    """
    Indsætter en ny studerende i databasen.
    """
    cursor = conn.cursor()
    query = "INSERT INTO students (name, age, grade_point) VALUES (?, ?, ?)"
    cursor.execute(query, (name, age, grade_point))
    conn.commit()
    print(f"Succes! {name} er tilføjet.")

def fetch_all_students(conn):
    """
    Henter alle studerende fra databasen.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
