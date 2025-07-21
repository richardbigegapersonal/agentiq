import streamlit as st
import requests

st.title("AgentIQ Dashboard")
query = st.text_input("Ask a question")

if query:
        res = requests.post("http://localhost:8000/query", json={"question": query})
            st.write(res.json()["answer"])
