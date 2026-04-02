"""
Recovery Planner
根据模式、类型包和治理域生成最小恢复策略。
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List

try:
    from Plugins.AgentBridge.Skills.base_domains import load_base_domain_modules
except ModuleNotFoundError:
    project_root = Path(__file__).resolve().parents[4]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from Plugins.AgentBridge.Skills.base_domains import load_base_domain_modules


def build_recovery_plan(
    handoff: Dict[str, Any],
    workflow_sequence: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """构建最小恢复策略与计划阻断信息。"""
    blockers: List[str] = []
    if not workflow_sequence:
        blockers.append("缺少 workflow_sequence，无法构建恢复策略")

    base_domain_refs = handoff.get("governance_context", {}).get("base_domain_refs", [])
    if not base_domain_refs:
        blockers.append("缺少 base_domain_refs，无法启用 Phase 7 治理域")

    base_domains = load_base_domain_modules(base_domain_refs)
    governance_entry = base_domains.get("domain_map", {}).get("planning_governance", {})
    governance_module = governance_entry.get("module")

    if governance_module is not None and hasattr(governance_module, "build_recovery_policy"):
        recovery = governance_module.build_recovery_policy(
            {
                "handoff": handoff,
                "workflow_sequence": workflow_sequence,
            }
        )
    else:
        game_type = handoff.get("project_context", {}).get("game_type", "unknown")
        mode = handoff.get("handoff_mode", "greenfield_bootstrap")
        recovery = {
            "policy_ref": f"recovery.{game_type}.{mode}.minimal",
            "policies": {
                "on_step_failure": "rebuild_handoff",
                "on_validation_failure": "manual_governance_review",
            },
        }

    recovery["blockers"] = blockers
    return recovery
