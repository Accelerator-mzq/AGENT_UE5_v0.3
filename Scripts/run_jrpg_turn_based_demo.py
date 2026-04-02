"""
端到端运行脚本
JRPG Turn-Based + Reviewed Handoff 最小闭环。
"""

from __future__ import annotations

import os
import sys
from typing import Any, Dict


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "Plugins", "AgentBridge", "Scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from bridge.project_config import get_dated_project_reports_dir
from compiler.handoff import build_handoff, serialize_handoff
from compiler.intake import read_gdd
from orchestrator.handoff_runner import run_from_handoff


def run_jrpg_turn_based_demo(
    bridge_mode: str = "simulated",
    mode: str = "greenfield_bootstrap",
) -> Dict[str, Any]:
    """运行 JRPG 最小闭环。"""
    gdd_path = os.path.join(PROJECT_ROOT, "ProjectInputs", "GDD", "jrpg_turn_based_v1.md")
    handoff_draft_dir = os.path.join(PROJECT_ROOT, "ProjectState", "Handoffs", "draft")
    handoff_approved_dir = os.path.join(PROJECT_ROOT, "ProjectState", "Handoffs", "approved")
    report_dir = str(get_dated_project_reports_dir())

    for directory in [handoff_draft_dir, handoff_approved_dir, report_dir]:
        os.makedirs(directory, exist_ok=True)

    print("=" * 60)
    print("JRPG Turn-Based + Handoff 最小闭环")
    print("=" * 60)

    design_input = read_gdd(gdd_path)
    project_state = _build_project_state(mode)

    print(f"  游戏类型: {design_input['game_type']}")
    print(f"  执行模式: {mode}")

    handoff = build_handoff(
        design_input=design_input,
        mode=mode,
        project_state=project_state,
        target_stage="vertical_slice",
        projection_profile="preview_static",
    )
    print(f"  Handoff ID: {handoff['handoff_id']}")
    print(f"  Handoff 状态: {handoff['status']}")
    print(f"  激活基础域: {handoff.get('governance_context', {}).get('base_domain_refs', [])}")

    draft_path = serialize_handoff(handoff, handoff_draft_dir, "yaml")
    approved_handoff = dict(handoff)
    approved_handoff["status"] = "approved_for_execution"
    approved_path = serialize_handoff(approved_handoff, handoff_approved_dir, "yaml")

    result = run_from_handoff(
        approved_path,
        report_output_dir=report_dir,
        bridge_mode=bridge_mode,
    )
    print(f"  执行状态: {result['status']}")
    print(f"  Draft Handoff: {draft_path}")
    print(f"  Approved Handoff: {approved_path}")
    print(f"  报告目录: {report_dir}")
    return result


def _build_project_state(mode: str) -> Dict[str, Any]:
    """构建 JRPG demo 使用的项目现状。"""
    if mode != "brownfield_expansion":
        return {
            "project_name": "Mvpv4TestCodex",
            "engine_version": "UE5.5.4",
            "current_level": "/Game/Maps/TestMap",
            "actor_count": 0,
            "is_empty": True,
            "actors": [],
            "has_existing_content": False,
            "has_baseline": False,
            "baseline_refs": [],
            "registry_refs": [],
            "known_issues_summary": [],
            "current_project_state_digest": "jrpg-greenfield-demo",
        }

    actors = [
        {
            "actor_name": "BattleArena",
            "actor_path": "/Game/Maps/TestMap.TestMap:PersistentLevel.BattleArena",
            "class": "/Script/Engine.StaticMeshActor",
            "transform": {
                "location": [0.0, 0.0, 0.0],
                "rotation": [0.0, 0.0, 0.0],
                "relative_scale3d": [6.0, 6.0, 0.2],
            },
            "tags": ["Baseline"],
        },
        {
            "actor_name": "HeroUnit_1",
            "actor_path": "/Game/Maps/TestMap.TestMap:PersistentLevel.HeroUnit_1",
            "class": "/Script/Engine.StaticMeshActor",
            "transform": {
                "location": [-180.0, 0.0, 50.0],
                "rotation": [0.0, 0.0, 0.0],
                "relative_scale3d": [0.8, 0.8, 1.6],
            },
            "tags": ["Baseline"],
        },
    ]

    return {
        "project_name": "Mvpv4TestCodex",
        "engine_version": "UE5.5.4",
        "current_level": "/Game/Maps/TestMap",
        "actor_count": len(actors),
        "is_empty": False,
        "actors": actors,
        "has_existing_content": True,
        "has_baseline": False,
        "baseline_refs": [],
        "registry_refs": [],
        "known_issues_summary": [],
        "current_project_state_digest": "jrpg-brownfield-demo",
    }


if __name__ == "__main__":
    selected_bridge_mode = "simulated"
    selected_mode = "greenfield_bootstrap"
    if len(sys.argv) > 1:
        selected_bridge_mode = sys.argv[1]
    if len(sys.argv) > 2:
        selected_mode = sys.argv[2]

    result = run_jrpg_turn_based_demo(bridge_mode=selected_bridge_mode, mode=selected_mode)
    sys.exit(0 if result.get("status") == "succeeded" else 1)
