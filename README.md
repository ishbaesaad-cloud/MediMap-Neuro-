# MediMap Neuro | Headache Triage Prototype

This project is a high-fidelity concept and layout I designed to show how a clinical decision-making tool for headaches could look and work in real life. 

Rather than building a complex, fully deployed web app that requires hosting and API keys, I designed the entire visual interface as a **Canva Site**. You can click through the interactive UI layout, while the actual medical logic and Python code are stored right here in this GitHub repository.

---

## 🔗 Live Visual Prototype
* **[Click here to open my interactive Canva Site design]** 

---

## 🧠 Why I Built This (The Medical Logic)
As a medical student, I wanted to see how we could make patient triage in emergency rooms or clinics both faster and safer. This design focuses on primary vs. secondary headaches using the established **SNOOP10 framework**

* **Spotting Red Flags:** The layout guides a clinician through checking for critical warning signs (like a sudden "thunderclap" headache, fever, or neurological changes).
* **Clean Doctor Handoffs:** Once the clinician clicks through the triage questions, the tool automatically drafts a clean, structured summary note ready to copy and paste into the patient’s medical chart.

---

## 🛠️ How It's Put Together
* **The Design (Canva):** I used Canva to build the high-fidelity user interface so recruiters and physicians can easily see how the tool is meant to be navigated in a clinical setting.
* **The Brains (Python):** In `app.py`, you'll find the actual backend logic. It contains the scoring algorithms and rules that evaluate the patient's answers.
* **The Build Process (AI-Assisted):** I acted as the clinical architect, designing the diagnostic flows and safety guardrails. I then used AI (Gemini/Claude) as a programming assistant to help me write the Python script and organize the setup.

---

## 📂 What's in this Repository?
* `app.py`: The Python file containing the actual triage logic and scoring algorithms.
* `requirements.txt`: The standard dependencies file.
* `gemini-code-...txt`: A record of the prompts and logic brainstormed during the AI-assisted design phaase.

---

## 🚀 How to Run the App Locally
1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
