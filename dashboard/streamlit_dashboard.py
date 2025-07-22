# dashboard/app.py
import streamlit as st
import requests

st.title("🧠 AgentIQ Streamlit Dashboard")
question = st.text_input("Ask a question")

if st.button("Submit") and question:
    response = requests.post("http://localhost:8000/query", json={"question": question})
    st.write("### Answer:")
    st.write(response.json()["answer"])
