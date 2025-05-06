import streamlit as st

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.pdf_extract import extract_text_from_pdf
from backend.web_extract import extract_text_from_url
from backend.agentic_ai import agentic_decision_maker

# Streamlit UI
st.title("Open-Source AI Summarizer with Agentic Behavior")

st.subheader("Select your input source")
option = st.selectbox("Choose input source", ["PDF", "URL"])

text = ""

if option == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)

elif option == "URL":
    url = st.text_input("Enter URL:")
    if url:
        text = extract_text_from_url(url)

if text:
    st.write("Text extracted successfully!")

    keyword = st.text_input("Enter a keyword to filter relevant information:")
    if keyword:
        action = st.selectbox("Choose action", ["summarize", "extract"])
        if st.button("Process"):
            result = agentic_decision_maker(text, action, keyword)
            st.write(result)
