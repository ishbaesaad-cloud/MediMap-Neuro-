import streamlit as st
from openai import OpenAI
import json

# 1. UI Setup - Professional Healthcare Theme
st.set_page_config(page_title="Neuro-Triage Auditor", page_icon="🧠", layout="wide")
st.title("🧠 Neuro-Triage Auditor")
st.subheader("Clinical Decision Support: Migraine vs. Secondary Risks")
st.markdown("""
*Grounding Source: SNOOP10 Framework (Mayo Clinic, Cleveland Clinic, Harvard, Oxford, PubMed)*
---
""")

# 2. Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.info("This app uses SNOOP10 criteria to audit risk levels for headaches.")

# 3. The 12 Clinical Variables (Input Form)
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

# 4. The Processing Logic
if submitted:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        client = OpenAI(api_key=api_key)
        
        # Constructing the "HPI" (History of Present Illness)
        case_data = f"""
        - Onset: {onset}
        - One-sided: {side}
        - Vision Changes: {vision}
        - Nausea: {nausea}
        - Fever/Neck Stiffness: {fever}
        - Weakness/Confusion: {weakness}
        - Recent Injury: {injury}
        - BP: {bp}
        - Diabetes: {diabetes}
        - Stress: {stress}/10
        - Sleep: {sleep}h
        - New Pattern: {recent_change}
        """

        # System Prompt with High-Knowledge Grounding
        system_prompt = """
        You are a Senior Neurological Consultant Audit Engine. 
        Apply SNOOP10 criteria from Mayo Clinic, Harvard, and Oxford.
        
        Logic:
        - Sudden onset (<1 min) = Thunderclap (SAH risk).
        - Fever + Headache = Meningitis rule-out.
        - Weakness/Confusion = Stroke/TIA rule-out.
        - BP >180/120 = Hypertensive emergency.
        
        Return ONLY JSON:
        {
            "urgency_score": 1-10,
            "color": "Red/Yellow/Green",
            "simple_why": "5th grade English explanation.",
            "clinical_audit": "Technical reasoning citing PubMed/Mayo/SNOOP10.",
            "rule_outs": ["Disease 1", "Disease 2"],
            "doctor_note": "Technical summary for ER staff."
        }
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Audit this case: {case_data}"}
                ],
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)

            # 5. Display Results
            st.divider()
            
            # Urgency Header
            color_map = {"Red": "#ff4b4b", "Yellow": "#ffa500", "Green": "#28a745"}
            st.markdown(f"<h1 style='text-align: center; color: {color_map.get(result['color'])};'>URGENCY: {result['urgency_score']}/10</h1>", unsafe_allow_all_with_header=True)
            
            r_col1, r_col2 = st.columns(2)
            with r_col1:
                st.info(f"**The 'Simple' Why:**\n\n{result['simple_why']}")
                st.error("**Rule-Out Targets:**\n\n" + "\n".join([f"- {r}" for r in result['rule_outs']]))
            
            with r_col2:
                st.success(f"**Clinical Audit (Academic):**\n\n{result['clinical_audit']}")
                st.warning(f"**Handover for your Doctor:**\n\n{result['doctor_note']}")

        except Exception as e:
            st.error(f"Error connecting to AI: {e}")