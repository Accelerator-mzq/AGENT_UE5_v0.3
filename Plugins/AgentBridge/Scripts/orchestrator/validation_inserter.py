"""
Validation Inserter
根据 handoff、workflow 和基础治理域插入最小验证检查点。
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


def insert_validation_checkpoints(
    workflow_sequence: List[Dict[str, Any]],
    handoff: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """为 Run Plan 插入最小验证检查点。"""
    if not workflow_sequence:
        return []

    base_domain_refs = handoff.get("governance_context", {}).get("base_domain_refs", [])
    base_domains = load_base_domain_modules(base_domain_refs)
    qa_entry = base_domains.get("domain_map", {}).get("qa_validation", {})
    qa_module = qa_entry.get("module")

    if qa_module is not None and hasattr(qa_module, "build_validation_checkpoints"):
        return qa_module.build_validation_checkpoints(
            {
                "workflow_sequence": workflow_sequence,
                "handoff": handoff,
            }
        )

    last_step = workflow_sequence[-1]
    return [
        {
            "checkpoint_id": "validate_scene_actor_count",
            "after_step": last_step.get("step_id", ""),
            "validation_type": "actor_count_check",
        }
    ]
