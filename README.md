# MediMap Neuro — Clinical Decision Support Logic for Headache Triage

**A rules-based triage scoring engine built on the SNOOP10 clinical framework, translating a headache triage protocol into a testable classification algorithm with sample-case validation.**

[▶ Interactive UI Prototype (Canva)](https://medimap-neuro.my.canva.site/)

---

## Problem

Emergency rooms and outpatient clinics need a fast, consistent way to separate low-risk ("primary") headaches from potentially dangerous ("secondary") ones. Manual triage is inconsistent and depends heavily on individual clinician experience — a gap where structured decision logic can reduce variability and catch red flags earlier.

## Approach

I designed the triage logic around the **SNOOP10 framework** (established red-flag criteria for secondary headache used in clinical guidelines) and translated it into a rules-based scoring algorithm in Python:

- **Input:** patient-reported symptoms and history, mapped to the 10 SNOOP10 categories (Systemic symptoms, Neurologic signs, Onset, Older age, Pattern change, Positional, Precipitated, Papilledema, Progressive, Pregnancy)
- **Logic:** `app.py` scores each flag by clinical severity and classifies the case into a **Red / Yellow / Green urgency tier**
- **Output:** a structured, chart-ready summary note generated automatically for each case

## Sample Output

Running `app.py` on 5 sample cases produces:

```
Total cases: 5
RED: 3
YELLOW: 1
GREEN: 1
```

Example single-case output:

```
--- MediMap Neuro Triage Summary ---
Case ID: CASE-001
Age: 34
SNOOP10 Score: 8
Urgency Tier: RED
Flags identified:
  - Onset - thunderclap (sudden, severe, peak <1 min)
  - Neurologic signs/symptoms (focal deficit, confusion, seizure)
Guidance: Recommend urgent evaluation / imaging per institutional protocol.
-------------------------------------
```

## Tech Stack

- **Python** (standard library only — no external dependencies)
- **Canva** — high-fidelity UI prototype for clinical usability review
- AI-assisted development (Claude/Gemini used as a coding assistant for implementation; clinical logic, diagnostic flow, and safety guardrails designed by me)

## Repository Contents

| File | Description |
|---|---|
| `app.py` | SNOOP10 scoring engine, tier classification logic, and 5 sample patient cases |
| `requirements.txt` | Dependency file (none required — Python 3.8+ stdlib) |

## How to Run

```bash
python app.py
```

This runs the scoring engine against the 5 built-in sample cases and prints a triage summary note plus a tier breakdown for each.

## Disclaimer

This is a portfolio prototype demonstrating clinical-logic-to-code translation. It is not a validated diagnostic device and is not intended for real clinical decision-making without further validation and regulatory review.



---

