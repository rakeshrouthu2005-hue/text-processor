import streamlit as st
import os

st.title(" Text Processor")

uploaded_file = st.file_uploader("Upload a text file")

if uploaded_file:
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    if st.button("Run Processing"):
        os.system("python main.py")
        st.success("Processing Done! Check Results page.")