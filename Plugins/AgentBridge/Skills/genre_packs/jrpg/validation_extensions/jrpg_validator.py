"""
JRPG Validator
提供 JRPG pack 的最小验证标记。
"""

from __future__ import annotations

from typing import Any, Dict


def build_validation_markers(compilation_state: Dict[str, Any]) -> Dict[str, Any]:
    """返回最小验证标记。"""
    return {
        "required_checks": ["battle_actor_presence", "command_menu_ready", "turn_queue_ready"],
        "runtime_smoke_checks": ["jrpg-turn-based-smoke-check"],
        "validation_markers": ["jrpg-pack-active"],
        "notes": ["JRPG validator 已注入最小战斗闭环检查。"],
    }
