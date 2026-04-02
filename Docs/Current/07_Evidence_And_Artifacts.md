# 证据与产物

> 文档版本：L1-Phase7-v1

## 1. 报告目录

- 项目级报告：`ProjectState/Reports/YYYY-MM-DD/`
- 插件级报告：`Plugins/AgentBridge/reports/YYYY-MM-DD/`

所有新生成的报告默认按日期分层，不再直接平铺到根目录。

## 2. Evidence 目录

- 项目级真实截图与验收证据继续放在 `ProjectState/Evidence/`
- 历史阶段证据归档副本继续放在 `Docs/History/reports/`

## 3. Snapshot 目录

- Snapshot 默认写到 `ProjectState/Snapshots/YYYY-MM-DD/`
- Phase 7 起，最小 snapshot manifest 至少包含：
  - `baseline_ref`
  - `digest`
  - `source_report`
  - `created_at`

## 4. Phase 7 当前约束

- 本阶段新增测试记录先写入项目级报告目录
- 本阶段新增用例编号只在根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md) 中维护
- 阶段归档时，再把通过用例补录进总表
