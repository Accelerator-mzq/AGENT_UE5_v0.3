"""
Battle Layout Skill
负责生成 JRPG 战斗场景与核心 spec。
"""

from __future__ import annotations

import copy
from typing import Any, Dict


def apply_skill(compilation_state: Dict[str, Any]) -> Dict[str, Any]:
    """生成 world_build_spec / jrpg_spec / battle_layout_spec。"""
    design_input = compilation_state["design_input"]
    loaded_specs = compilation_state["static_spec_context"]["loaded_specs"]
    nodes = compilation_state["nodes"]
    routing_context = compilation_state["routing_context"]
    pack_manifest = compilation_state["pack_manifest"]

    nodes["world_build_spec"] = _build_world_build_spec(loaded_specs)
    nodes["jrpg_spec"] = {
        "spec_id": "JRPGSpec",
        "version": "1.0",
        "data": {
            "combat_spec": copy.deepcopy(design_input.get("combat_spec", {})),
            "party_setup": copy.deepcopy(design_input.get("party_setup", {})),
            "feature_tags": list(design_input.get("feature_tags", [])),
            "skill_pack": {
                "pack_id": pack_manifest.get("pack_id", "genre-jrpg"),
                "activated_skill_packs": routing_context.get("activated_skill_packs", []),
            },
        },
    }
    nodes["battle_layout_spec"] = {
        "spec_id": "BattleLayoutSpec",
        "version": "1.0",
        "data": {
            "arena_name": "BattleArena",
            "hero_slots": list(design_input.get("party_setup", {}).get("heroes", ["HeroUnit_1"])),
            "enemy_slots": list(design_input.get("party_setup", {}).get("enemies", ["EnemyUnit_1"])),
        },
    }

    _append_trace(nodes, "battle_layout")
    return compilation_state


def _build_world_build_spec(loaded_specs: Dict[str, Any]) -> Dict[str, Any]:
    """从通用基座实例化场景节点。"""
    template = copy.deepcopy(loaded_specs["WorldBuildStaticSpec"]["template"])
    template["data"]["board"] = {
        "board_type": "battle_arena",
        "grid_size": [1, 1],
        "cell_size_cm": [600, 600],
        "total_size_cm": [600, 600],
        "location": [0.0, 0.0, 0.0],
        "material": "JRPGArenaMaterial",
    }
    template["data"]["actor_defaults"]["actor_class"] = "/Script/Engine.StaticMeshActor"
    return template


def _append_trace(nodes: Dict[str, Any], skill_id: str) -> None:
    """记录 skill 执行轨迹。"""
    trace = nodes.setdefault("generation_trace", {})
    trace.setdefault("required_skills", [])
    if skill_id not in trace["required_skills"]:
        trace["required_skills"].append(skill_id)
