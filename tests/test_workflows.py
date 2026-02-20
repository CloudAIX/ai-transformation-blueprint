"""Tests for workflow redesign templates."""

from blueprint.workflows import create_workflow_templates, WORKFLOW_COUNT
from blueprint.models import WorkflowRedesign


def test_workflow_count():
    """10 workflows returned."""
    workflows = create_workflow_templates()
    assert len(workflows) == WORKFLOW_COUNT
    assert WORKFLOW_COUNT == 10


def test_workflow_type():
    """All entries are WorkflowRedesign instances."""
    for wf in create_workflow_templates():
        assert isinstance(wf, WorkflowRedesign)


def test_workflow_fields():
    """Each workflow has name, department, current steps, future steps."""
    for wf in create_workflow_templates():
        assert wf.workflow_name
        assert wf.department
        assert len(wf.current_steps) > 0
        assert len(wf.future_steps) > 0


def test_time_savings_positive():
    """Time savings percentage is between 1% and 100%."""
    for wf in create_workflow_templates():
        assert 1 <= wf.time_savings_percent <= 100, f"{wf.workflow_name}: {wf.time_savings_percent}%"


def test_annual_hours_saved():
    """Annual hours saved is positive for all workflows."""
    for wf in create_workflow_templates():
        assert wf.annual_hours_saved > 0, f"{wf.workflow_name}: {wf.annual_hours_saved}"


def test_implementation_cost():
    """Implementation cost is positive for all workflows."""
    for wf in create_workflow_templates():
        assert wf.implementation_cost > 0, f"{wf.workflow_name}: ${wf.implementation_cost}"


def test_tools_needed():
    """Each workflow lists tools needed."""
    for wf in create_workflow_templates():
        assert len(wf.tools_needed) > 0


def test_step_structure():
    """Current and future steps have required keys."""
    for wf in create_workflow_templates():
        for step in wf.current_steps:
            assert "step" in step
            assert "actor" in step
            assert "time_mins" in step
        for step in wf.future_steps:
            assert "step" in step
            assert "actor" in step
            assert "time_mins" in step
