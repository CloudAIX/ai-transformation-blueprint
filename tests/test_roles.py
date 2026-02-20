"""Tests for role transformation templates."""

from blueprint.roles import create_role_transformations, ROLE_TRANSFORMATION_COUNT
from blueprint.models import RoleTransformation


def test_role_count():
    """7 role transformations returned."""
    roles = create_role_transformations()
    assert len(roles) == ROLE_TRANSFORMATION_COUNT
    assert ROLE_TRANSFORMATION_COUNT == 7


def test_role_type():
    """All entries are RoleTransformation instances."""
    for role in create_role_transformations():
        assert isinstance(role, RoleTransformation)


def test_role_fields():
    """Each role has current_role, future_role, department, and skills."""
    for role in create_role_transformations():
        assert role.current_role
        assert role.future_role
        assert role.department
        assert len(role.current_skills) > 0
        assert len(role.required_skills) > 0


def test_skills_delta_computed():
    """skills_delta is non-empty (skills to acquire)."""
    for role in create_role_transformations():
        assert len(role.skills_delta) > 0, f"{role.current_role} has empty skills_delta"


def test_training_plan_structure():
    """Each role has a training plan with skill, method, duration_hours, cost."""
    for role in create_role_transformations():
        assert len(role.training_plan) > 0
        for item in role.training_plan:
            assert "skill" in item
            assert "method" in item
            assert "duration_hours" in item
            assert "cost" in item
            assert item["duration_hours"] > 0
            assert item["cost"] > 0


def test_training_cost_positive():
    """Total training cost per role is positive."""
    for role in create_role_transformations():
        total = sum(item["cost"] for item in role.training_plan)
        assert total > 0, f"{role.current_role} has zero training cost"


def test_role_risk_levels():
    """All risk levels are valid."""
    valid = {"low", "medium", "high"}
    for role in create_role_transformations():
        assert role.risk_level in valid, f"{role.current_role} has invalid risk_level: {role.risk_level}"


def test_timeline_months():
    """All timelines are positive and reasonable (1-18 months)."""
    for role in create_role_transformations():
        assert 1 <= role.timeline_months <= 18
