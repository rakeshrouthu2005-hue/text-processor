import os
from concurrent.futures import ThreadPoolExecutor

DATA_FOLDER = "data"

RULES = {
    "great": 2,
    "good": 1
}

def process_file(filename):
    results = []
    with open(os.path.join(DATA_FOLDER, filename), "r") as f:
        for line in f:
            words = line.lower().split()
            for word in words:
                if word in RULES:
                    results.append((line.strip(), word, RULES[word]))
    return results

def parallel_read():
    files = os.listdir(DATA_FOLDER)
    all_results = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(process_file, files)

    for res in results:
        all_results.extend(res)

    return all_results

if __name__ == "__main__":
    output = parallel_read()

    for text, word, score in output:
        print(f"Text: {text}")
        print(f"Matched Word: {word}")
        print(f"Score: {score}")
        print("-" * 40)
