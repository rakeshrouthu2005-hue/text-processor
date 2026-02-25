import random

sentences = [
    "The product is great",
    "Service is good",
    "The app is bad and slow",
    "Excellent experience",
    "Terrible performance",
    "Average experience",
]

with open("reviews_large.txt", "w") as f:
    for _ in range(1_000_000):
        f.write(random.choice(sentences) + "\n")

print("Generated reviews_large.txt")