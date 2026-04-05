# 当前阶段文档索引

> 阶段名称：Phase 8 - Skill-First Compiler Reset + MonopolyGame 垂直切片
> 状态：Completed / Awaiting Phase 9 Planning
> 启动日期：2026-04-03
> 文档版本：L1-Phase8-v3

## 本目录文件

| 文件 | 摘要 |
|------|------|
| 01_Project_Baseline.md | 当前项目基线，包含 Phase 8 已落地产物 |
| 02_Current_Phase_Goals.md | Phase 8 阶段目标与成功标准 |
| 03_Active_Backlog.md | Phase 8 当前待办与进展 |
| 04_Open_Risks.md | Phase 8 当前风险与风险状态 |
| 05_Implementation_Boundary.md | Phase 8 实施边界 |
| 06_Current_Task_List.md | 当前任务入口说明 |
| 07_Evidence_And_Artifacts.md | Reports / Evidence / Snapshots 的落盘规则 |
| 08_Phase8_Retrospective_And_Phase9_Checklist.md | Phase 8 运行时问题复盘与 Phase 9 防回归清单 |
| 10_Phase8_Closeout.md | Phase 8 收尾结论、证据和归档口径 |

## 当前事实来源

- Phase 8 收尾总览：[10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md)
- Phase 8 历史任务：[task8_phase8.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task8_phase8.md)
- 根目录占位任务入口：[task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
- Phase 8 统一方案：[Phase8_Plan_Original.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Proposals/Phase8_Plan_Original.md)
- Phase 8 交接文档：[Phase8_M3_Handover_to_Execution_Agent.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Proposals/Phase8_M3_Handover_to_Execution_Agent.md)
- Phase 8 详细设计：[Phase8_DD1_Schema_and_Interface_Spec.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Proposals/Phase8_DD1_Schema_and_Interface_Spec.md) / [Phase8_DD3_Lowering_Map_and_CPP_Design.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Proposals/Phase8_DD3_Lowering_Map_and_CPP_Design.md)
- Phase 8 Compiler 产物：`ProjectState/phase8/`
- 上一阶段归档任务：[task6_phase7.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task6_phase7.md)
- 框架级规范：`Plugins/AgentBridge/Docs/` + `Schemas/` + `Compiler/` + `SkillTemplates/` + `MCP/`

## 当前附加规则

- Phase 8 已收尾，当前项目口径以 [10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md) 为准。
- 根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md) 当前仅作下一阶段占位入口，不再承载 Phase 8 正文。
- [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 与 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 当前登记 `234` 条用例，其中原 `230` 条地基保留，Phase 8 新增 `E2E-37 ~ E2E-40` 已补录。
- Phase 8 运行时问题复盘与后续防回归要求，统一记录在 [08_Phase8_Retrospective_And_Phase9_Checklist.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/08_Phase8_Retrospective_And_Phase9_Checklist.md)。
- 如果需要重做 Phase 8 的任务口径设计，请将 [Phase8_Task_Redesign_Draft.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Proposals/Phase8_Task_Redesign_Draft.md) 视为历史参考草案，而不是当前生效任务。
