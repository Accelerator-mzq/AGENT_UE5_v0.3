# 项目基线

> 文档版本：L1-Phase8-v2

## 1. 当前事实

- `Phase 6` 已完成并归档，历史任务见 [task4_phase6.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task4_phase6.md)。
- `Phase 7` 已完成并归档，历史任务见 [task6_phase7.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/History/Tasks/task6_phase7.md)。
- `Phase 8` 已完成并进入收尾状态，收尾总览见 [10_Phase8_Closeout.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/10_Phase8_Closeout.md)。
- 插件层系统总表与系统测试入口当前统一登记为 `234` 条用例。

## 2. Phase 8 已产出事实

### 设计文档
- DD-1：`Docs/History/Proposals/Phase8_DD1_Schema_and_Interface_Spec.md`（Schema + Compiler 接口规约）
- DD-3：`Docs/History/Proposals/Phase8_DD3_Lowering_Map_and_CPP_Design.md`（C++ 类设计 + Build Step 映射）
- 交接文档：`Docs/History/Proposals/Phase8_M3_Handover_to_Execution_Agent.md`（含 UMG 布局方案）
- 统一方案：`Docs/History/Proposals/Phase8_Plan_Original.md`

### 新增 Schema（6 个）
- `Plugins/AgentBridge/Schemas/{gdd_projection,planner_output,skill_fragment,cross_review_report,build_ir,reviewed_handoff_v2}.schema.json`

### 新增 Compiler 骨架（5 段）
- `Plugins/AgentBridge/Compiler/{intake,planner,skill_runtime,cross_review,lowering}/`

### 新增 Skill Template Pack（6 套 × 6 文件 = 36 文件）
- `Plugins/AgentBridge/SkillTemplates/genre_packs/boardgame/monopoly_like/`

### 新增 MCP Server（6 文件）
- `Plugins/AgentBridge/MCP/{server,tool_definitions,naming,py_channel,rc_channel}.py` + `README.md`

### Main Chain 产物（11 个 JSON）
- `ProjectState/phase8/{gdd_projection,planner_output,cross_review_report,build_ir,reviewed_handoff_v2}.json`
- `ProjectState/phase8/skill_fragments/skill-{board,tile-event,turn,economy,jail,ui}.json`

### 项目层运行时与验证产物
- Monopoly 垂直切片运行时代码、地图和 UI 壳资产已落地在项目层。
- `TASK 06` 自动化验证脚本、UE Automation 测试和人工冒烟模板已补齐。
- `Stage 9 / E2E` 已新增 `E2E-37 ~ E2E-40`。

## 3. 最终验证事实

- `TASK 06` 最终通过，见 [phase8_task06_validation_2026-04-05_230956.json](/D:/UnrealProjects/Mvpv4TestCodex/ProjectState/Reports/2026-04-05/phase8_task06_validation_2026-04-05_230956.json)。
- 人工冒烟已留证，见 [phase8_manual_smoke_report_2026-04-05_210434.md](/D:/UnrealProjects/Mvpv4TestCodex/ProjectState/Reports/2026-04-05/phase8_manual_smoke_report_2026-04-05_210434.md)。
- `Stage 9 / E2E` 已通过 `40/40`，见 [system_test_report_2026-04-05_230956.json](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/reports/2026-04-05/system_test_report_2026-04-05_230956.json)。
- 当前测试总表为 `234` 条，见 [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md)。

## 4. 已确认的项目真相

- Phase 6/7 的 `preview_static` 与 `runtime_playable` 仍是回归基线。
- Phase 8 引入 Skill-First 6 阶段主链，替代旧的 intake/routing/generation 链路。
- Reviewed Handoff v2 以 `reviewed_dynamic_spec_tree` 替代 v1 的 `scene_spec.actors` 中心。
- MonopolyGame 是 Phase 8 唯一垂直切片测试案例。
