"""
Presentation & Asset 基础域。
"""

DOMAIN_ID = "presentation_asset"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Presentation & Asset",
        "status": "skeleton",
        "capabilities": ["ui_projection", "asset_binding"],
    }
