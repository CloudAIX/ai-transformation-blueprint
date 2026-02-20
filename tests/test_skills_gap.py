"""Tests for skills gap analysis engine."""

from blueprint.skills_gap import calculate_skills_gap, summarise_by_department, summarise_by_skill
from blueprint.roles import create_role_transformations
from blueprint.models import SkillsGapAnalysis


def test_calculate_skills_gap_type():
    """Returns SkillsGapAnalysis instance."""
    roles = create_role_transformations()
    result = calculate_skills_gap(roles)
    assert isinstance(result, SkillsGapAnalysis)


def test_training_hours_positive():
    """Total training hours > 0."""
    result = calculate_skills_gap(create_role_transformations())
    assert result.total_training_hours > 0


def test_training_cost_positive():
    """Total training cost > 0."""
    result = calculate_skills_gap(create_role_transformations())
    assert result.total_training_cost > 0


def test_critical_gaps_identified():
    """Critical gaps are identified (high risk roles)."""
    result = calculate_skills_gap(create_role_transformations())
    assert len(result.critical_gaps) > 0


def test_critical_gaps_sorted_by_urgency():
    """Critical gaps sorted: high urgency first."""
    result = calculate_skills_gap(create_role_transformations())
    urgency_order = {"high": 0, "medium": 1, "low": 2}
    urgencies = [urgency_order.get(g["urgency"], 3) for g in result.critical_gaps]
    assert urgencies == sorted(urgencies)


def test_training_timeline():
    """Timeline matches longest role transformation."""
    roles = create_role_transformations()
    result = calculate_skills_gap(roles)
    max_months = max(r.timeline_months for r in roles)
    assert result.training_timeline_months == max_months


def test_summarise_by_department():
    """Department summary has expected structure."""
    result = calculate_skills_gap(create_role_transformations())
    dept_summary = summarise_by_department(result)
    assert len(dept_summary) > 0
    for dept, data in dept_summary.items():
        assert "roles_affected" in data
        assert "skills_to_acquire" in data
        assert "training_hours" in data
        assert "training_cost" in data
        assert data["roles_affected"] > 0


def test_summarise_by_skill():
    """Skill summary has expected structure."""
    result = calculate_skills_gap(create_role_transformations())
    skill_summary = summarise_by_skill(result)
    assert len(skill_summary) > 0
    for skill, data in skill_summary.items():
        assert "roles_needing" in data
        assert "total_hours" in data
        assert "total_cost" in data
        assert "methods" in data
        assert isinstance(data["methods"], list)


def test_empty_roles():
    """Empty role list returns zeroed analysis."""
    result = calculate_skills_gap([])
    assert result.total_training_hours == 0
    assert result.total_training_cost == 0
    assert len(result.critical_gaps) == 0
