"""
MediMap Neuro — SNOOP10 Headache Triage Scoring Engine
--------------------------------------------------------
Rules-based classification of headache presentations into
Red / Yellow / Green urgency tiers, based on the SNOOP10
red-flag framework used in clinical headache triage.

This is a portfolio / decision-support PROTOTYPE.
It is NOT a diagnostic device and is not intended for real
clinical use without validation and regulatory review.


"""

from dataclasses import dataclass, field
from typing import List, Dict


# ---------------------------------------------------------
# 1. SNOOP10 CRITERIA DEFINITIONS
# ---------------------------------------------------------
# Each criterion maps to a red-flag category. Weight reflects
# how strongly that flag alone should push toward urgent review.

SNOOP10_CRITERIA: Dict[str, Dict] = {
    "systemic_symptoms":   {"label": "Systemic symptoms (fever, weight loss, malignancy history)", "weight": 3},
    "neurologic_signs":    {"label": "Neurologic signs/symptoms (focal deficit, confusion, seizure)", "weight": 4},
    "onset_thunderclap":   {"label": "Onset - thunderclap (sudden, severe, peak <1 min)", "weight": 4},
    "older_age":           {"label": "Older age (new headache onset >50 years)", "weight": 2},
    "pattern_change":      {"label": "Pattern change (progressive, or change from baseline pattern)", "weight": 2},
    "positional":          {"label": "Positional (worse lying down / on standing)", "weight": 2},
    "precipitated":        {"label": "Precipitated by valsalva/cough/exertion/sex", "weight": 2},
    "papilledema":         {"label": "Papilledema (on exam) or visual disturbance", "weight": 3},
    "progressive":         {"label": "Progressive worsening over days/weeks", "weight": 2},
    "pregnancy":           {"label": "Pregnancy or postpartum state", "weight": 2},
}


# ---------------------------------------------------------
# 2. PATIENT CASE STRUCTURE
# ---------------------------------------------------------

@dataclass
class PatientCase:
    case_id: str
    age: int
    flags: List[str] = field(default_factory=list)  # keys from SNOOP10_CRITERIA present
    notes: str = ""


# ---------------------------------------------------------
# 3. SCORING LOGIC
# ---------------------------------------------------------

def score_case(case: PatientCase) -> Dict:
    """
    Scores a patient case against SNOOP10 criteria and returns
    a classification tier + structured summary note.
    """
    triggered = [SNOOP10_CRITERIA[f] for f in case.flags if f in SNOOP10_CRITERIA]
    total_score = sum(c["weight"] for c in triggered)
    max_single_weight = max((c["weight"] for c in triggered), default=0)

    # Tier logic:
    # RED    -> any single high-severity flag (weight >=4) OR total score >= 6
    # YELLOW -> total score between 2 and 5
    # GREEN  -> no flags or total score < 2
    if max_single_weight >= 4 or total_score >= 6:
        tier = "RED"
    elif total_score >= 2:
        tier = "YELLOW"
    else:
        tier = "GREEN"

    summary_note = generate_summary_note(case, triggered, tier, total_score)

    return {
        "case_id": case.case_id,
        "tier": tier,
        "score": total_score,
        "triggered_flags": [c["label"] for c in triggered],
        "summary_note": summary_note,
    }


def generate_summary_note(case: PatientCase, triggered: List[Dict], tier: str, score: int) -> str:
    """
    Generates a clean, chart-ready summary note.
    """
    flag_lines = "\n".join(f"  - {c['label']}" for c in triggered) if triggered else "  - None identified"

    tier_guidance = {
        "RED": "Recommend urgent evaluation / imaging per institutional protocol.",
        "YELLOW": "Recommend close clinical follow-up and further history/exam.",
        "GREEN": "Consistent with primary headache pattern; routine management.",
    }[tier]

    return (
        f"--- MediMap Neuro Triage Summary ---\n"
        f"Case ID: {case.case_id}\n"
        f"Age: {case.age}\n"
        f"SNOOP10 Score: {score}\n"
        f"Urgency Tier: {tier}\n"
        f"Flags identified:\n{flag_lines}\n"
        f"Guidance: {tier_guidance}\n"
        f"-------------------------------------"
    )


# ---------------------------------------------------------
# 4. SAMPLE CASES (for demo / validation)
# ---------------------------------------------------------

SAMPLE_CASES = [
    PatientCase(
        case_id="CASE-001",
        age=34,
        flags=["onset_thunderclap", "neurologic_signs"],
        notes="Sudden severe headache, peaked in under a minute, right-sided weakness.",
    ),
    PatientCase(
        case_id="CASE-002",
        age=27,
        flags=[],
        notes="Recurrent headache, consistent pattern for 3 years, no new symptoms.",
    ),
    PatientCase(
        case_id="CASE-003",
        age=58,
        flags=["older_age", "pattern_change", "progressive"],
        notes="New headache onset at 58, gradually worsening over 3 weeks.",
    ),
    PatientCase(
        case_id="CASE-004",
        age=29,
        flags=["pregnancy", "positional"],
        notes="Pregnant, headache worse when lying flat.",
    ),
    PatientCase(
        case_id="CASE-005",
        age=45,
        flags=["papilledema", "systemic_symptoms"],
        notes="Blurred vision on exam, low-grade fever for 5 days.",
    ),
]


# ---------------------------------------------------------
# 5. RUN DEMO
# ---------------------------------------------------------

def run_demo():
    print("Running MediMap Neuro SNOOP10 Triage Engine on sample cases...\n")
    results = [score_case(c) for c in SAMPLE_CASES]
    for r in results:
        print(r["summary_note"])
        print()

    tier_counts = {"RED": 0, "YELLOW": 0, "GREEN": 0}
    for r in results:
        tier_counts[r["tier"]] += 1

    print("=== Summary Across Sample Cases ===")
    print(f"Total cases: {len(results)}")
    for tier, count in tier_counts.items():
        print(f"{tier}: {count}")


if __name__ == "__main__":
    run_demo()

