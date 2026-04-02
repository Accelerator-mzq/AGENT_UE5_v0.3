"""
QA & Validation 基础域。
负责最小验证检查点与回归摘要。
"""

from __future__ import annotations

from typing import Any, Dict, List


DOMAIN_ID = "qa_validation"


def build_domain_descriptor() -> Dict[str, Any]:
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "QA & Validation",
        "status": "implemented",
        "capabilities": ["validation_checkpoints", "regression_summary"],
    }


def build_validation_checkpoints(run_plan_context: Dict[str, Any]) -> List[Dict[str, Any]]:
    """根据计划上下文生成最小验证检查点。"""
    workflow_sequence = run_plan_context.get("workflow_sequence", [])
    handoff = run_plan_context.get("handoff", {})
    if not workflow_sequence:
        return []

    last_step_id = workflow_sequence[-1].get("step_id", "")
    delta_context = handoff.get("delta_context", {})
    projection_profile = handoff.get("routing_context", {}).get("projection_profile", "preview_static")
    actor_names = [
        actor.get("actor_name", "")
        for actor in handoff.get("dynamic_spec_tree", {}).get("scene_spec", {}).get("actors", [])
        if actor.get("actor_name")
    ]

    checkpoints = [
        {
            "checkpoint_id": "validate_scene_actor_count",
            "after_step": last_step_id,
            "validation_type": "actor_count_check",
            "expected_actor_count": len(actor_names),
        },
        {
            "checkpoint_id": "validate_scene_actor_presence",
            "after_step": last_step_id,
            "validation_type": "actor_presence_check",
            "expected_actor_names": actor_names,
        },
    ]

    regression_focus = list(delta_context.get("required_regression_checks", []))
    if regression_focus:
        checkpoints.append(
            {
                "checkpoint_id": "validate_regression_focus",
                "after_step": last_step_id,
                "validation_type": "regression_focus_check",
                "required_regression_checks": regression_focus,
            }
        )

    if projection_profile == "runtime_playable" or handoff.get("project_context", {}).get("game_type") == "jrpg":
        checkpoints.append(
            {
                "checkpoint_id": "validate_runtime_contract",
                "after_step": last_step_id,
                "validation_type": "runtime_contract_check",
            }
        )

    return checkpoints


def build_regression_summary(handoff: Dict[str, Any], execution_result: Dict[str, Any]) -> Dict[str, Any]:
    """构建最小 Actor 级回归摘要。"""
    delta_context = handoff.get("delta_context", {})
    scene_actors = handoff.get("dynamic_spec_tree", {}).get("scene_spec", {}).get("actors", [])
    actor_names = [actor.get("actor_name", "") for actor in scene_actors if actor.get("actor_name")]

    return {
        "status": "captured" if execution_result.get("status") == "succeeded" else "needs_attention",
        "baseline_ref": handoff.get("baseline_context", {}).get("snapshot_ref", ""),
        "delta_intent": delta_context.get("delta_intent", "greenfield_bootstrap"),
        "added_actor_names": actor_names,
        "required_regression_checks": delta_context.get("required_regression_checks", []),
    }
