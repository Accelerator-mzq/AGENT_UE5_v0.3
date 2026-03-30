# 项目基线

> 文档版本：L1-Phase2-v1
> 基线截止时间：Phase 1 (MVP) 结束

## 已实装能力

### 插件核心

- AgentBridge C++ Editor Plugin（UEditorSubsystem）— 核心实现
- Bridge 三通道架构：通道 A（Python Editor Scripting）/ 通道 B（Remote Control API）/ 通道 C（C++ Plugin，推荐）
- 三层受控工具体系：L1 语义工具 > L2 编辑器服务工具 > L3 UI 工具

### L1 语义接口

写接口（4 个，FScopedTransaction）：
- `import_assets` / `create_blueprint_child` / `spawn_actor` / `set_actor_transform`

反馈接口（7 个 + 日志）：
- `get_current_project_state` / `list_level_actors` / `get_actor_state` / `get_actor_bounds` / `get_asset_metadata` / `get_dirty_assets` / `run_map_check` / `get_editor_log_tail`

### L3 UI 工具（Automation Driver）

- `click_detail_panel_button` / `type_in_detail_panel_field` / `drag_asset_to_viewport`
- L3→L1 交叉比对机制已实装

### L2 编辑器服务

- Commandlet 无头执行（-Spec / -RunTests / -Tool 三种模式）
- UAT BuildCookRun 构建自动化
- Gauntlet CI/CD 测试会话编排（AllTests / SmokeTests / SpecExecution）

### 验证体系

- L1 Simple Automation Test：11 个（Query 7 + Write 4）
- L3 UITool 测试：4 个
- L2 Automation Spec 闭环：5 个（ClosedLoop 3 + UITool 2）
- L3 Functional Testing：AFunctionalTest 子类 + FTEST_WarehouseDemo 地图
- Schema 校验：validate_examples.py --strict → 10/10 通过

### 数据契约

- JSON Schema 体系：6 common + 9 feedback + 1 write_feedback = 16 个 Schema
- 10 个 example JSON
- Spec 模板（YAML）：3 个

## 已完成任务

- task.md TASK 01–20 全部跑通

## 当前架构状态

- 引擎版本：UE5.5.4
- 插件版本：v0.3.0
- 项目结构：项目壳（Mvpv4TestCodex）+ AgentBridge 插件（父仓库内置目录）

## 已知限制

- 不支持 Blueprint 图深度重写、Niagara 图编辑、材质图深度修改
- 不支持多 Agent 并发、大规模无人监管场景改造
- Orchestrator 尚未实现
- Phase 2 反馈接口（get_material_assignment 等）待补充
- Agent→Editor 通信方案需选型落地（推荐 Remote Control API HTTP）
