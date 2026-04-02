"""
Base Skill Domains Loader
按 registry 约定加载基础域模块。
"""

from __future__ import annotations

import importlib.util
from types import ModuleType
from typing import Any, Dict, List, Optional

from .registry import load_base_domain_registry, resolve_required_base_domains


def load_base_domain_modules(
    domain_ids: Optional[List[str]] = None,
    base_root: Optional[str] = None,
) -> Dict[str, Any]:
    """按域 ID 列表加载基础域模块。"""
    registry = load_base_domain_registry(base_root)
    selected_ids = domain_ids or [entry["domain_id"] for entry in registry["domains"]]
    loaded_entries: List[Dict[str, Any]] = []

    for domain_id in selected_ids:
        entry = registry["domain_map"].get(domain_id)
        if entry is None:
            loaded_entries.append(
                {
                    "domain_id": domain_id,
                    "module_path": "",
                    "module": None,
                    "exists": False,
                }
            )
            continue

        if not entry["exists"]:
            loaded_entries.append(
                {
                    "domain_id": domain_id,
                    "module_path": entry["module_path"],
                    "module": None,
                    "exists": False,
                }
            )
            continue

        loaded_entries.append(
            {
                "domain_id": domain_id,
                "module_path": entry["module_path"],
                "module": _load_python_module(entry["module_path"], domain_id),
                "exists": True,
            }
        )

    return {
        "registry": registry,
        "loaded_domains": loaded_entries,
        "domain_map": {entry["domain_id"]: entry for entry in loaded_entries},
    }


def load_required_base_domain_modules(
    pack_manifest: Dict[str, Any],
    base_root: Optional[str] = None,
) -> Dict[str, Any]:
    """按 pack manifest 依赖加载基础域模块。"""
    required_domain_ids = resolve_required_base_domains(pack_manifest)
    return load_base_domain_modules(required_domain_ids, base_root=base_root)


def _load_python_module(module_path: str, domain_id: str) -> ModuleType:
    """从文件路径加载基础域模块。"""
    import_name = f"agentbridge_phase7_base_domain_{domain_id}"
    spec = importlib.util.spec_from_file_location(import_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法为基础域生成导入 spec: {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
