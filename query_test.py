import sqlite3
import time

conn = sqlite3.connect("results_large.db")
cursor = conn.cursor()

start = time.time()

cursor.execute("SELECT COUNT(*) FROM results WHERE sentiment='Positive'")
print("Positive count:", cursor.fetchone()[0])

end = time.time()
print(f"Query Time: {end - start:.4f} seconds")

conn.close()