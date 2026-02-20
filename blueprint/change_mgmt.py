"""Change management framework for AI transformation."""

from .models import ChangeManagementPlan


def create_default_change_plan(organisation_name: str = "Organisation") -> ChangeManagementPlan:
    """Return a template change management plan for healthcare AI transformation."""
    return ChangeManagementPlan(
        stakeholder_map=[
            {"role": "CEO/Executive Director", "influence": "high", "support_level": "champion", "strategy": "Engage as executive sponsor, provide regular ROI updates"},
            {"role": "Clinical Director/DON", "influence": "high", "support_level": "supportive", "strategy": "Involve in clinical AI tool selection, address patient safety concerns"},
            {"role": "IT Manager", "influence": "high", "support_level": "supportive", "strategy": "Partner on technical implementation, address security and integration concerns"},
            {"role": "Finance Manager", "influence": "medium", "support_level": "neutral", "strategy": "Demonstrate cost savings and revenue improvements with data"},
            {"role": "HR Manager", "influence": "medium", "support_level": "cautious", "strategy": "Address job security concerns, emphasise role evolution not elimination"},
            {"role": "Clinical Staff (RNs, ENs)", "influence": "medium", "support_level": "mixed", "strategy": "Pilot with early adopters, demonstrate time savings, address documentation burden"},
            {"role": "Administrative Staff", "influence": "low", "support_level": "cautious", "strategy": "Provide hands-on training, celebrate early wins, pair with AI champions"},
            {"role": "Residents/Patients & Families", "influence": "low", "support_level": "neutral", "strategy": "Communicate transparency about AI use, emphasise care quality improvements"},
        ],
        communication_plan=[
            {"phase": "Awareness", "audience": "All staff", "channel": "Town hall + email", "message": f"{organisation_name} is investing in AI to support staff, not replace them", "frequency": "Month 1"},
            {"phase": "Awareness", "audience": "Management", "channel": "Workshop", "message": "AI transformation roadmap, ROI projections, and timeline", "frequency": "Month 1"},
            {"phase": "Understanding", "audience": "Department leads", "channel": "Department meetings", "message": "Specific AI tools for your department and expected benefits", "frequency": "Month 2-3"},
            {"phase": "Understanding", "audience": "All staff", "channel": "Intranet + posters", "message": "FAQ: What AI means for your role, training opportunities", "frequency": "Month 2-3"},
            {"phase": "Adoption", "audience": "Pilot teams", "channel": "Hands-on workshops", "message": "Here's how to use the new AI tools, feedback welcome", "frequency": "Month 3-6"},
            {"phase": "Adoption", "audience": "All staff", "channel": "Newsletter + Slack", "message": "Pilot results, success stories, upcoming rollout schedule", "frequency": "Month 4-6"},
            {"phase": "Reinforcement", "audience": "All staff", "channel": "Monthly updates", "message": "Progress dashboard, time saved, quality improvements", "frequency": "Month 6-12"},
            {"phase": "Reinforcement", "audience": "Management", "channel": "Quarterly review", "message": "ROI actuals vs projections, next phase planning", "frequency": "Quarterly"},
        ],
        resistance_mitigation=[
            {"risk": "Fear of job loss", "likelihood": "high", "mitigation": "Emphasise role evolution messaging, show new role descriptions, guarantee no AI-caused redundancies in first 12 months"},
            {"risk": "Technology anxiety", "likelihood": "high", "mitigation": "Provide graduated training, pair anxious staff with AI champions, allow practice time before go-live"},
            {"risk": "Clinical safety concerns", "likelihood": "medium", "mitigation": "Implement human-in-the-loop for all clinical AI, share evidence from peer organisations, involve clinicians in tool selection"},
            {"risk": "Change fatigue", "likelihood": "medium", "mitigation": "Phase rollout to avoid overwhelm, celebrate quick wins, reduce other change initiatives during AI adoption"},
            {"risk": "Data privacy fears", "likelihood": "medium", "mitigation": "Transparent data governance policy, regular privacy updates, involve privacy officer in all AI deployments"},
            {"risk": "Workflow disruption", "likelihood": "high", "mitigation": "Run parallel systems during transition, have rollback plan, dedicated support during first 2 weeks"},
        ],
        success_metrics=[
            {"metric": "Staff AI adoption rate", "target": ">80% within 6 months of training", "measurement_method": "AI tool usage analytics and login data"},
            {"metric": "Time savings per staff member", "target": ">2 hours/week average", "measurement_method": "Time tracking surveys and workflow analytics"},
            {"metric": "Staff satisfaction with AI tools", "target": ">70% positive", "measurement_method": "Quarterly pulse survey"},
            {"metric": "Clinical documentation time", "target": "50% reduction", "measurement_method": "EHR time-stamp analysis pre/post"},
            {"metric": "Incident reporting timeliness", "target": "100% within required timeframe", "measurement_method": "SIRS submission timestamps"},
            {"metric": "Revenue impact", "target": ">$100K annual improvement", "measurement_method": "Financial reporting comparison"},
            {"metric": "Error/rework reduction", "target": "30% reduction in billing rejections", "measurement_method": "Claims rejection rate tracking"},
            {"metric": "Staff turnover", "target": "10% reduction in first year", "measurement_method": "HR turnover reporting"},
        ],
        phases=[
            {"name": "Phase 1: Foundation", "duration_months": 3, "objectives": ["Establish AI governance committee", "Complete shadow AI assessment", "Select and procure initial AI tools", "Begin staff awareness campaign"], "deliverables": ["AI acceptable use policy", "Tool selection report", "Communication plan launched"]},
            {"name": "Phase 2: Pilot", "duration_months": 3, "objectives": ["Deploy AI tools in 1-2 departments", "Train pilot team", "Measure initial results", "Gather feedback and iterate"], "deliverables": ["Pilot deployment complete", "Training materials", "Initial ROI measurement", "Feedback report"]},
            {"name": "Phase 3: Scale", "duration_months": 3, "objectives": ["Roll out to remaining departments", "Complete role transition training", "Optimise workflows based on pilot learnings", "Establish ongoing support model"], "deliverables": ["Organisation-wide deployment", "All staff trained", "Optimised workflows documented", "Support model operational"]},
            {"name": "Phase 4: Optimise", "duration_months": 3, "objectives": ["Measure full ROI", "Identify next wave of AI opportunities", "Embed continuous improvement", "Plan advanced AI capabilities"], "deliverables": ["12-month ROI report", "Next phase roadmap", "Continuous improvement framework", "Advanced AI business case"]},
        ],
    )
