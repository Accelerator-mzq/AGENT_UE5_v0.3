"""
Base Skill Domains Registry
统一声明 Phase 7 使用的 10 个基础域。
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional


BASE_DOMAIN_ORDER = [
    "design_project_state_intake",
    "baseline_understanding",
    "delta_scope_analysis",
    "product_scope",
    "runtime_gameplay",
    "world_level",
    "presentation_asset",
    "config_platform",
    "qa_validation",
    "planning_governance",
]


def get_default_base_domain_root(project_root: Optional[str] = None) -> str:
    """返回 base_domains 根目录。"""
    if project_root:
        return os.path.join(project_root, "Plugins", "AgentBridge", "Skills", "base_domains")
    return os.path.abspath(os.path.dirname(__file__))


def load_base_domain_registry(base_root: Optional[str] = None) -> Dict[str, Any]:
    """构建基础域 registry。"""
    resolved_root = base_root or get_default_base_domain_root()
    domains: List[Dict[str, Any]] = []

    for domain_id in BASE_DOMAIN_ORDER:
        module_path = os.path.join(resolved_root, f"{domain_id}.py")
        domains.append(
            {
                "domain_id": domain_id,
                "module_path": module_path,
                "exists": os.path.exists(module_path),
            }
        )

    return {
        "base_domain_root": resolved_root,
        "domains": domains,
        "domain_map": {entry["domain_id"]: entry for entry in domains},
    }


def resolve_required_base_domains(pack_manifest: Dict[str, Any]) -> List[str]:
    """从类型包 manifest 中解析依赖的基础域。"""
    domain_ids = pack_manifest.get("dependencies", {}).get("base_domains", [])
    return [domain_id for domain_id in domain_ids if domain_id in BASE_DOMAIN_ORDER]
