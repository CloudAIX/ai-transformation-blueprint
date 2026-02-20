"""Department assessment templates for Australian healthcare organisations."""

from .models import DepartmentAssessment


def create_department_templates() -> list[DepartmentAssessment]:
    """Return 5 department assessment templates for healthcare."""
    return [
        DepartmentAssessment(
            department="Clinical",
            current_maturity=0,
            target_maturity=0,
            gap=0,
            pain_points=[
                "Excessive time spent on clinical documentation and progress notes",
                "Manual care plan creation and updates consuming nursing hours",
                "Handover communication gaps between shifts leading to missed information",
                "Difficulty tracking and meeting mandated care minutes per resident",
                "Delayed incident reporting and SIRS notification processes",
                "Limited access to real-time clinical decision support at point of care",
            ],
            ai_interventions=[
                {"name": "AI Medical Scribe", "description": "Real-time clinical documentation from voice during consultations and care delivery", "effort": "medium", "impact": "high", "timeline": "2-4 months"},
                {"name": "Clinical Decision Support", "description": "AI-powered alerts for medication interactions, deterioration risk, and care gaps", "effort": "high", "impact": "high", "timeline": "6-12 months"},
                {"name": "Automated Care Plans", "description": "AI-generated care plan drafts from assessment data with clinician review", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "Smart Handover", "description": "AI-summarised shift handover reports highlighting key changes and priorities", "effort": "low", "impact": "medium", "timeline": "1-3 months"},
                {"name": "Predictive Deterioration", "description": "Early warning system using vital signs and observation patterns", "effort": "high", "impact": "high", "timeline": "6-12 months"},
            ],
            quick_wins=[
                "Deploy AI scribe for clinical documentation (immediate time savings)",
                "Implement AI-assisted handover summaries between shifts",
                "Use AI to draft initial care plans from assessment data",
            ],
        ),
        DepartmentAssessment(
            department="Administrative",
            current_maturity=0,
            target_maturity=0,
            gap=0,
            pain_points=[
                "High volume of phone calls for appointments, enquiries, and follow-ups",
                "Manual patient intake and registration processes",
                "Paper-based or fragmented document management",
                "Time-consuming compliance reporting and audit preparation",
                "Scheduling inefficiencies and appointment no-shows",
                "Manual data entry across multiple disconnected systems",
            ],
            ai_interventions=[
                {"name": "AI Receptionist/Chatbot", "description": "24/7 AI-powered patient enquiries, appointment booking, and triage", "effort": "medium", "impact": "high", "timeline": "2-4 months"},
                {"name": "Automated Patient Intake", "description": "Digital intake forms with AI extraction and system population", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "Intelligent Document Processing", "description": "AI classification, extraction, and routing of incoming documents", "effort": "medium", "impact": "medium", "timeline": "3-6 months"},
                {"name": "Automated Reporting", "description": "AI-generated compliance reports from operational data", "effort": "low", "impact": "high", "timeline": "1-3 months"},
                {"name": "Smart Scheduling", "description": "AI-optimised appointment scheduling with no-show prediction", "effort": "medium", "impact": "medium", "timeline": "3-6 months"},
            ],
            quick_wins=[
                "Deploy AI chatbot for after-hours enquiries and appointment booking",
                "Implement automated compliance report generation",
                "Use AI for document classification and routing",
            ],
        ),
        DepartmentAssessment(
            department="Finance/Billing",
            current_maturity=0,
            target_maturity=0,
            gap=0,
            pain_points=[
                "Manual billing code selection leading to errors and missed revenue",
                "High claim rejection rates from incorrect coding",
                "Slow accounts receivable processes and payment reconciliation",
                "Difficulty optimising funding models (AN-ACC, MBS, NDIS)",
                "Manual invoice processing and accounts payable",
                "Limited financial forecasting and cash flow visibility",
            ],
            ai_interventions=[
                {"name": "AI-Assisted Coding", "description": "Automated billing code suggestion from clinical documentation", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "Claims Validation", "description": "AI pre-submission validation to reduce rejection rates", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "Automated Invoice Processing", "description": "AI extraction and matching for accounts payable", "effort": "low", "impact": "medium", "timeline": "2-4 months"},
                {"name": "Revenue Optimisation", "description": "AI analysis of missed billing opportunities and funding maximisation", "effort": "medium", "impact": "high", "timeline": "4-8 months"},
                {"name": "Financial Forecasting", "description": "AI-powered cash flow and revenue forecasting", "effort": "high", "impact": "medium", "timeline": "6-12 months"},
            ],
            quick_wins=[
                "Deploy AI coding assistant for AN-ACC documentation",
                "Implement automated invoice processing for accounts payable",
                "Use AI to audit past claims for missed revenue",
            ],
        ),
        DepartmentAssessment(
            department="HR/Workforce",
            current_maturity=0,
            target_maturity=0,
            gap=0,
            pain_points=[
                "Complex rostering to meet care minute requirements",
                "High staff turnover and recruitment costs",
                "Manual onboarding and credentialing processes",
                "Difficulty tracking mandatory training compliance",
                "Workforce planning challenges with variable demand",
                "Manual timesheet processing and payroll reconciliation",
            ],
            ai_interventions=[
                {"name": "AI-Optimised Rostering", "description": "Automated roster generation meeting care minute targets, staff preferences, and budget constraints", "effort": "high", "impact": "high", "timeline": "4-8 months"},
                {"name": "Predictive Workforce Planning", "description": "AI-driven demand forecasting and staff requirement modelling", "effort": "medium", "impact": "high", "timeline": "6-9 months"},
                {"name": "Automated Onboarding", "description": "AI-guided onboarding workflows with document verification and training scheduling", "effort": "medium", "impact": "medium", "timeline": "3-6 months"},
                {"name": "Training Compliance Tracker", "description": "AI monitoring of mandatory training, certifications, and CPD requirements", "effort": "low", "impact": "medium", "timeline": "1-3 months"},
                {"name": "AI Recruitment Assistant", "description": "AI-powered candidate screening, interview scheduling, and onboarding", "effort": "medium", "impact": "medium", "timeline": "3-6 months"},
            ],
            quick_wins=[
                "Automate training compliance monitoring and reminders",
                "Implement AI-assisted timesheet processing",
                "Deploy AI screening for recruitment applications",
            ],
        ),
        DepartmentAssessment(
            department="IT/Data",
            current_maturity=0,
            target_maturity=0,
            gap=0,
            pain_points=[
                "Data silos across clinical, admin, and financial systems",
                "Limited data analytics capability",
                "Manual system administration and monitoring",
                "Security and compliance monitoring is reactive",
                "Insufficient data infrastructure for AI workloads",
                "Shadow IT and unmanaged AI tool proliferation",
            ],
            ai_interventions=[
                {"name": "Data Integration Platform", "description": "Unified data layer connecting clinical, admin, and financial systems for AI consumption", "effort": "high", "impact": "high", "timeline": "6-12 months"},
                {"name": "AI-Powered Security", "description": "Automated threat detection, anomaly monitoring, and compliance checking", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "AI Governance Platform", "description": "Centralised AI tool management, usage monitoring, and policy enforcement", "effort": "medium", "impact": "high", "timeline": "3-6 months"},
                {"name": "Automated IT Operations", "description": "AI-assisted helpdesk, system monitoring, and incident response", "effort": "medium", "impact": "medium", "timeline": "3-6 months"},
                {"name": "Business Intelligence", "description": "AI-powered dashboards and insights across all operational data", "effort": "medium", "impact": "high", "timeline": "4-8 months"},
            ],
            quick_wins=[
                "Deploy AI-powered security monitoring",
                "Implement AI governance policy and approved tools list",
                "Set up automated system health monitoring",
            ],
        ),
    ]

DEPARTMENT_NAMES = ["Clinical", "Administrative", "Finance/Billing", "HR/Workforce", "IT/Data"]
