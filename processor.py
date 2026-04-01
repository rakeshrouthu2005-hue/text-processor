import os
import sqlite3

from db import DB_NAME, init_db
from rules import calculate_score, get_sentiment


def process_large_file(file_path):
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()

            if not text:
                continue

            score = calculate_score(text)
            sentiment = get_sentiment(score)

            cursor.execute(
                "INSERT INTO results (text, score, sentiment) VALUES (?, ?, ?)",
                (text, score, sentiment)
            )

    conn.commit()
    conn.close()