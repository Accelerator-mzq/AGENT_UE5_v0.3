"""
Product & Scope 基础域。
"""

DOMAIN_ID = "product_scope"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Product & Scope",
        "status": "skeleton",
        "capabilities": ["goal_summary", "stage_boundary"],
    }
