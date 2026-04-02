"""
Baseline Understanding 基础域。
"""

DOMAIN_ID = "baseline_understanding"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Baseline Understanding",
        "status": "skeleton",
        "capabilities": ["baseline_snapshot", "current_project_model"],
    }
