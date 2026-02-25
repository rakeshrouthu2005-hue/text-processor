import sqlite3

DB_NAME = "results_large.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        score INTEGER,
        sentiment TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_batch(records):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO results (text, score, sentiment) VALUES (?, ?, ?)",
        records
    )

    conn.commit()
    conn.close()