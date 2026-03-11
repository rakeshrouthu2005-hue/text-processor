import streamlit as st
import time
import sqlite3
import os

from db import init_db, DB_NAME
from processor import process_large_file

st.title("⚙ Processing Results")

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

init_db()

start = time.time()

process_large_file("temp.txt")

end = time.time()

st.success(f"Processing completed in {end-start:.2f} seconds")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("SELECT sentiment, COUNT(*) FROM results GROUP BY sentiment")
summary = dict(cursor.fetchall())

col1, col2, col3 = st.columns(3)

col1.metric("Positive", summary.get("Positive",0))
col2.metric("Negative", summary.get("Negative",0))
col3.metric("Neutral", summary.get("Neutral",0))

st.bar_chart(summary)

cursor.execute("SELECT * FROM results LIMIT 10")
rows = cursor.fetchall()

st.subheader("Sample Results")
st.dataframe(rows)
conn.close()