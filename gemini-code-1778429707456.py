import streamlit as st
from openai import OpenAI
import json

st.set_page_config(page_title="Neuro-Triage Auditor", page_icon="🧠", layout="wide")
st.title("🧠 Neuro-Triage Auditor")
st.subheader("Clinical Decision Support: Migraine vs. Secondary Risks")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")

with st.form("triage_form"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Symptom Profile")
        onset = st.selectbox("How fast did pain reach its peak?", ["Gradual (Minutes/Hours)", "Sudden (Seconds/Instant)"])
        side = st.radio("Is it one-sided?", ["Yes", "No (Whole head/Both sides)"])
        vision = st.radio("Vision changes (blurring, loss, double)?", ["No", "Yes"])
        nausea = st.radio("Nausea or vomiting?", ["No", "Yes"])
        fever = st.radio("Fever or stiff neck?", ["No", "Yes"])
        weakness = st.radio("One-sided weakness or confusion?", ["No", "Yes"])
    with col2:
        st.write("### History & Context")
        injury = st.radio("Recent head injury?", ["No", "Yes"])
        bp = st.text_input("Blood Pressure (if known, e.g. 150/95)", "Unknown")
        diabetes = st.radio("History of Diabetes?", ["No", "Yes"])
        stress = st.slider("Current Stress Level", 1, 10, 5)
        sleep = st.slider("Sleep last night (hours)", 0, 12, 7)
        recent_change = st.radio("Is this a brand new type of pain for you?", ["No", "Yes"])

    submitted = st.form_submit_button("🚀 RUN CLINICAL AUDIT")

if submitted:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        client = OpenAI(api_key=api_key)
        case_data = f"Onset: {onset}, One-sided: {side}, Vision: {vision}, Nausea: {nausea}, Fever: {fever}, Weakness: {weakness}, Injury: {injury}, BP: {bp}, Diabetes: {diabetes}, Stress: {stress}, Sleep: {sleep}, New Pattern: {recent_change}"
        system_prompt = "You are a Senior Neurological Consultant. Apply SNOOP10 criteria. Return ONLY JSON with urgency_score (1-10), color (Red/Yellow/Green), simple_why, clinical_audit, rule_outs, and doctor_note."
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": case_data}],
                response_format={"type": "json_object"}
            )
            result = json.loads(response.choices[0].message.content)
            st.divider()
            color_map = {"Red": "#ff4b4b", "Yellow": "#ffa500", "Green": "#28a745"}
            st.markdown(f"<h1 style='text-align: center; color: {color_map.get(result['color'])};'>URGENCY: {result['urgency_score']}/10</h1>", unsafe_allow_all_with_header=True)
            st.info(f"**The 'Simple' Why:** {result['simple_why']}")
            st.success(f"**Clinical Audit:** {result['clinical_audit']}")
            st.warning(f"**Doctor Note:** {result['doctor_note']}")
        except Exception as e:
            st.error(f"Error: {e}")