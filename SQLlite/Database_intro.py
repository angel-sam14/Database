import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT NOT NULL
    )
''')

conn.close()