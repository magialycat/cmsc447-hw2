import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'database', 'app.db')

def init_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Points INTEGER NOT NULL
    );
    ''')

    cursor.execute('DELETE FROM users')

    test_data = [
        ('Steve Smith', 211, 80),
        ('Jian Wong', 122, 92),
        ('Chris Peterson', 213, 91),
        ('Sai Patel', 524, 94),
        ('Andrew Whitehead', 425, 99),
        ('Lynn Roberts', 626, 90),
        ('Robert Sanders', 287, 75),
    ]
    
    cursor.executemany('INSERT INTO users (Name, Id, Points) VALUES (?, ?, ?)', test_data)
    
    connection.commit()
    connection.close()

def get_db_connection():
    print("Attempting to connect to database at:", DATABASE)
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
