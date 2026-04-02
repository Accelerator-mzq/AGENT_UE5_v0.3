"""
Turn Queue Skill
负责生成 JRPG 的回合队列表达。
"""

from __future__ import annotations

from typing import Any, Dict


def apply_skill(compilation_state: Dict[str, Any]) -> Dict[str, Any]:
    """生成 turn_queue_spec。"""
    design_input = compilation_state["design_input"]
    nodes = compilation_state["nodes"]
    heroes = list(design_input.get("party_setup", {}).get("heroes", ["HeroUnit_1"]))
    enemies = list(design_input.get("party_setup", {}).get("enemies", ["EnemyUnit_1"]))

    nodes["turn_queue_spec"] = {
        "spec_id": "TurnQueueSpec",
        "version": "1.0",
        "data": {
            "queue_order": heroes + enemies,
            "turn_model": "turn_based",
            "initiative_source": "fixed_party_order",
        },
    }
    _append_trace(nodes, "turn_queue")
    return compilation_state


def _append_trace(nodes: Dict[str, Any], skill_id: str) -> None:
    """记录 skill 执行轨迹。"""
    trace = nodes.setdefault("generation_trace", {})
    trace.setdefault("required_skills", [])
    if skill_id not in trace["required_skills"]:
        trace["required_skills"].append(skill_id)
