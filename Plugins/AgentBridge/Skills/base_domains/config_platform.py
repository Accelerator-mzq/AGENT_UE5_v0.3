"""
Config & Platform 基础域。
"""

DOMAIN_ID = "config_platform"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Config & Platform",
        "status": "skeleton",
        "capabilities": ["platform_profile", "config_defaults"],
    }
