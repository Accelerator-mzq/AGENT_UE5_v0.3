"""
Command Menu Skill
负责生成最小命令菜单与 runtime wiring。
"""

from __future__ import annotations

from typing import Any, Dict


def apply_skill(compilation_state: Dict[str, Any]) -> Dict[str, Any]:
    """生成 command_menu_spec / runtime_wiring_spec。"""
    design_input = compilation_state["design_input"]
    nodes = compilation_state["nodes"]
    commands = list(design_input.get("combat_spec", {}).get("command_menu", ["Attack", "Skill", "Defend"]))

    nodes["command_menu_spec"] = {
        "spec_id": "CommandMenuSpec",
        "version": "1.0",
        "data": {
            "commands": commands,
            "default_selection": commands[0] if commands else "",
            "display_mode": "minimal_status_text",
        },
    }
    nodes["runtime_wiring_spec"] = {
        "spec_id": "JRPGRuntimeWiringSpec",
        "version": "1.0",
        "data": {
            "battle_controller_actor_class": "/Script/Engine.StaticMeshActor",
            "command_menu_actor_name": "CommandMenuAnchor",
            "projection_profile": compilation_state.get("projection_profile", "preview_static"),
        },
    }
    _append_trace(nodes, "command_menu")
    return compilation_state


def _append_trace(nodes: Dict[str, Any], skill_id: str) -> None:
    """记录 skill 执行轨迹。"""
    trace = nodes.setdefault("generation_trace", {})
    trace.setdefault("required_skills", [])
    if skill_id not in trace["required_skills"]:
        trace["required_skills"].append(skill_id)
