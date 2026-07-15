---
name: skillforge-project-governance
description: Govern the SkillForge cross-platform skill repository, including business taxonomy, portable package structure, metadata, triggering quality, evidence boundaries, reusable resources, examples, acceptance tests, registry synchronization, and distribution checks. Use before creating, upgrading, reviewing, indexing, or packaging any SkillForge skill or when deciding where a new business capability belongs.
---

# SkillForge Project Governance

## Compliance gate

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

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
- 以“一个完整业务结果”为默认粒度，防止把同一工作流拆成大量动作级 Skill
- 要求 Skill 优先读取 `公司上下文/` 中的贵司事实，并围绕贵司系统与部门边界执行

## Skill Granularity Rules

- 一个 Skill 能从输入完成到可验收结果时，不再按步骤、工具、消息模板或单一动作拆分。
- 只有专业知识、触发场景、风险边界、输入输出和独立复用价值均明显不同，才建立专项 Skill。
- 主角色 Skill 负责目标、取舍、编排和验收；专项 Skill 负责完整专业结果，不按岗位人数机械建 Skill。
- 新增前先检查现有 Skill 能否升级覆盖；默认升级，例外才新增。

## Company Customization

- 在仓库内执行时先读 `公司上下文/company-profile.yaml` 和 `公司上下文/README.md`。
- 已确认公司事实优先于通用行业假设；未知内容明确询问或标记，不得虚构。
- 系统工作默认使用贵司 OMS、IMS、OFS、CMS、WMS、TMS、CRM、PLM 的业务语言，并先确认实际缩写口径和 source of truth。

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
