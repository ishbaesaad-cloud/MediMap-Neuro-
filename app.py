# app.py
# MediMap Neuro - Clinical Decision Logic (SNOOP10 Framework)

def evaluate_headache_triage(symptoms):
    """
    Evaluates headache symptoms based on clinical red flags (SNOOP10 framework)
    and categorizes the risk level.
    """
    red_flags_detected = []
    
    # 1. Systemic symptoms (S)
    if symptoms.get("fever") or symptoms.get("weight_loss"):
        red_flags_detected.append("Systemic symptoms (Fever/Meningismus)")
        
    # 2. Neurologic deficits (N)
    if symptoms.get("weakness") or symptoms.get("confusion") or symptoms.get("vision_changes"):
        red_flags_detected.append("Neurologic deficits or dysfunction")
        
    # 3. Onset (O) - Thunderclap headache
    if symptoms.get("onset") == "Sudden (Seconds/Instant)":
        red_flags_detected.append("Sudden, ultra-rapid onset (Thunderclap risk)")
        
    # 4. Older age (O) - New onset headache in patients > 50
    if symptoms.get("age", 0) >= 50:
        red_flags_detected.append("New-onset headache in patient aged 50 or older")

    # Determine Triage Status
    if len(red_flags_detected) > 0:
        return {
            "triage_level": "RED FLAG - HIGH RISK",
            "clinical_action": "Emergent evaluation required. Rule out secondary etiologies (e.g., SAH, meningitis, mass lesion).",
            "findings": red_flags_detected
        }
    else:
        return {
            "triage_level": "GREEN FLAG - LOW RISK / CONSERVATIVE MANAGEMENT",
            "clinical_action": "Consider primary headache disorders (e.g., Migraine, Tension-type). Monitor for new symptoms.",
            "findings": ["No immediate SNOOP10 red flags detected."]
        }

# --- Example Patient Case Execution ---
if __name__ == "__main__":
    # Simulated incoming patient data from the frontend UI
    patient_case = {
        "age": 28,
        "onset": "Sudden (Seconds/Instant)", # SNOOP Red Flag!
        "fever": True,                       # SNOOP Red Flag!
        "weakness": False,
        "vision_changes": False
    }
    
    print("--- MediMap Neuro Triage Analysis ---")
    result = evaluate_headache_triage(patient_case)
    print(f"Resulting Triage Status: {result['triage_level']}")
    print(f"Detected Risks: {', '.join(result['findings'])}")
    print(f"Recommended Action: {result['clinical_action']}")
