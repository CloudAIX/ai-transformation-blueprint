"""Skills gap analysis engine for AI transformation planning."""

from .models import SkillsGapAnalysis, RoleTransformation


def calculate_skills_gap(role_transformations: list[RoleTransformation]) -> SkillsGapAnalysis:
    """Analyse skills gaps across all role transformations and compute totals."""
    total_hours = 0.0
    total_cost = 0.0
    critical_gaps = []
    max_timeline = 0

    for rt in role_transformations:
        for item in rt.training_plan:
            hours = item.get("duration_hours", 0)
            cost = item.get("cost", 0)
            total_hours += hours
            total_cost += cost

        max_timeline = max(max_timeline, rt.timeline_months)

        # Identify critical gaps (high risk roles or many skills to acquire)
        if rt.risk_level == "high" or len(rt.skills_delta) >= 5:
            for skill in rt.skills_delta:
                urgency = "high" if rt.risk_level == "high" else "medium"
                critical_gaps.append({
                    "role": rt.current_role,
                    "future_role": rt.future_role,
                    "skill": skill,
                    "urgency": urgency,
                    "department": rt.department,
                })

    # Sort critical gaps: high urgency first
    urgency_order = {"high": 0, "medium": 1, "low": 2}
    critical_gaps.sort(key=lambda g: urgency_order.get(g["urgency"], 3))

    return SkillsGapAnalysis(
        role_transformations=role_transformations,
        total_training_hours=round(total_hours, 1),
        total_training_cost=round(total_cost, 2),
        critical_gaps=critical_gaps,
        training_timeline_months=max_timeline,
    )


def summarise_by_department(analysis: SkillsGapAnalysis) -> dict:
    """Group skills gap data by department."""
    dept_summary = {}
    for rt in analysis.role_transformations:
        dept = rt.department
        if dept not in dept_summary:
            dept_summary[dept] = {
                "roles_affected": 0,
                "skills_to_acquire": 0,
                "training_hours": 0,
                "training_cost": 0,
                "max_timeline_months": 0,
            }
        dept_summary[dept]["roles_affected"] += 1
        dept_summary[dept]["skills_to_acquire"] += len(rt.skills_delta)
        dept_summary[dept]["max_timeline_months"] = max(
            dept_summary[dept]["max_timeline_months"], rt.timeline_months
        )
        for item in rt.training_plan:
            dept_summary[dept]["training_hours"] += item.get("duration_hours", 0)
            dept_summary[dept]["training_cost"] += item.get("cost", 0)
    return dept_summary


def summarise_by_skill(analysis: SkillsGapAnalysis) -> dict:
    """Group skills gap data by skill across all roles."""
    skill_summary = {}
    for rt in analysis.role_transformations:
        for item in rt.training_plan:
            skill = item.get("skill", "Unknown")
            if skill not in skill_summary:
                skill_summary[skill] = {
                    "roles_needing": [],
                    "total_hours": 0,
                    "total_cost": 0,
                    "methods": set(),
                }
            skill_summary[skill]["roles_needing"].append(rt.current_role)
            skill_summary[skill]["total_hours"] += item.get("duration_hours", 0)
            skill_summary[skill]["total_cost"] += item.get("cost", 0)
            skill_summary[skill]["methods"].add(item.get("method", ""))

    # Convert sets to lists for serialization
    for s in skill_summary.values():
        s["methods"] = sorted(s["methods"])

    return skill_summary
