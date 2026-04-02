"""
JRPG Delta Policy
提供 JRPG pack 的最小 Brownfield 策略。
"""

from __future__ import annotations

from typing import Any, Dict


def build_delta_policy(design_input: Dict[str, Any], routing_context: Dict[str, Any]) -> Dict[str, Any]:
    """构建最小 JRPG delta policy。"""
    return {
        "policy_id": "jrpg_delta_policy",
        "regression_focus": [
            "existing_actor_presence",
            "jrpg-battle-loop-smoke-check",
            "jrpg-command-menu-smoke-check",
        ],
        "high_risk_breakpoints": [
            "turn_queue_changed",
            "command_menu_changed",
            "runtime_wiring_changed",
        ],
        "routing_mode": routing_context.get("mode", "greenfield_bootstrap"),
        "game_type": design_input.get("game_type", "jrpg"),
    }
