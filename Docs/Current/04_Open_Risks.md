# 当前风险

> 文档版本：L1-Phase8-v3

## 已关闭风险

- Phase 7 治理闭环风险已关闭。
- JRPG 第二类型包复用风险已关闭。
- Phase 8 运行时 HUD 可见性与输入焦点问题已定位并修复，相关证据见 [phase8_task06_validation_2026-04-05_230956.json](/D:/UnrealProjects/Mvpv4TestCodex/ProjectState/Reports/2026-04-05/phase8_task06_validation_2026-04-05_230956.json)。
- Phase 8 的运行时冒烟验证缺口已在本阶段通过自动化补强和人工冒烟补齐。

## 结转到下一阶段的风险

| 风险 | 严重度 | 说明 | 下一步 |
|------|--------|------|----------|
| MCP Server 仍为占位骨架 | 中 | Phase 8 只落地了目录、工具定义和基础骨架，尚未形成完整可执行服务 | 进入下一阶段后评估最小可用实现 |
| 联网多人复制改造量较大 | 中 | 若从 Phase 1 扩展到网络多人，需要重做 `GameMode / GameState / PlayerState` 的复制策略 | Phase 9 立项时单独评估 |
| 第三个 genre pack 的通用性尚未验证 | 低中 | 当前只验证到 `boardgame` 与 `jrpg` 两类 | 后续新增类型包时继续验证 |
| Phase 8 运行时防回归规则仍需制度化 | 中 | 复盘结论已经形成，但还需要在后续阶段持续贯彻 | 延续 [08_Phase8_Retrospective_And_Phase9_Checklist.md](/D:/UnrealProjects/Mvpv4TestCodex/Docs/Current/08_Phase8_Retrospective_And_Phase9_Checklist.md) |
