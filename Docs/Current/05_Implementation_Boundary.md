# 实施边界

> 阶段：Phase 7 正式开发期

## 允许改动

- `Docs/Current/*`
- 根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
- `Plugins/AgentBridge/Scripts/compiler/`
- `Plugins/AgentBridge/Scripts/orchestrator/`
- `Plugins/AgentBridge/Skills/base_domains/`
- `Plugins/AgentBridge/Skills/genre_packs/jrpg/`
- `Scripts/run_jrpg_turn_based_demo.py`
- 与 Phase 7 新功能直接相关的测试与文档

## 本期保持不动

- [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 当前 `206` 条总表
- [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 当前 `206` 条对齐口径
- 稳定的 `Bridge` 三通道主体
- 不必要的 C++ 大改动

## 设计原则

- 先做最小闭环，再做泛化
- 治理能力优先做“可表达、可验证、可审计”
- 第二个类型包只做一个：`JRPG Turn-Based`
