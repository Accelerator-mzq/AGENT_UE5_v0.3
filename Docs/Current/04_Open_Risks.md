# 当前风险

> 文档版本：L1-Phase7-v1

## 风险 1：治理闭环新增字段破坏现有链路

- 风险：`run_plan` / `execution_report` 新字段若直接侵入旧逻辑，可能破坏 Phase 4~6 回归
- 缓解：新增字段只做增量扩展，保持旧字段兼容

## 风险 2：第二个类型包只是文档存在，未形成真实编译路径

- 风险：若只新增 `manifest` 而不接入 generation / review / delta，Phase 7 会停留在样板层
- 缓解：`jrpg` pack 必须接到 Greenfield / Brownfield 最小闭环

## 风险 3：Base Skill Domains 继续停留在占位目录

- 风险：Phase 7 无法证明“治理闭环 + 多类型扩展”具备可复用骨架
- 缓解：至少实装 registry / loader，并让两个真实域参与治理逻辑

## 风险 4：过早扩写总表

- 风险：若中途把新编号写进总表，会再次打破 [SystemTestCases.md](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/SystemTestCases.md) 与 [run_system_tests.py](/D:/UnrealProjects/Mvpv4TestCodex/Plugins/AgentBridge/Tests/run_system_tests.py) 的对齐
- 缓解：Phase 7 新编号只写在根目录 [task.md](/D:/UnrealProjects/Mvpv4TestCodex/task.md)
