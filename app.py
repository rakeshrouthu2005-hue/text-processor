import streamlit as st

st.title("📊 Text Processor")

st.write("Upload a text file to analyze sentiment.")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:

    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    if st.button("Run Processing"):
        st.switch_page("pages/results.py")