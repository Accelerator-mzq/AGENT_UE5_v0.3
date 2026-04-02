"""
JRPG Reviewer
执行 JRPG pack 特有的编译期审查。
"""

from __future__ import annotations

from typing import Any, Dict, List


def review_dynamic_spec_tree(
    design_input: Dict[str, Any],
    dynamic_spec_tree: Dict[str, Any],
    routing_context: Dict[str, Any],
    analysis_context: Dict[str, Any],
) -> Dict[str, Any]:
    """对 JRPG 特有节点做最小审查。"""
    errors: List[str] = []
    warnings: List[str] = []
    capability_gaps = {
        "required_static_templates": [],
        "unresolved_refs": [],
        "unsupported_gdd_sections": [],
        "missing_patch_contracts": [],
        "missing_migration_contracts": [],
        "unsupported_regression_checks": [],
    }

    required_nodes = [
        "jrpg_spec",
        "battle_layout_spec",
        "turn_queue_spec",
        "command_menu_spec",
        "runtime_wiring_spec",
    ]
    for node_name in required_nodes:
        if node_name not in dynamic_spec_tree:
            errors.append(f"缺少 jrpg 必需节点: {node_name}")

    scene_actors = list(dynamic_spec_tree.get("scene_spec", {}).get("actors", []))
    if routing_context.get("mode") == "brownfield_expansion":
        # Brownfield 下 scene_spec 只携带增量 Actor，审查时需要把 baseline 里的 Actor 一并并入视角。
        baseline_actors = (
            analysis_context.get("baseline_snapshot", {})
            .get("current_spec_baseline", {})
            .get("scene_spec", {})
            .get("actors", [])
        )
        scene_actors = list(baseline_actors) + scene_actors

    actor_names = [actor.get("actor_name", "") for actor in scene_actors]
    for required_actor in ["BattleArena", "CommandMenuAnchor"]:
        if required_actor not in actor_names:
            errors.append(f"JRPG scene_spec 缺少必需 Actor: {required_actor}")

    if routing_context.get("mode") == "brownfield_expansion":
        required_checks = analysis_context.get("delta_context", {}).get("required_regression_checks", [])
        if "jrpg-battle-loop-smoke-check" not in required_checks:
            warnings.append("JRPG Brownfield 缺少 battle loop 回归检查")

    return {
        "errors": errors,
        "warnings": warnings,
        "capability_gaps": capability_gaps,
        "notes": ["jrpg reviewer 已检查战斗闭环最小节点。"],
    }
