import time
from db import init_db
from processor import process_large_file

if __name__ == "__main__":
    init_db()

    start = time.time()
    process_large_file("reviews_large.txt")
    end = time.time()

    print(f"⏱ Processing Time: {end - start:.2f} seconds")