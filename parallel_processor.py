import os
import sqlite3
from concurrent.futures import ThreadPoolExecutor

DATA_FOLDER = "data"

RULES = {
    "great": 2,
    "good": 1
}

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            matched_word TEXT,
            score INTEGER
        )
    """)

    conn.commit()
    conn.close()

def save_result(text, word, score):
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO results (text, matched_word, score) VALUES (?, ?, ?)",
        (text, word, score)
    )

    conn.commit()
    conn.close()

# ---------- FILE PROCESSING ----------
def process_file(filename):
    results = []
    with open(os.path.join(DATA_FOLDER, filename), "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                if word in RULES:
                    results.append((line.strip(), word, RULES[word]))
    return results

# ---------- PARALLEL EXECUTION ----------
def parallel_read():
    files = os.listdir(DATA_FOLDER)
    all_results = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(process_file, files)

    for res in results:
        all_results.extend(res)

    return all_results

# ---------- MAIN ----------
if __name__ == "__main__":
    init_db()  # create DB + table

    output = parallel_read()

    for text, word, score in output:
        print(f"Text: {text}")
        print(f"Matched Word: {word}")
        print(f"Score: {score}")
        print("-" * 40)

        save_result(text, word, score)  # insert into DB

    print("\n✅ Results saved to results.db")
