---
name: skillforge-project-governance
description: Govern the SkillForge cross-platform skill repository, including business taxonomy, portable package structure, metadata, triggering quality, evidence boundaries, reusable resources, examples, acceptance tests, registry synchronization, and distribution checks. Use before creating, upgrading, reviewing, indexing, or packaging any SkillForge skill or when deciding where a new business capability belongs.
---

# SkillForge Project Governance

## Identity

- skill id: `skillforge-project-governance`
- display name: `SkillForge项目治理`
- type: `portable-governance-skill`
- scope: `cross-platform`

## What It Does

- 解释 `SkillForge` 项目的定位、目标与架构设计
- 约束后续 AI 如何创建、修改和分发业务 skill
- 提供统一的目录规则、文件职责与升级原则
- 要求每个 skill 具备真实专业判断链、证据边界和可执行验收，而不是只换名称的提示词模板

## When To Use

- 新 AI 接手这个项目时
- 在新增或重构业务 skill 之前
- 在不确定某个文件该放哪里、是否该做成 skill 包时
- 在准备把 skill 单独发给别人之前

## Read In Order

1. `skill.json`
2. `README.md`
3. `ARCHITECTURE.md`
4. `assets/project-rules.md`
5. `INVOCATION.md`
6. `platforms/<platform>.md`

## Package Guarantee

- 这是一个可独立分享的项目级 skill 文件夹
- 直接发送整个 `skillforge-project-governance/` 目录即可让其他 AI 理解项目规则
