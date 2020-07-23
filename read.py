import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn=None
try:
    conn=sqlite3.connect('student.db')
except Error as e:
    print(e)


def select_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for x in rows:
        print(x)
        def main():
            db_file = "student.db"
            database = r"C:\unwanted\examples"
            conn = create_connection(database)
            with conn:
                print("all students")
                select_students(conn)
            if not __name__ != "__main__":
               main()
