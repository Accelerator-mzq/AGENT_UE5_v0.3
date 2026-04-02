# 当前阶段目标

> 阶段：Phase 7 — 正式开发期（治理闭环 + JRPG 第二类型包）

## 本期目标

1. 把文档和任务入口从“准备期”切换到“正式开发期”
2. 落地最小治理闭环：
   - Validation Inserter
   - Recovery Planner
   - Regression Summary
   - Freeze / Snapshot Manifest
   - Minimal Promotion
3. 把 `Skills/base_domains/` 从占位目录升级为真实 registry + loader
4. 落地第二个类型包 `JRPG Turn-Based`
5. 给 Phase 7 建立独立测试入口，但不提前改总表

## 成功标准

- `Docs/Current/*` 与入口文档不再出现“Phase 7 准备期”口径
- 根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md) 按正式开发期结构重建
- `run_plan` 支持 `validation_checkpoints[]` 与 `recovery_policy_ref`
- 执行报告支持 `regression_summary`、`snapshot_ref`、`promotion_status`
- `base_domains` 可注册 10 个域，其中 `qa_validation` 与 `planning_governance` 为真实实现
- `jrpg` pack 能从 GDD 生成最小可玩的结构化闭环，并支持 Greenfield / Brownfield 路径

## 本期不做

- 不在阶段中途改 [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md)
- 不在阶段中途改 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 的 `206` 条总表口径
- 不做完整 Promotion 流水线
- 不做像素级回归对比
