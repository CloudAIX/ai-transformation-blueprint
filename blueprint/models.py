"""Data models for the AI Transformation Blueprint."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MaturityLevel:
    level: int              # 0-5
    name: str               # "No AI", "Spicy Autocomplete", etc.
    description: str
    healthcare_example: str
    indicators: list[str] = field(default_factory=list)


@dataclass
class DepartmentAssessment:
    department: str         # "Clinical", "Administrative", "Finance/Billing", "HR/Workforce", "IT/Data"
    current_maturity: int   # 0-5
    target_maturity: int    # 0-5
    gap: int                # computed: target - current
    ai_tools_current: list[str] = field(default_factory=list)
    ai_interventions: list[dict] = field(default_factory=list)
    pain_points: list[str] = field(default_factory=list)
    quick_wins: list[str] = field(default_factory=list)


@dataclass
class RoleTransformation:
    current_role: str       # e.g. "Medical Receptionist"
    future_role: str        # e.g. "Patient Experience Coordinator"
    department: str
    current_skills: list[str] = field(default_factory=list)
    required_skills: list[str] = field(default_factory=list)
    skills_delta: list[str] = field(default_factory=list)
    training_plan: list[dict] = field(default_factory=list)
    timeline_months: int = 6
    risk_level: str = "medium"


@dataclass
class WorkflowRedesign:
    workflow_name: str      # e.g. "Patient Intake"
    department: str
    current_steps: list[dict] = field(default_factory=list)
    future_steps: list[dict] = field(default_factory=list)
    time_savings_percent: float = 0.0
    annual_hours_saved: float = 0.0
    implementation_cost: float = 0.0
    tools_needed: list[str] = field(default_factory=list)


@dataclass
class SkillsGapAnalysis:
    role_transformations: list[RoleTransformation] = field(default_factory=list)
    total_training_hours: float = 0.0
    total_training_cost: float = 0.0
    critical_gaps: list[dict] = field(default_factory=list)
    training_timeline_months: int = 12


@dataclass
class ChangeManagementPlan:
    stakeholder_map: list[dict] = field(default_factory=list)
    communication_plan: list[dict] = field(default_factory=list)
    resistance_mitigation: list[dict] = field(default_factory=list)
    success_metrics: list[dict] = field(default_factory=list)
    phases: list[dict] = field(default_factory=list)


@dataclass
class TransformationBlueprint:
    """Top-level data model for an AI Transformation Blueprint."""
    organisation_name: str
    industry: str
    employee_count: int
    assessment_date: str = ""
    assessed_by: str = ""

    # Maturity
    overall_current_maturity: float = 0.0
    overall_target_maturity: float = 0.0

    # Components
    department_assessments: list[DepartmentAssessment] = field(default_factory=list)
    role_transformations: list[RoleTransformation] = field(default_factory=list)
    workflow_redesigns: list[WorkflowRedesign] = field(default_factory=list)
    skills_gap: Optional[SkillsGapAnalysis] = None
    change_management: Optional[ChangeManagementPlan] = None

    # Financials
    total_implementation_cost: float = 0.0
    total_annual_savings: float = 0.0
    roi_multiplier: float = 0.0
    payback_months: float = 0.0

    # Roadmap
    implementation_phases: list[dict] = field(default_factory=list)

    schema_version: str = "1.0"
