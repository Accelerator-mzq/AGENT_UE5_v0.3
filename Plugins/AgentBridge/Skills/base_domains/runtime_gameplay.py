"""
Runtime & Gameplay 基础域。
"""

DOMAIN_ID = "runtime_gameplay"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Runtime & Gameplay",
        "status": "skeleton",
        "capabilities": ["runtime_wiring", "gameplay_loop"],
    }
