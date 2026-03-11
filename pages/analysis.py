import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import smtplib
from email.message import EmailMessage

from db import DB_NAME

st.title("📊 Sentiment Analysis Dashboard")

# connect database
conn = sqlite3.connect(DB_NAME)

df = pd.read_sql_query("SELECT * FROM results", conn)

# show stored results
st.subheader("Stored Results")
st.dataframe(df.head(50))

# sentiment summary
summary = df["sentiment"].value_counts()

st.subheader("Sentiment Summary")
st.write(summary)

# metrics
col1, col2, col3 = st.columns(3)

col1.metric("Positive", summary.get("Positive",0))
col2.metric("Negative", summary.get("Negative",0))
col3.metric("Neutral", summary.get("Neutral",0))

# bar chart
st.subheader("Bar Chart")
st.bar_chart(summary)

# pie chart
st.subheader("Pie Chart")

fig, ax = plt.subplots()
ax.pie(summary.values, labels=summary.index, autopct='%1.1f%%')
ax.axis("equal")

st.pyplot(fig)

# download results
st.subheader("Download Results")

csv = df.head(1000).to_csv(index=False)

st.download_button(
    label="Download Results CSV",
    data=csv,
    file_name="results.csv",
    mime="text/csv"
)

# send results via email
st.subheader("Send Results via Email")

email = st.text_input("Enter Email Address")

if st.button("Send Email"):

    if email == "":
        st.error("Please enter an email")
    else:
        try:
            msg = EmailMessage()
            msg["Subject"] = "Sentiment Analysis Results"
            msg["From"] = os.getenv("EMAIL_USER")
            msg["To"] = email

            msg.set_content("Attached are the sentiment analysis results.")

            msg.add_attachment(
                csv.encode(),
                maintype="text",
                subtype="csv",
                filename="results.csv"
            )

            EMAIL = os.getenv("EMAIL_USER")
            PASSWORD = os.getenv("EMAIL_PASS")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL, PASSWORD)
                smtp.send_message(msg)

            st.success("Email sent successfully!")

        except Exception as e:
            st.error(f"Error sending email: {e}")

conn.close()
