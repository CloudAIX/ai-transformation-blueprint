"""Role transformation mappings for AI-native healthcare organisations."""

from .models import RoleTransformation


def create_role_transformations() -> list[RoleTransformation]:
    """Return 7 role transformation templates for healthcare."""
    return [
        RoleTransformation(
            current_role="Medical Receptionist",
            future_role="Patient Experience Coordinator",
            department="Administrative",
            current_skills=["Phone handling", "Appointment booking", "Data entry", "Filing", "Patient greeting"],
            required_skills=["AI tool management", "Digital patient experience", "Chatbot oversight", "Data quality monitoring", "Complex enquiry resolution", "Process improvement"],
            skills_delta=["AI tool management", "Digital patient experience", "Chatbot oversight", "Data quality monitoring", "Process improvement"],
            training_plan=[
                {"skill": "AI tool management", "method": "Vendor training + hands-on", "duration_hours": 16, "cost": 500},
                {"skill": "Digital patient experience", "method": "Online course + mentoring", "duration_hours": 24, "cost": 800},
                {"skill": "Chatbot oversight", "method": "Vendor training", "duration_hours": 8, "cost": 300},
                {"skill": "Data quality monitoring", "method": "Internal training", "duration_hours": 12, "cost": 200},
                {"skill": "Process improvement", "method": "Short course", "duration_hours": 16, "cost": 600},
            ],
            timeline_months=4,
            risk_level="low",
        ),
        RoleTransformation(
            current_role="Clinical Coder",
            future_role="AI-Augmented Coding Specialist",
            department="Finance/Billing",
            current_skills=["ICD-10 coding", "Clinical documentation review", "Billing system operation", "Audit preparation"],
            required_skills=["AI coding tool operation", "AI output validation", "Exception handling", "Coding accuracy auditing", "AI training data curation", "Regulatory compliance monitoring"],
            skills_delta=["AI coding tool operation", "AI output validation", "AI training data curation", "Regulatory compliance monitoring"],
            training_plan=[
                {"skill": "AI coding tool operation", "method": "Vendor certification", "duration_hours": 40, "cost": 2000},
                {"skill": "AI output validation", "method": "Workshop + practice", "duration_hours": 24, "cost": 1000},
                {"skill": "AI training data curation", "method": "Specialist training", "duration_hours": 16, "cost": 1500},
                {"skill": "Regulatory compliance monitoring", "method": "Online course", "duration_hours": 12, "cost": 500},
            ],
            timeline_months=6,
            risk_level="medium",
        ),
        RoleTransformation(
            current_role="Registered Nurse",
            future_role="AI-Enhanced Clinical Nurse",
            department="Clinical",
            current_skills=["Patient assessment", "Medication administration", "Care plan execution", "Clinical documentation", "Handover communication"],
            required_skills=["AI scribe operation", "Clinical decision support interpretation", "AI alert triage", "Digital care plan management", "AI-assisted patient monitoring", "Technology-enabled care delivery"],
            skills_delta=["AI scribe operation", "Clinical decision support interpretation", "AI alert triage", "AI-assisted patient monitoring"],
            training_plan=[
                {"skill": "AI scribe operation", "method": "Vendor training + supervised practice", "duration_hours": 12, "cost": 400},
                {"skill": "Clinical decision support interpretation", "method": "Clinical workshop", "duration_hours": 16, "cost": 800},
                {"skill": "AI alert triage", "method": "Simulation training", "duration_hours": 8, "cost": 500},
                {"skill": "AI-assisted patient monitoring", "method": "Vendor training", "duration_hours": 8, "cost": 300},
            ],
            timeline_months=3,
            risk_level="medium",
        ),
        RoleTransformation(
            current_role="Rostering Officer",
            future_role="Workforce Analytics Coordinator",
            department="HR/Workforce",
            current_skills=["Manual roster creation", "Award interpretation", "Staff availability tracking", "Overtime management"],
            required_skills=["AI roster optimisation", "Workforce analytics", "Demand forecasting interpretation", "Care minute compliance monitoring", "Staff wellbeing metrics", "Continuous improvement"],
            skills_delta=["AI roster optimisation", "Workforce analytics", "Demand forecasting interpretation", "Care minute compliance monitoring", "Staff wellbeing metrics"],
            training_plan=[
                {"skill": "AI roster optimisation", "method": "Vendor training", "duration_hours": 24, "cost": 1200},
                {"skill": "Workforce analytics", "method": "Online course + mentoring", "duration_hours": 32, "cost": 1500},
                {"skill": "Demand forecasting interpretation", "method": "Workshop", "duration_hours": 8, "cost": 400},
                {"skill": "Care minute compliance monitoring", "method": "Internal training", "duration_hours": 8, "cost": 200},
                {"skill": "Staff wellbeing metrics", "method": "Short course", "duration_hours": 8, "cost": 300},
            ],
            timeline_months=6,
            risk_level="medium",
        ),
        RoleTransformation(
            current_role="Compliance Officer",
            future_role="AI Governance & Compliance Lead",
            department="Administrative",
            current_skills=["Regulatory monitoring", "Audit preparation", "Policy management", "Incident investigation", "Quality standards"],
            required_skills=["AI governance frameworks", "AI risk assessment", "Automated compliance monitoring", "AI ethics oversight", "Regulatory technology management", "AI audit methodology"],
            skills_delta=["AI governance frameworks", "AI risk assessment", "Automated compliance monitoring", "AI ethics oversight", "AI audit methodology"],
            training_plan=[
                {"skill": "AI governance frameworks", "method": "Specialist course (DISR/ISO)", "duration_hours": 24, "cost": 2000},
                {"skill": "AI risk assessment", "method": "Workshop + certification", "duration_hours": 32, "cost": 2500},
                {"skill": "Automated compliance monitoring", "method": "Vendor training", "duration_hours": 16, "cost": 800},
                {"skill": "AI ethics oversight", "method": "University short course", "duration_hours": 24, "cost": 1800},
                {"skill": "AI audit methodology", "method": "Professional development", "duration_hours": 16, "cost": 1200},
            ],
            timeline_months=9,
            risk_level="high",
        ),
        RoleTransformation(
            current_role="IT Support Technician",
            future_role="AI Systems Administrator",
            department="IT/Data",
            current_skills=["Helpdesk support", "System administration", "Network management", "Software installation", "User training"],
            required_skills=["AI platform administration", "AI model monitoring", "Data pipeline management", "AI security", "Integration management", "AI vendor management"],
            skills_delta=["AI platform administration", "AI model monitoring", "Data pipeline management", "AI security", "AI vendor management"],
            training_plan=[
                {"skill": "AI platform administration", "method": "Cloud vendor certification (AWS/Azure AI)", "duration_hours": 40, "cost": 3000},
                {"skill": "AI model monitoring", "method": "Online course + hands-on", "duration_hours": 24, "cost": 1000},
                {"skill": "Data pipeline management", "method": "Specialist training", "duration_hours": 32, "cost": 2000},
                {"skill": "AI security", "method": "Security certification", "duration_hours": 24, "cost": 1800},
                {"skill": "AI vendor management", "method": "Workshop", "duration_hours": 8, "cost": 400},
            ],
            timeline_months=9,
            risk_level="high",
        ),
        RoleTransformation(
            current_role="Care Manager",
            future_role="AI-Enabled Care Coordinator",
            department="Clinical",
            current_skills=["Care coordination", "Family communication", "Multidisciplinary team management", "Care planning", "Quality oversight"],
            required_skills=["AI care insights interpretation", "Digital family engagement", "AI-enhanced MDT coordination", "Predictive care planning", "AI quality metrics", "Technology change management"],
            skills_delta=["AI care insights interpretation", "Digital family engagement", "AI-enhanced MDT coordination", "Predictive care planning", "AI quality metrics"],
            training_plan=[
                {"skill": "AI care insights interpretation", "method": "Clinical workshop", "duration_hours": 16, "cost": 800},
                {"skill": "Digital family engagement", "method": "Vendor training", "duration_hours": 8, "cost": 300},
                {"skill": "AI-enhanced MDT coordination", "method": "Simulation + practice", "duration_hours": 12, "cost": 600},
                {"skill": "Predictive care planning", "method": "Specialist workshop", "duration_hours": 16, "cost": 1000},
                {"skill": "AI quality metrics", "method": "Online course", "duration_hours": 8, "cost": 400},
            ],
            timeline_months=6,
            risk_level="medium",
        ),
    ]

ROLE_TRANSFORMATION_COUNT = 7
