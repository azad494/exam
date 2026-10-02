import requests
import streamlit as st

BASE_URL = "http://localhost:8000/api/v1/agents"

st.title("Researcher -> Analyst -> Writer")

topic = st.text_input("Topic", placeholder="e.g. AI agent orchestration frameworks")

if st.button("Run") and topic:
    with st.spinner("Researcher is searching the web..."):
        r1 = requests.post(f"{BASE_URL}/researcher/run", json={"topic": topic}, timeout=120)

    if not r1.ok:
        st.error(f"Researcher error {r1.status_code}: {r1.text}")
    else:
        research_notes = r1.json()["research_notes"]

        with st.spinner("Analyst is interpreting the research..."):
            r2 = requests.post(
                f"{BASE_URL}/analyst/run",
                json={"topic": topic, "research_notes": research_notes},
                timeout=120,
            )

        if not r2.ok:
            st.error(f"Analyst error {r2.status_code}: {r2.text}")
        else:
            insights = r2.json()["insights"]

            with st.spinner("Writer is drafting the final piece..."):
                r3 = requests.post(
                    f"{BASE_URL}/writer/run",
                    json={"topic": topic, "insights": insights},
                    timeout=120,
                )

            if not r3.ok:
                st.error(f"Writer error {r3.status_code}: {r3.text}")
            else:
                st.markdown(r3.json()["article"])

                with st.expander("See research notes and insights"):
                    st.markdown("**Research notes**")
                    st.write(research_notes)
                    st.markdown("**Insights**")
                    st.write(insights)
