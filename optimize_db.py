import sqlite3
from db import DB_NAME


def optimize():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create indexes for faster queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON results(sentiment)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON results(score)")

    conn.commit()
    conn.close()

    print("✅ Database optimized with indexes")


if __name__ == "__main__":
    optimize()