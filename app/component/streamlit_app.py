import requests
import streamlit as st

API_URL = "http://localhost:8000/api/v1/crew/run"

st.title("Mother-Model Crew")

topic = st.text_input("Topic", placeholder="e.g. AI agent orchestration frameworks")

if st.button("Run") and topic:
    with st.spinner("Researcher, Analyst and Writer are working..."):
        response = requests.post(API_URL, json={"topic": topic}, timeout=120)
    if response.ok:
        st.markdown(response.json()["result"])
    else:
        st.error(f"API error {response.status_code}: {response.text}")
