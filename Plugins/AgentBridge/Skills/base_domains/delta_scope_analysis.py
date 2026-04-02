"""
Delta Scope Analysis 基础域。
"""

DOMAIN_ID = "delta_scope_analysis"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Delta Scope Analysis",
        "status": "skeleton",
        "capabilities": ["delta_intent", "affected_specs"],
    }
