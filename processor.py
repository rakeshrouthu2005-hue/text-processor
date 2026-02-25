from rules import calculate_score, get_sentiment
from db import insert_batch

def process_large_file(filename):
    batch = []
    batch_size = 5000

    with open(filename) as f:
        for line in f:
            text = line.strip()
            score = calculate_score(text)
            sentiment = get_sentiment(score)
            batch.append((text, score, sentiment))

            if len(batch) == batch_size:
                insert_batch(batch)
                batch.clear()

        if batch:
            insert_batch(batch)