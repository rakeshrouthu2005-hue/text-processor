import sqlite3
from db import DB_NAME

def optimize():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON results(sentiment)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON results(score)")

    conn.commit()
    conn.close()

    print("✅ Database optimized with indexes")

if __name__ == "__main__":
    optimize()
import sqlite3

conn = sqlite3.connect("results_large.db")
cursor = conn.cursor()

cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON results(sentiment)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON results(score)")

conn.commit()
conn.close()

print("Indexes created.")