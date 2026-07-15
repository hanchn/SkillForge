---
name: "skillforge-project-governance"
description: "Loads SkillForge project governance rules and architecture. Invoke when working inside this project, before editing structure, adding skills, or refactoring package layout."
---

# SkillForge Project Governance

This is the Trae bridge skill for the current `SkillForge` project.

## Purpose

- Make Trae read the project-level governance skill before making structural changes
- Ensure this project follows its own skill repository rules
- Keep business skills in business folders while only using `.trae` as the local bridge entry

## Read In Order

1. `/Users/yuanjing/Desktop/SkillForge/PROJECT_INDEX.md`
2. `/Users/yuanjing/Desktop/SkillForge/skillforge-project-governance/SKILL.md`
3. `/Users/yuanjing/Desktop/SkillForge/skillforge-project-governance/README.md`
4. `/Users/yuanjing/Desktop/SkillForge/skillforge-project-governance/ARCHITECTURE.md`
5. `/Users/yuanjing/Desktop/SkillForge/skillforge-project-governance/assets/project-rules.md`
6. `/Users/yuanjing/Desktop/SkillForge/registry/skills-index.json`

## Mandatory Rules

- Do not place business skills in `.trae`
- Treat `README.md` as documentation only
- Prefer the standard skill package template for new business skills
- Keep every business skill portable as a single folder when possible
- Update project-level registry and index files when adding new skills

## When To Use

- Before adding a new skill to this project
- Before moving or restructuring project folders
- Before changing skill package conventions
- When unsure whether a change is project-level or business-level
