# 项目基线

> 文档版本：L1-Phase7-v1
> 更新时间：2026-04-02

## 1. 当前阶段事实

- `Phase 6` 已完成并归档，完整任务见 [task4_phase6.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task4_phase6.md)
- `Phase 7` 当前已进入正式开发期，准备期任务已归档到 [task5_phase7_preparation.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task5_phase7_preparation.md)
- 项目层当前稳定保留三条可回归主链：
  - Greenfield：`Scripts/run_greenfield_demo.py`
  - Brownfield：`Scripts/run_brownfield_demo.py`
  - Boardgame playable runtime：`Scripts/run_boardgame_playable_demo.py`
- 插件层当前总表仍维持 `206` 条已归档测试口径，不在本阶段中途扩容

## 2. 已稳定的 Phase 6 能力

- `boardgame` 已是首个真实类型包，支持 `_core` + manifest + required skills + review / validation / delta policy
- `preview_static` 与 `runtime_playable` 双投影已落地
- `Brownfield append/new-actor` 最小闭环已落地
- 项目层 playable runtime、真实截图证据与顶视图验收已经落地

## 3. Phase 7 当前目标基线

本期不重做 Phase 6，而是在其上补齐以下最小能力：

1. `Validation Inserter`
2. `Recovery Planner`
3. Actor 级 `Regression Summary`
4. `Freeze / Snapshot Manifest`
5. `Minimal Promotion`
6. `Base Skill Domains` 最小真实化
7. 第二个 `Genre Pack`：`JRPG Turn-Based`

## 4. 当前目录与落盘约定

- 项目级报告：`ProjectState/Reports/YYYY-MM-DD/`
- 插件级报告：`Plugins/AgentBridge/reports/YYYY-MM-DD/`
- Snapshot：`ProjectState/Snapshots/YYYY-MM-DD/`
- 当前阶段证据与记录统一继续落在项目目录内，不扩写到项目外目录

## 5. 当前不变的治理约束

- `SystemTestCases.md` 与 `run_system_tests.py` 在 Phase 7 开发期保持现状，不提前写入新编号
- 现有 `boardgame` 主链必须继续可回归
- `Phase 7` 新增能力优先通过新增模块接入，不重写稳定核心
