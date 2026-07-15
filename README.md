# MediMap Neuro | Clinical AI Triage Engine

A responsive, web-based clinical scoring application and triage engine designed to assist in neurological risk stratification and clinical red-flag recognition for headache presentations[cite: 1].

---

## 🎯 Project Overview & Clinical Scaffolding
In emergency and primary care settings, rapid and accurate triage of neurological symptoms is critical. MediMap Neuro was developed to bridge clinical decision guidelines with responsive software interface design[cite: 1]. 

* **Evidence-Based Logic:** Designed symptom-assessment workflows focused on identifying critical secondary headache etiologies (such as Subarachnoid Hemorrhage, meningitis, and hypertensive crises)[cite: 1].
* **Red-Flag Alert System:** Implemented triage screening parameters highlighting critical warning signs (e.g., thunderclap onset, focal neurological deficits, and meningismus)[cite: 1].
* **Clinician Documentation Handoffs:** Built an automated summary output generator to format patient assessments into clean, structured clinical notes ready for attending physicians[cite: 1].

---

## 🛠️ Development & Architecture
* **Clinical Design & Scaffolding:** Acted as the Clinical Architect, mapping out diagnostic workflows, safety boundaries, and assessment scoring rules based on established medical protocols[cite: 1].
* **AI-Assisted Prototyping:** Leveraged generative AI models (Claude/Gemini) as virtual "junior developers" to rapidly generate the React, Tailwind CSS frontend, and Python scripting[cite: 1].
* **Backend Framework:** Built with Python using lightweight application routing to run the evaluation algorithms[cite: 1].

---

## 📂 Repository File Structure
* `app.py`: The core Python application backend containing the scoring algorithms and server routing.
* `requirements.txt`: Python package dependencies required to host and run the application.
* `gemini-code-...`: Prompts and raw logic generated during the collaborative AI-assisted design phase[cite: 1].

---

## 🚀 How to Run the App Locally
1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
