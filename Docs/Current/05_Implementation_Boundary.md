# 实施边界

> 阶段：Phase 8 — Skill-First Compiler Reset + MonopolyGame 垂直切片（归档保留）

## 允许改动

- 项目层 `Source/Mvpv4TestCodex/` 下新增 C++ 文件（11 对 .h/.cpp）
- 插件层 `Plugins/AgentBridge/Schemas/` 下新增的 6 个 Schema
- 插件层 `Plugins/AgentBridge/Compiler/` 下新增的 5 段 Python 骨架
- 插件层 `Plugins/AgentBridge/SkillTemplates/` 下新增的 Skill Template Pack
- 插件层 `Plugins/AgentBridge/MCP/` 下新增的 MCP Server
- 项目层 `ProjectState/phase8/` 下的 Compiler 产物
- 项目层 `Docs/History/Proposals/` 下的设计文档和交接文档
- 项目层 `Docs/Current/*` 的阶段口径维护
- 根目录 `task.md` 的任务更新

## 不允许改动

- `Plugins/AgentBridge/Source/` 下已稳定的 C++ 核心
- `Plugins/AgentBridge/Scripts/bridge/` 下已稳定的 Bridge 客户端
- `Plugins/AgentBridge/Scripts/orchestrator/` 下已稳定的 Orchestrator 核心（orchestrator.py / plan_generator.py / verifier.py / report_generator.py / spec_reader.py）
- `Plugins/AgentBridge/AgentBridgeTests/` 下所有测试文件
- `Plugins/AgentBridge/Schemas/common/`、`feedback/`、`write_feedback/` 下已稳定的 Schema

## Phase 8 最终固定口径

- [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 与 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 当前登记为 `234` 条，其中原 `230` 条地基保留，Phase 8 新增 `E2E-37 ~ E2E-40` 已补录。
- MonopolyGame 是唯一垂直切片，不同时引入其他游戏类型。
- Build IR 14 步按 6 Batch 顺序执行，不跳步。
