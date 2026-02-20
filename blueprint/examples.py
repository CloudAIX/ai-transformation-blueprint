"""Example blueprints and healthcare business model templates."""

from .models import TransformationBlueprint, DepartmentAssessment
from .departments import create_department_templates
from .roles import create_role_transformations
from .workflows import create_workflow_templates
from .skills_gap import calculate_skills_gap
from .change_mgmt import create_default_change_plan
from .maturity import classify_maturity


BUSINESS_TEMPLATES = {
    "aged_care": {
        "name": "Aged Care Facility",
        "description": "Residential aged care (AN-ACC, care minutes, Quality Standards)",
        "typical_employees": 40,
        "focus_areas": ["Care minutes tracking", "SIRS compliance", "Quality Standards documentation", "Medication management", "Family communication"],
    },
    "gp_clinic": {
        "name": "GP / Medical Clinic",
        "description": "General practice clinic (MBS billing, patient throughput)",
        "typical_employees": 15,
        "focus_areas": ["Patient intake", "Clinical documentation", "MBS billing optimisation", "Referral management", "Recall/reminder systems"],
    },
    "private_hospital": {
        "name": "Private Hospital",
        "description": "Private hospital (surgical scheduling, DRG coding)",
        "typical_employees": 200,
        "focus_areas": ["Surgical scheduling", "DRG coding", "Bed management", "Discharge planning", "Theatre utilisation"],
    },
    "community_health": {
        "name": "Community Health",
        "description": "Community health service (NDIS, chronic disease management)",
        "typical_employees": 50,
        "focus_areas": ["NDIS plan management", "Chronic disease programs", "Outreach coordination", "Group program scheduling", "Outcome reporting"],
    },
    "telehealth": {
        "name": "Telehealth Provider",
        "description": "Telehealth/virtual care service (remote monitoring, virtual consults)",
        "typical_employees": 25,
        "focus_areas": ["Virtual consultation workflow", "Remote patient monitoring", "Digital triage", "Patient engagement", "Clinical data integration"],
    },
}


def create_example_blueprint() -> TransformationBlueprint:
    """Create a fully populated example blueprint for Maplewood Aged Care."""
    # Department assessments with realistic maturity scores
    departments = create_department_templates()
    # Set example current and target maturity levels
    maturity_assignments = [
        (1, 3),  # Clinical: Spicy Autocomplete -> AI-Integrated
        (1, 3),  # Administrative: Spicy Autocomplete -> AI-Integrated
        (0, 2),  # Finance/Billing: No AI -> AI-Assisted
        (0, 2),  # HR/Workforce: No AI -> AI-Assisted
        (1, 3),  # IT/Data: Spicy Autocomplete -> AI-Integrated
    ]
    for dept, (current, target) in zip(departments, maturity_assignments):
        dept.current_maturity = current
        dept.target_maturity = target
        dept.gap = target - current

    # Role transformations
    roles = create_role_transformations()

    # Workflow redesigns
    workflows = create_workflow_templates()

    # Skills gap analysis
    skills_gap = calculate_skills_gap(roles)

    # Change management plan
    change_plan = create_default_change_plan("Maplewood Residential Aged Care")

    # Calculate overall maturity
    current_avg = sum(d.current_maturity for d in departments) / len(departments)
    target_avg = sum(d.target_maturity for d in departments) / len(departments)

    # Calculate financials
    total_impl_cost = sum(w.implementation_cost for w in workflows) + skills_gap.total_training_cost
    # Estimate annual savings from workflow improvements (hours saved * avg hourly rate $45 AUD)
    total_annual_savings = sum(w.annual_hours_saved for w in workflows) * 45
    roi_multiplier = round(total_annual_savings / total_impl_cost, 2) if total_impl_cost > 0 else 0
    payback_months = round(total_impl_cost / total_annual_savings * 12, 1) if total_annual_savings > 0 else 0

    return TransformationBlueprint(
        organisation_name="Maplewood Residential Aged Care",
        industry="aged_care",
        employee_count=40,
        assessment_date="2025-01-15",
        assessed_by="GVRN-AI",
        overall_current_maturity=round(current_avg, 1),
        overall_target_maturity=round(target_avg, 1),
        department_assessments=departments,
        role_transformations=roles,
        workflow_redesigns=workflows,
        skills_gap=skills_gap,
        change_management=change_plan,
        total_implementation_cost=total_impl_cost,
        total_annual_savings=total_annual_savings,
        roi_multiplier=roi_multiplier,
        payback_months=payback_months,
        implementation_phases=[
            {"phase": "Foundation", "months": "1-3", "focus_areas": ["Governance", "Shadow AI assessment", "Tool selection"], "investment": round(total_impl_cost * 0.2)},
            {"phase": "Pilot", "months": "4-6", "focus_areas": ["Clinical documentation", "Admin automation", "Staff training"], "investment": round(total_impl_cost * 0.3)},
            {"phase": "Scale", "months": "7-9", "focus_areas": ["Full rollout", "Workflow optimisation", "Role transitions"], "investment": round(total_impl_cost * 0.3)},
            {"phase": "Optimise", "months": "10-12", "focus_areas": ["ROI measurement", "Advanced AI", "Continuous improvement"], "investment": round(total_impl_cost * 0.2)},
        ],
    )
