# Git 安全工作流管理器

先读取仓库证据，再用可恢复的方式完成 Git 流转并保护用户现有改动。

## 典型任务

- 为当前改动建立合规 feature 分支并准备提交。
- 检查 test 到 pre 的实际提交范围和发布风险。
- 解释分支分叉并给出不会丢改动的整合方案。

## 交付物

- git_state_and_plan.md
- executed_ref_summary

## 硬边界

- 不得未经授权丢弃工作或重写共享历史
- 不得暂存或提交无关用户改动
- 不得假设分支名、远端或发布流存在

## 读取顺序

1. SKILL.md
2. SKILL.md 指定的 references 与 assets
3. INVOCATION.md
4. eval/acceptance.md

整个目录可以独立分发；README 只承担人类说明，不是 skill 执行入口。
