# AGENTS.md — Mvpv4TestCodex 项目

> 目标引擎版本：UE5.5.4 | 适用范围：本项目根目录与项目壳层面的 Agent 协作规则

## 1. 通用规则入口

本项目使用 `AgentBridge` 插件作为受控编排层。凡是调用桥接工具、编写 Spec、执行写后读回或使用 L1/L2/L3 工具时，Agent 必须先遵守插件通用规则：

→ `Plugins/AgentBridge/AGENTS.md`

## 2. 本项目特定规则

### 2.1 项目定位

本仓库不是普通游戏项目，而是一个用于承载和验证 `AgentBridge` 插件的 UE5.5.4 项目壳。项目根目录负责：

- `Mvpv4TestCodex.uproject` 与项目级配置
- `Config/`、`Content/`、`Source/` 等宿主工程内容
- `.vscode/tasks.json` 等项目级启动与验证入口

### 2.2 默认修改范围

若任务未特别说明，优先在以下范围内工作：

- `Plugins/AgentBridge/`
- `Plugins/AgentBridge/AgentBridgeTests/`
- 项目级启动与验证脚本
- 测试地图与验证资源（如 `/Game/Tests`、`/Temp`）

不要无故扩散到无关游戏内容。

### 2.3 L3 UI 工具在本项目中允许使用

本项目保留 `L3 UI` 工具用于验证闭环、功能测试和 Task19/Task20 相关回归，但仍必须遵守插件级规则：

- 先证明确实没有更合适的 L1 路径
- 执行后必须做 L3→L1 交叉比对
- 不得用来做高风险不可逆修改

### 2.4 证据与报告目录

本项目新增的验证证据默认放在：

- `Plugins/AgentBridge/reports/...`

如果某个任务已有固定产物路径，则遵循该任务约定。

### 2.5 任务清单入口

当前任务清单主文件位于：

- `task.md`

项目级 Agent 在处理任务时，应把它视为当前项目的执行清单来源。

## 3. 项目协作约定

### 3.1 PowerShell 编码

为避免中文乱码，读取和写入文本时必须显式声明 UTF-8 编码：

- `Get-Content -Raw -Encoding UTF8`
- `Set-Content -Encoding UTF8`
- `Add-Content -Encoding UTF8`

### 3.2 文档引用顺序

处理本项目任务时，推荐优先阅读：

1. 本文件 `AGENTS.md`
2. `Plugins/AgentBridge/AGENTS.md`
3. `README.md`
4. `Plugins/AgentBridge/README.md`
5. `task.md`
6. 当前任务涉及的 `Docs/`、`Schemas/`、`reports/`

### 3.3 普通打开项目与测试打开项目要区分

- 普通打开 `Mvpv4TestCodex.uproject` 时，不应把 `AgentBridgeTests` 作为默认必需插件
- 运行自动化测试、Gauntlet、命令行验证时，再显式启用 `AgentBridgeTests`

### 3.4 VS Code 文件引用格式

- Agent 在聊天面板中引用本项目文件时，应优先使用 VS Code 可直接跳转的 Markdown 链接格式
- 链接目标必须使用“以 `/` 开头的 Windows 绝对路径 + `#L行号`”形式，例如：`[AGENTS.md (line 44)](/D:/UnrealProjects/Mvpv4TestCodex/AGENTS.md#L44)`
- 不要使用不带前导 `/` 的 `D:/...` 链接，也不要把普通网页链接样式当作文件跳转链接
- 如果项目根目录名称或盘符发生变化，应按当前实际绝对路径重新生成上述格式的链接

## 4. 当前文档分层

本项目的四份入口文档分工如下：

- 项目级规则：`AGENTS.md`
- 项目级说明：`README.md`
- 插件级规则：`Plugins/AgentBridge/AGENTS.md`
- 插件级说明：`Plugins/AgentBridge/README.md`

如果以后把 `AgentBridge` 拷贝到其他项目，应优先保留插件目录下的两份文档；项目根目录两份文档只对当前仓库生效。

