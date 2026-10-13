import streamlit as st
import requests
st.set_page_config(page_title="Atlas Crisis Intelligence",layout="wide")
st.title("Atlas Crisis Intelligence")
st.warning("Synthetic portfolio demo only. Not connected to emergency services or live data.")
api=st.sidebar.text_input("FastAPI URL","http://127.0.0.1:8000")
with st.form("incident"):
    question=st.text_area("Planning question","What preparation steps should a team review for flood shelter operations?")
    region=st.text_input("Scenario region","North Valley")
    kind=st.selectbox("Scenario type",["flood","wildfire","earthquake","storm"])
    severity=st.slider("Severity",1,5,3)
    population=st.number_input("Affected population (synthetic)",0,100000,1000)
    rain=st.number_input("Rainfall mm (synthetic)",0.0,1000.0,80.0)
    wind=st.number_input("Wind km/h (synthetic)",0.0,300.0,25.0)
    teams=st.number_input("Teams available (synthetic)",0,100,4)
    submit=st.form_submit_button("Run simulation")
if submit:
    try:
        r=requests.post(api.rstrip("/")+"/analyze",json={"question":question,"region":region,"incident_type":kind,"severity":severity,"affected_population":population,"rainfall_mm":rain,"wind_kmh":wind,"available_teams":teams},timeout=30)
        r.raise_for_status();result=r.json()
        c1,c2,c3=st.columns(3)
        c1.metric("Synthetic risk score",result["risk_score"])
        c2.metric("Risk category",result["risk_level"])
        c3.metric("Retrieved sources",len(result["citations"]))
        st.subheader("Draft response");st.write(result["answer"])
        st.subheader("Evidence");st.json(result["citations"])
        st.subheader("Proposed resources (simulation)");st.json(result["resources"])
        st.subheader("Agent trace");st.write(result["audit"])
    except requests.RequestException as e:st.error(f"API unavailable: {e}")
