# Mvpv4TestCodex

> 目标引擎版本：UE5.5.4
> 当前状态：Phase 8 已收尾 / 等待 Phase 9 启动

## 项目简介

`Mvpv4TestCodex` 是基于 `AgentBridge` 插件的 UE5 工程，用于验证从设计输入到编译、handoff、执行、回归、治理与证据留存的完整开发链路。

当前已经完成并归档的阶段：

- Phase 6： [task4_phase6.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task4_phase6.md)
- Phase 7 准备期： [task5_phase7_preparation.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task5_phase7_preparation.md)
- Phase 7： [task6_phase7.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task6_phase7.md)
- Phase 8： [task8_phase8.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task8_phase8.md)

Phase 8 收尾证据见：

- [10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md)
- [phase8_task06_validation_2026-04-05_230956.json](/D:/UnrealProjects/Mvpv4TestCodex/ProjectState/Reports/2026-04-05/phase8_task06_validation_2026-04-05_230956.json)
- [system_test_report_2026-04-05_230956.json](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/reports/2026-04-05/system_test_report_2026-04-05_230956.json)

## 当前入口

- 当前索引： [00_Index.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/00_Index.md)
- Phase 8 收尾总览： [10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md)
- 根目录占位任务入口： [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
- 插件入口： [Plugins/AgentBridge/README.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/README.md)

当前根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md) 只保留为下一阶段占位入口，不再承载 Phase 8 正文。

## 常用命令

```bash
# Schema 校验
python Plugins/AgentBridge/Scripts/validation/validate_examples.py --strict

# Greenfield 最小闭环
python Scripts/run_greenfield_demo.py

# Brownfield 最小闭环
python Scripts/run_brownfield_demo.py

# Playable runtime 最小闭环
python Scripts/run_boardgame_playable_demo.py

# 系统测试总入口（当前登记 234 条）
python Plugins/AgentBridge/Tests/run_system_tests.py
```

## 目录结构

```text
Mvpv4TestCodex/
├── AGENTS.md
├── README.md
├── task.md                              ← 下一阶段占位入口
├── Scripts/
│   ├── run_greenfield_demo.py
│   ├── run_brownfield_demo.py
│   ├── run_boardgame_playable_demo.py
│   ├── run_jrpg_turn_based_demo.py
│   └── validation/
├── Source/
├── ProjectInputs/
├── ProjectState/
│   ├── Handoffs/
│   ├── Reports/
│   ├── RuntimeConfigs/
│   ├── Snapshots/
│   └── Evidence/
├── Docs/
└── Plugins/
    └── AgentBridge/
```

## 文档阅读顺序

1. [AGENTS.md](/D:/UnrealProjects/Mvpv4TestCodex/AGENTS.md)
2. [Docs/Current/00_Index.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/00_Index.md)
3. [Docs/Current/10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md)
4. [Docs/Current/01_Project_Baseline.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/01_Project_Baseline.md)
5. [Docs/Current/05_Implementation_Boundary.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/05_Implementation_Boundary.md)
6. [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
7. [Plugins/AgentBridge/README.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/README.md)

## 当前约定

- 历史阶段证据副本统一放在 `Docs/History/reports/AgentBridgeEvidence/`
- `ProjectState/Snapshots/` 继续只放 baseline / state snapshot，并按日期目录组织
- [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 与 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 当前登记为 `234` 条用例
