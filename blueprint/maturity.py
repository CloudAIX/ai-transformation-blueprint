"""Dan Shapiro's AI Maturity Model -- adapted for Australian healthcare."""

from .models import MaturityLevel

MATURITY_LEVELS = [
    MaturityLevel(
        level=0,
        name="No AI",
        description="No AI usage in the organisation. All processes are manual or use traditional software only.",
        healthcare_example="Paper-based patient records, manual rostering in spreadsheets, phone-only appointment booking.",
        indicators=[
            "No staff using AI tools",
            "All documentation is manual",
            "No awareness of AI capabilities",
            "IT infrastructure doesn't support AI",
        ],
    ),
    MaturityLevel(
        level=1,
        name="Spicy Autocomplete",
        description="Individual staff members using AI tools ad-hoc for personal productivity. No organisational strategy or governance.",
        healthcare_example="Nurses using ChatGPT to draft care plans, admin staff using Copilot for emails, no approved tools list.",
        indicators=[
            "Shadow AI usage detected",
            "No AI policy or governance",
            "Individual productivity gains only",
            "No data integration with AI tools",
            "Potential compliance risks from uncontrolled usage",
        ],
    ),
    MaturityLevel(
        level=2,
        name="AI-Assisted",
        description="Organisation has sanctioned AI tools with governance. Some workflows enhanced with AI assistance but humans drive all decisions.",
        healthcare_example="Approved AI medical scribe for clinical documentation, AI-assisted medication checking, structured AI acceptable use policy in place.",
        indicators=[
            "AI acceptable use policy exists",
            "IT-approved AI tool list",
            "Some workflows enhanced with AI",
            "Basic AI training for staff",
            "Data governance for AI tools established",
        ],
    ),
    MaturityLevel(
        level=3,
        name="AI-Integrated",
        description="AI is embedded in core business workflows and data pipelines. Decisions are AI-informed with human oversight. Cross-functional AI initiatives.",
        healthcare_example="Automated patient intake with AI triage, AI-powered care minutes tracking and AN-ACC documentation, predictive rostering based on acuity data.",
        indicators=[
            "AI embedded in 3+ core workflows",
            "Data pipelines feed AI systems",
            "Cross-department AI initiatives",
            "Dedicated AI governance committee",
            "Regular AI performance monitoring",
            "Staff competency frameworks include AI skills",
        ],
    ),
    MaturityLevel(
        level=4,
        name="AI-Native",
        description="Organisation designed around AI capabilities. AI is the default for all suitable tasks. Humans focus on judgment, empathy, and oversight.",
        healthcare_example="AI-first care coordination platform, automated compliance reporting, AI-driven workforce planning, real-time clinical decision support integrated into all care delivery.",
        indicators=[
            "AI is default approach for new processes",
            "Organisation structure reflects AI capabilities",
            "Continuous AI improvement culture",
            "Advanced AI skills across all departments",
            "AI ROI measured systematically",
            "Innovation lab or AI experimentation function",
        ],
    ),
    MaturityLevel(
        level=5,
        name="Dark Factory",
        description="Autonomous operations with human oversight. All suitable processes run autonomously. Humans provide strategic direction, quality assurance, and care that requires human connection.",
        healthcare_example="Fully automated administrative operations (billing, scheduling, reporting). AI-assisted clinical workflows with human clinical judgment for final decisions. Real-time regulatory compliance monitoring.",
        indicators=[
            "Administrative processes largely autonomous",
            "Human effort focused on high-value activities",
            "Real-time performance optimisation",
            "Predictive rather than reactive operations",
            "Industry-leading AI capabilities",
            "Continuous autonomous improvement cycles",
        ],
    ),
]


def get_maturity_level(level: int) -> MaturityLevel:
    """Return the MaturityLevel for a given level number (0-5)."""
    if 0 <= level <= 5:
        return MATURITY_LEVELS[level]
    raise ValueError(f"Maturity level must be 0-5, got {level}")


def classify_maturity(score: float) -> MaturityLevel:
    """Classify a maturity score (0.0-5.0) into the nearest MaturityLevel."""
    level = min(5, max(0, round(score)))
    return MATURITY_LEVELS[level]


MATURITY_COLOURS = {
    0: "text-gray-500",
    1: "text-red-500",
    2: "text-orange-400",
    3: "text-yellow-400",
    4: "text-blue-400",
    5: "text-green-500",
}

MATURITY_LABELS = {level.level: level.name for level in MATURITY_LEVELS}
