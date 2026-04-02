"""
Design & Project State Intake 基础域。
"""

DOMAIN_ID = "design_project_state_intake"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Design & Project State Intake",
        "status": "skeleton",
        "capabilities": ["design_input_adapter", "project_state_adapter"],
    }
