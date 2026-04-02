# JRPG 回合制战斗 GDD v1

## 游戏类型
JRPG（Turn-Based RPG）

## 核心玩法
- 回合制战斗
- 主角与敌人交替行动
- 命令菜单：Attack、Skill、Defend
- 胜利条件：击败全部敌人

## 队伍配置
- Hero：HeroUnit_1
- Enemy：EnemyUnit_1

## 场景需求

### 战斗场景
- 类型：Battle Arena
- 总尺寸：600x600 cm
- 位置：世界原点 (0, 0, 0)

## 初始场景布局
- 战斗场地位于世界原点
- 主角位于左侧
- 敌人位于右侧
- 命令菜单锚点位于场地下方

## 技术需求
- UE5.5.4
- 使用 StaticMeshActor
- 不要求复杂 UI，只要求最小命令菜单锚点
- 不要求大地图、背包、任务系统
