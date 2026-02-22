import os
import sqlite3
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# =========================
# CONFIG
# =========================
DATA_FOLDER = "data"

POSITIVE_WORDS = {
    "great": 2,
    "good": 1,
    "excellent": 3,
    "amazing": 3,
    "helpful": 1
}

NEGATIVE_WORDS = {
    "bad": -2,
    "slow": -1,
    "poor": -2,
    "terrible": -3
}

# =========================
# DATABASE SETUP
# =========================
def init_db():
    try:
        conn = sqlite3.connect("results.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                score INTEGER,
                sentiment TEXT,
                timestamp TEXT
            )
        """)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Database initialization error:", e)

# =========================
# SENTIMENT LOGIC
# =========================
def calculate_score(text):
    score = 0
    words = text.lower().split()

    for word in words:
        if word in POSITIVE_WORDS:
            score += POSITIVE_WORDS[word]
        if word in NEGATIVE_WORDS:
            score += NEGATIVE_WORDS[word]

    return score

def get_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# =========================
# SAVE TO DATABASE
# =========================
def save_result(text, score, sentiment):
    try:
        conn = sqlite3.connect("results.db")
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO results (text, score, sentiment, timestamp)
            VALUES (?, ?, ?, ?)
        """, (text, score, sentiment, timestamp))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Database error:", e)

# =========================
# FILE PROCESSING
# =========================
def process_file(filename):
    results = []

    try:
        filepath = os.path.join(DATA_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                text = line.strip()
                if not text:
                    continue

                score = calculate_score(text)
                sentiment = get_sentiment(score)

                save_result(text, score, sentiment)
                results.append((text, score, sentiment))

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

    return results

# =========================
# PARALLEL PROCESSING
# =========================
def parallel_read():
    files = os.listdir(DATA_FOLDER)
    all_results = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(process_file, files)

    for res in results:
        all_results.extend(res)

    return all_results

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    init_db()

    output = parallel_read()

    print("\n=== Processing Results ===\n")

    for text, score, sentiment in output:
        print(f"Text: {text}")
        print(f"Score: {score}")
        print(f"Sentiment: {sentiment}")
        print("-" * 40)

    print("✅ Results saved to results.db")