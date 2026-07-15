#!/usr/bin/env python3
"""Rebuild SkillForge registries and the AI-facing project index from skill.json files."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "4.0.0"


def skill_records():
    records = []
    for meta_path in ROOT.rglob("skill.json"):
        rel = meta_path.relative_to(ROOT)
        if rel.parts[0] in {"templates", ".git", "work"}:
            continue
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        package_root = meta_path.parent.relative_to(ROOT).as_posix()
        data["package_root"] = package_root
        records.append(data)
    records.sort(key=lambda x: (x.get("category_path", []), x["name"]))
    return records


skills = skill_records()
registry_skills = []
project_skills = []
for item in skills:
    registry = {
        "name": item["name"],
        "display_name": item["display_name"],
        "description": item["description"],
        "category_path": item.get("category_path", []),
        "package_root": item["package_root"],
        "portable": item["portable"],
        "supported_platforms": item["supported_platforms"],
        "entrypoint": item["entrypoint"],
        "search_keywords": item.get("search_keywords", []),
    }
    if item["name"] == "skillforge-project-governance":
        registry["dashboard_visible"] = False
    registry_skills.append(registry)
    project_skills.append({
        "name": item["name"],
        "display_name": item["display_name"],
        "package_root": item["package_root"],
        "entrypoint": item["entrypoint"],
        "type": item["type"],
        "search_keywords": item.get("search_keywords", []),
    })

(ROOT / "registry/skills-index.json").write_text(json.dumps({
    "project": "SkillForge", "version": VERSION, "skills": registry_skills,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

(ROOT / "registry/project-index.json").write_text(json.dumps({
    "project": "SkillForge", "version": VERSION,
    "entry_docs": {
        "readme": "README.md", "project_index": "PROJECT_INDEX.md",
        "skills_dashboard": "skills-dashboard/index.html",
        "governance_skill": "skillforge-project-governance/SKILL.md",
        "skills_registry": "registry/skills-index.json", "schema": "schemas/skill.schema.json",
    },
    "layers": {
        "project_governance": ["README.md", "PROJECT_INDEX.md", "skills-dashboard", "skillforge-project-governance", "schemas", "templates", "registry", "platforms"],
        "business_browse": ["渠道运营", "精准营销", "互联网研发", "法律政务", "数据", "项目管理", "work"],
    },
    "skills": project_skills,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "# SkillForge Project Index", "",
    "这个文件给 AI 提供全局导航、分类定位和技能检索入口。", "",
    "## First Read", "",
    "- 项目总说明：README.md",
    "- 项目治理：skillforge-project-governance/SKILL.md",
    "- 全局注册表：registry/skills-index.json",
    "- 元数据规范：schemas/skill.schema.json",
    "- 标准模板：templates/standard-skill-package/",
    "- 可视化管理：skills-dashboard/",
    "- 前后端架构地图：互联网研发/ARCHITECTURE_SKILLS_MAP.md",
    "- 渠道运营地图：渠道运营/CHANNEL_OPERATIONS_SKILLS_MAP.md",
    "- 精准营销地图：精准营销/PRECISION_MARKETING_SKILLS_MAP.md",
    "- 业务数据分析地图：数据/BUSINESS_ANALYTICS_SKILLS_MAP.md",
    "- 企业系统产品架构：互联网研发/产品/系统产品架构/SYSTEM_PRODUCT_ARCHITECTURE_MAP.md",
    "", "## Search Strategy", "",
    "1. 新建、升级或打包 Skill 前先读项目治理 Skill。",
    "2. 从 registry/skills-index.json 按 name、category_path 或 search_keywords 定位。",
    "3. 先用能力地图选择主 Skill，再组合必要的专项 Skill。",
    "4. 进入技能包后先读 README.md 理解中文产品能力和版本，再读 SKILL.md 执行。",
    "5. 按 SKILL.md 加载 references 与 assets，最后使用 eval/acceptance.md 验收。",
    "", "## Registered Skills", "",
]
last_category = None
for item in registry_skills:
    top = item["category_path"][0] if item["category_path"] else "未分类"
    if top != last_category:
        lines.extend([f"### {top}", ""])
        last_category = top
    visible = "；前端隐藏" if item.get("dashboard_visible") is False else ""
    category = " / ".join(item["category_path"]) or "未分类"
    lines.extend([
        f"- **{item['display_name']}**（`{item['name']}`）{visible}",
        f"  - 路径：`{item['package_root']}/`",
        f"  - 分类：{category}",
        f"  - 用途：{item['description']}",
    ])

(ROOT / "PROJECT_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Indexed {len(skills)} skills; dashboard visible {sum(x.get('dashboard_visible', True) for x in registry_skills)}")
