"""
JRPG Scene Generator
在最小 Static Base + Genre Pack 约束下生成 JRPG dynamic spec tree。
"""

from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional


def generate_jrpg_dynamic_spec_tree(
    design_input: Dict[str, Any],
    routing_context: Dict[str, Any],
    static_spec_context: Dict[str, Any],
    pack_manifest: Dict[str, Any],
    pack_modules: Optional[Dict[str, Any]] = None,
    projection_profile: str = "preview_static",
) -> Dict[str, Any]:
    """生成 JRPG turn-based prototype 所需的最小 dynamic spec tree。"""
    loaded_specs = static_spec_context.get("loaded_specs", {})
    pack_modules = pack_modules or {}

    nodes: Dict[str, Any] = {
        "validation_spec": _build_validation_spec(loaded_specs, design_input),
        "generation_trace": {
            "generator": "AgentBridge.Compiler.Phase7.JRPGSceneGenerator",
            "activated_skill_packs": routing_context.get("activated_skill_packs", []),
            "static_spec_ids": sorted(list(loaded_specs.keys())),
            "skill_pack_id": pack_manifest.get("pack_id", "unknown"),
            "projection_profile": projection_profile,
            "required_skills": [],
            "review_extensions": [
                entry.get("module_id", "") for entry in pack_modules.get("review_extensions", [])
            ],
            "validation_extensions": [
                entry.get("module_id", "") for entry in pack_modules.get("validation_extensions", [])
            ],
            "missing_modules": [],
        },
    }

    compilation_state = {
        "design_input": design_input,
        "routing_context": routing_context,
        "static_spec_context": static_spec_context,
        "pack_manifest": pack_manifest,
        "pack_modules": pack_modules,
        "projection_profile": projection_profile,
        "nodes": nodes,
    }

    for skill_entry in pack_modules.get("required_skills", []):
        module = skill_entry.get("module")
        if module is None or not hasattr(module, "apply_skill"):
            nodes["generation_trace"]["missing_modules"].append(skill_entry.get("module_id", ""))
            continue
        module.apply_skill(compilation_state)

    delta_policy = {}
    for delta_entry in pack_modules.get("delta_policies", []):
        module = delta_entry.get("module")
        if module is None or not hasattr(module, "build_delta_policy"):
            continue
        delta_policy = module.build_delta_policy(design_input, routing_context)
        break
    if delta_policy:
        nodes["generation_trace"]["delta_policy"] = delta_policy

    for validator_entry in pack_modules.get("validation_extensions", []):
        module = validator_entry.get("module")
        if module is None or not hasattr(module, "build_validation_markers"):
            continue
        _merge_validation_markers(nodes["validation_spec"], module.build_validation_markers(compilation_state))

    nodes["scene_spec"] = {
        "actors": _build_scene_actors(design_input),
    }
    return nodes


def _build_validation_spec(loaded_specs: Dict[str, Any], design_input: Dict[str, Any]) -> Dict[str, Any]:
    """使用通用 ValidationStaticSpec 生成最小 JRPG 校验节点。"""
    base_template = copy.deepcopy(loaded_specs["ValidationStaticSpec"]["template"])
    data = base_template.setdefault("data", {})
    data.setdefault("required_checks", [])
    for check in ["battle_actor_presence", "command_menu_ready", "turn_queue_ready"]:
        if check not in data["required_checks"]:
            data["required_checks"].append(check)
    data["notes"] = list(data.get("notes", [])) + [f"目标类型：{design_input.get('game_type', 'unknown')}"]
    return {
        "spec_id": "JRPGValidationSpec",
        "version": base_template.get("version", "1.0"),
        "data": data,
    }


def _build_scene_actors(design_input: Dict[str, Any]) -> List[Dict[str, Any]]:
    """投影为当前 orchestrator 可消费的 scene actors。"""
    battle_arena = design_input.get("board", {}).get("location", [0.0, 0.0, 0.0])
    heroes = design_input.get("party_setup", {}).get("heroes", ["HeroUnit_1"])
    enemies = design_input.get("party_setup", {}).get("enemies", ["EnemyUnit_1"])

    actors = [
        {
            "actor_name": "BattleArena",
            "actor_class": "/Script/Engine.StaticMeshActor",
            "transform": {
                "location": [float(battle_arena[0]), float(battle_arena[1]), float(battle_arena[2])],
                "rotation": [0.0, 0.0, 0.0],
                "relative_scale3d": [6.0, 6.0, 0.2],
            },
        }
    ]

    for index, hero_name in enumerate(heroes):
        actors.append(
            {
                "actor_name": hero_name or f"HeroUnit_{index + 1}",
                "actor_class": "/Script/Engine.StaticMeshActor",
                "transform": {
                    "location": [-180.0, float(index) * 120.0, 50.0],
                    "rotation": [0.0, 0.0, 0.0],
                    "relative_scale3d": [0.8, 0.8, 1.6],
                },
            }
        )

    for index, enemy_name in enumerate(enemies):
        actors.append(
            {
                "actor_name": enemy_name or f"EnemyUnit_{index + 1}",
                "actor_class": "/Script/Engine.StaticMeshActor",
                "transform": {
                    "location": [180.0, float(index) * 120.0, 50.0],
                    "rotation": [0.0, 180.0, 0.0],
                    "relative_scale3d": [0.9, 0.9, 1.6],
                },
            }
        )

    actors.append(
        {
            "actor_name": "CommandMenuAnchor",
            "actor_class": "/Script/Engine.StaticMeshActor",
            "transform": {
                "location": [0.0, -260.0, 40.0],
                "rotation": [0.0, 0.0, 0.0],
                "relative_scale3d": [1.2, 0.4, 0.1],
            },
        }
    )
    return actors


def _merge_validation_markers(validation_spec: Dict[str, Any], markers: Dict[str, Any]) -> None:
    """把 validator 输出合并进 validation_spec。"""
    validation_data = validation_spec.setdefault("data", {})
    for key in ["required_checks", "runtime_smoke_checks", "validation_markers", "notes"]:
        validation_data.setdefault(key, [])

    for key in ["required_checks", "runtime_smoke_checks", "validation_markers", "notes"]:
        for item in markers.get(key, []):
            if item not in validation_data[key]:
                validation_data[key].append(item)
