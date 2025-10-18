import sqlite3

def create_tables():
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            frequency TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY (habit_id) REFERENCES habits (id)
        )
    ''')
    conn.commit()
    conn.close()

def add_habit(name, frequency):
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("INSERT INTO habits (name, frequency) VALUES (?, ?)", (name, frequency))
    conn.commit()
    conn.close()

def get_habits():
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("SELECT id, name, frequency FROM habits")
    habits = c.fetchall()
    conn.close()
    return habits

def log_habit(habit_id, date, status):
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (habit_id, date, status) VALUES (?, ?, ?)", (habit_id, date, status))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect("habits.db")
    c = conn.cursor()
    c.execute("""
        SELECT h.name, l.date, l.status 
        FROM logs l JOIN habits h ON h.id = l.habit_id
        ORDER BY l.date DESC
    """)
    logs = c.fetchall()
    conn.close()
    return logs
