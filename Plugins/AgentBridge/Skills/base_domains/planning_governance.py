"""
Planning & Governance 基础域。
负责最小恢复策略与 promotion 状态。
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict


DOMAIN_ID = "planning_governance"


def build_domain_descriptor() -> Dict[str, Any]:
    """返回基础域描述。"""
    return {
        "domain_id": DOMAIN_ID,
        "title": "Planning & Governance",
        "status": "implemented",
        "capabilities": ["recovery_policy", "promotion_status"],
    }


def build_recovery_policy(run_plan_context: Dict[str, Any]) -> Dict[str, Any]:
    """构建最小恢复策略。"""
    handoff = run_plan_context.get("handoff", {})
    mode = handoff.get("handoff_mode", "greenfield_bootstrap")
    game_type = handoff.get("project_context", {}).get("game_type", "unknown")
    delta_intent = handoff.get("delta_context", {}).get("delta_intent", "greenfield_bootstrap")
    policy_ref = f"recovery.{game_type}.{mode}.minimal"

    return {
        "policy_ref": policy_ref,
        "policies": {
            "on_step_failure": "rollback_new_actors" if mode == "brownfield_expansion" else "rebuild_handoff",
            "on_validation_failure": "review_handoff_and_retry",
            "on_blocked": "require_manual_governance_review",
            "delta_intent": delta_intent,
        },
    }


def build_promotion_status(
    handoff: Dict[str, Any],
    execution_result: Dict[str, Any],
    snapshot_ref: str,
) -> Dict[str, Any]:
    """根据执行结果生成最小 promotion 状态。"""
    succeeded = execution_result.get("status") == "succeeded"
    current_state = "approved" if succeeded else "reviewed"
    transition_time = datetime.now().isoformat()

    return {
        "current_state": current_state,
        "snapshot_ref": snapshot_ref,
        "transitions": [
            {"from": "draft", "to": "reviewed", "at": transition_time},
            {"from": "reviewed", "to": current_state, "at": transition_time},
        ],
        "audit_note": "Phase 7 最小 promotion 审计记录",
    }
