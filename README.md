# Parallel Text Processor with Sentiment Analysis

A Python application that processes large text datasets, performs sentiment analysis, and provides an interactive dashboard for exploring results.

The system uses **parallel processing**, **database storage**, and a **Streamlit web interface** to analyze text files efficiently.

---

# Features

### Parallel Text Processing

Uses `ThreadPoolExecutor` to process large numbers of text records efficiently.

### Keyword-Based Sentiment Analysis

Sentiment is calculated using rule-based keyword scoring:

* Positive words increase score
* Negative words decrease score

Classification categories:

* Positive
* Negative
* Neutral

### SQLite Database Storage

Processed results are stored in an **SQLite database** for efficient querying and analysis.

### Query Optimization

Indexes are added to the database to improve query performance for large datasets.

### Interactive Streamlit UI

The application provides a web interface where users can:

* Upload text files
* Process large datasets
* View processed results
* Analyze sentiment statistics

### Data Visualization

The dashboard includes:

* Sentiment summary
* Bar chart visualization
* Pie chart visualization

### Export Options

Users can:

* Download results as a CSV file
* Send analysis results via email

---

# Project Structure

```
text-processor/
│
├── data/
│   ├── file1.txt
│   ├── file2.txt
│   ├── file3.txt
│   ├── file4.txt
│   └── file5.txt
│
├── pages/
│   ├── results.py
│   └── analysis.py
│
├── app.py
├── processor.py
├── db.py
├── rules.py
├── generate_data.py
├── optimize_db.py
├── query_test.py
│
├── README.md
└── .gitignore
```

---

# Installation

### Clone the repository

```
git clone https://github.com/rakeshrouthu2005-hue/text-processor.git
cd text-processor
```

### Install dependencies

```
pip install streamlit pandas matplotlib
```

---

# Running the Application

Start the Streamlit application:

```
python -m streamlit run app.py
```

Then open your browser:

```
http://localhost:8501
```

---

# Usage

1. Upload a `.txt` file containing text data.
2. The application processes the data and stores results in the database.
3. Navigate to the **Results page** to view processed records.
4. Open the **Analysis page** to see sentiment statistics and charts.
5. Download results as CSV or send them via email.

---

# Dataset

This project uses text datasets containing simulated product reviews and feedback.

Example text samples include:

* Product reviews
* Service feedback
* User experience comments

These datasets are used to demonstrate large-scale text processing and sentiment analysis.

---

# Performance Test

Dataset size: **1,000,000 records**

| Stage           | Query Time     |
| --------------- | -------------- |
| Before Indexing | 0.0589 seconds |
| After Indexing  | 0.0160 seconds |

Result:

**Database indexing improved query performance by ~72%.**

---

# Email Configuration

Email credentials are stored using **environment variables** to avoid exposing sensitive information.

Set them using:

```
setx EMAIL_USER "your_email@gmail.com"
setx EMAIL_PASS "your_app_password"
```

Restart your terminal after setting these values.

---

# Author

Rakesh Routhu
