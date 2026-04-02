"""
World & Level 基础域。
"""

DOMAIN_ID = "world_level"


def build_domain_descriptor():
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "World & Level",
        "status": "skeleton",
        "capabilities": ["scene_projection", "level_layout"],
    }
