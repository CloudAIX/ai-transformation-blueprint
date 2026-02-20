"""Tests for department assessment templates."""

from blueprint.departments import create_department_templates, DEPARTMENT_NAMES
from blueprint.models import DepartmentAssessment


def test_department_count():
    """5 departments returned."""
    departments = create_department_templates()
    assert len(departments) == 5


def test_department_names_match():
    """Department names match expected list."""
    departments = create_department_templates()
    names = [d.department for d in departments]
    assert names == DEPARTMENT_NAMES


def test_department_type():
    """All departments are DepartmentAssessment instances."""
    for dept in create_department_templates():
        assert isinstance(dept, DepartmentAssessment)


def test_department_pain_points():
    """Each department has at least 3 pain points."""
    for dept in create_department_templates():
        assert len(dept.pain_points) >= 3, f"{dept.department} has only {len(dept.pain_points)} pain points"


def test_department_ai_interventions():
    """Each department has at least 3 AI interventions with required keys."""
    for dept in create_department_templates():
        assert len(dept.ai_interventions) >= 3
        for ai in dept.ai_interventions:
            assert "name" in ai
            assert "description" in ai
            assert "effort" in ai
            assert "impact" in ai
            assert "timeline" in ai


def test_department_quick_wins():
    """Each department has at least 2 quick wins."""
    for dept in create_department_templates():
        assert len(dept.quick_wins) >= 2, f"{dept.department} has only {len(dept.quick_wins)} quick wins"


def test_department_defaults():
    """Default maturity values are 0 (to be filled by user)."""
    for dept in create_department_templates():
        assert dept.current_maturity == 0
        assert dept.target_maturity == 0
        assert dept.gap == 0
