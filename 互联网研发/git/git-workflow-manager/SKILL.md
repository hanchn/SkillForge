# Git分支流转与合并规范技能

## Identity

- skill id: `git-workflow-manager`
- display name: `Git分支流转与合并规范技能`
- type: `portable-business-skill`
- scope: `cross-platform`

## What It Does

- 解释并执行标准的分支命名规范（如 `feature/日期/功能`，`fix/日期/功能`）
- 指导开发、测试、预发到生产的分支合并路径
- 防止错误的分支合并（如 test 直接合 master）

## When To Use

- 研发团队需要统一 Git 分支管理与代码合并流转
- 遇到分支冲突或不知道当前改动该切什么分支时
- 准备发布版本，需要明确从开发到上线的合并步骤

## Read In Order

1. `skill.json`
2. `INVOCATION.md`
3. `BASE_PROMPT.md`
4. `platforms/<platform>.md`

## Package Guarantee

- 这是一个可独立分享的 skill 文件夹
- 直接发送整个 `git-workflow-manager/` 目录即可复用
- `README.md` 只是说明文档，不是 skill 本体
