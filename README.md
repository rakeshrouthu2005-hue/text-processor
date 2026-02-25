# Parallel Text Processor

A Python project that reads multiple text files in parallel and evaluates them using keyword matching and scoring rules.

##  Feature
- Parallel processing using `ThreadPoolExecutor`
- Keyword-based scoring system (positive & negative words)
- Sentiment classification (Positive / Negative / Neutral)
- SQLite database storage of results
- Exception handling for file and database errors
- Clean and structured console output

## 📂 Project Structure
text-processor/
│── data/
│── output/          ← store exports here
│── parallel_processor.py
│── config.py        ← rules & keywords
│── requirements.txt
│── README.md




---

## ▶️ How to Run

### 1️⃣ Prerequisites
- Python 3 installed

### 2️⃣ Add your text files
Place `.txt` files inside the `data/` folder or use `reviews.txt`.

### 3️⃣ Run the script

```bash
python parallel_processor.py

```bash
python parallel_processor.py

##  Example Output

Text: Support team is good and helpful.
Score: 1
Sentiment: Positive
----------------------------------------

Text: The app is bad and slow.
Score: -2
Sentiment: Negative
----------------------------------------

Text: Average experience, nothing special.
Score: 0
Sentiment: Neutral
----------------------------------------

## 📄 Dataset

This project uses a small sample text dataset stored in the `data/` folder and `reviews.txt`.  
The dataset contains example user reviews created for testing the sentiment scoring system.

The text samples simulate real-world feedback such as product reviews, service experiences, and usability comments.

### Performance Test

Dataset size: 1,000,000 records

| Stage | Query Time |
|------|------|
| Before Indexing | 0.0589 seconds |
| After Indexing  | 0.0160 seconds |

**Result:** Indexing improved query performance by ~72%.