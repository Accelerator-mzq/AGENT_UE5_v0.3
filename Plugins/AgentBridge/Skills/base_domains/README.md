# Base Skill Domains

## 当前状态

Phase 7 起，`base_domains/` 不再是占位目录，而是最小可用的通用编译域注册中心。

## 当前落地范围

- `registry.py`：统一列出 10 个基础域
- `loader.py`：按域 ID 动态加载模块
- `qa_validation.py`：真实治理域，负责最小验证检查点与回归摘要
- `planning_governance.py`：真实治理域，负责恢复策略与最小 promotion 状态
- 其余 8 个域：提供可加载骨架与统一元数据

## 目录职责

- Base Skill Domains 负责跨项目、跨类型都可复用的通用骨架
- Genre Packs 负责类型化策略差异
- 本阶段不追求 10 个域全部深实现，只要求 registry、loader、真实治理域与可扩展骨架到位
