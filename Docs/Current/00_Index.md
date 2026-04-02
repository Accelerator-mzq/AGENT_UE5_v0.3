# 当前阶段文档索引

> 阶段名称：Phase 7 — 正式开发期（治理闭环 + JRPG 第二类型包）
> 状态：Active
> 起始日期：2026-04-02
> 文档版本：L1-Phase7-v1

## 本目录文件

| 文件 | 摘要 |
|------|------|
| 01_Project_Baseline.md | 进入 Phase 7 开发期时的项目事实与当前基线 |
| 02_Current_Phase_Goals.md | 本期目标、成功标准与默认假设 |
| 03_Active_Backlog.md | 当前待办、开发顺序与观察项 |
| 04_Open_Risks.md | 当前风险、缓解策略与不做项 |
| 05_Implementation_Boundary.md | Phase 7 允许改动与禁止改动范围 |
| 06_Current_Task_List.md | 当前阶段唯一任务入口导航 |
| 07_Evidence_And_Artifacts.md | Reports / Evidence / Snapshots 的落盘约定 |
| 08_Playable_Runtime_Acceptance.md | 已归档的 Phase 6 playable runtime 验收基线 |

## 当前事实来源

- 当前阶段任务入口：[task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
- 上一阶段正式归档：[task4_phase6.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task4_phase6.md)
- 本阶段准备期归档：[task5_phase7_preparation.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task5_phase7_preparation.md)
- Phase 6 历史证据归档：[phase6_evidence_2026-04-02](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/reports/AgentBridgeEvidence/phase6_evidence_2026-04-02)
- 框架级规范：`Plugins/AgentBridge/Docs/` + `Schemas/` + `Specs/`

## 当前附加规则

- `Phase 6` 已完成并归档，当前阶段不再使用准备期口径
- 根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md) 是 Phase 7 开发期唯一任务入口
- [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 与 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 在 Phase 7 开发期间保持 `206` 条口径不动
- Phase 7 新测试只维护在根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)，阶段结束归档时再补录进总表
