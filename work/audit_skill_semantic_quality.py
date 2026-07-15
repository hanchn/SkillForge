#!/usr/bin/env python3
"""Produce a per-skill semantic and business-depth audit for the full portfolio."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CATEGORY_FOCUS = {
    "互联网研发": "真实仓库与版本、架构边界、测试、安全、发布回滚、Git 与生产权限",
    "渠道运营": "站点平台、商品事实、市场与关键词、库存利润、账户合规、上下架与复盘",
    "精准营销": "人群同意、实时市场、渠道创意、归因增量、预算止损、SEO/GEO 与触达",
    "创拍视觉": "商品真实性、创意策略、拍摄制作、人物版权、AIGC 血缘、标签与素材效果",
    "市场采购": "需求证据、选品门、样品、供应商、成本现金、质量合规、交付与退出",
    "仓储库存": "实物和系统时点、库存状态、入出库、补货分配、账实对账、安全与逆向",
    "客服售前": "商品事实、语言市场、承诺权限、知识、线索交接、质检与客户声音",
    "数据看板": "指标口径、数据质量、截止时间、可复算分析、因果边界、决策与监控",
    "法律政务": "司法辖区、当前官方规则、证据时效、非律师边界、整改与专业升级",
    "财务出纳": "主体期间币种、账实勾稽、职责分离、支付权限、税汇时效、审计证据",
    "人事招聘": "岗位理解、人才市场、工作地、隐私公平、招聘证据、劳动升级与员工体验",
    "基础工具": "跨部门复用边界、真实数据、平台连接器、凭证权限、回执关闭、周报口径与复盘效果",
    "project-root": "分类版本、生成可复现、用户改动保护、索引打包、审计与回滚",
}

COMMON_FILES = {
    "references/compliance-baseline.md", "references/scenario-playbook.md",
    "references/data-source-and-api-gate.md", "assets/data-source-intake-template.md",
    "assets/decision-record-template.md", "examples/README.md", "eval/acceptance.md",
}


def bullets(text: str, heading: str) -> list[str]:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text)
    if not match:
        return []
    return [line[2:].strip() for line in match.group(1).splitlines() if line.startswith("- ")]


def audit(root: Path = ROOT) -> dict:
    registry = json.loads((root / "registry/skills-index.json").read_text(encoding="utf-8"))
    classifications = {item["name"]: item.get("classification", {}) for item in registry["skills"]}
    results = []
    for meta_path in sorted(root.rglob("skill.json")):
        rel = meta_path.relative_to(root)
        if rel.parts[0] in {"templates", "work"}:
            continue
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        base = meta_path.parent
        skill = (base / "SKILL.md").read_text(encoding="utf-8")
        readme = (base / "README.md").read_text(encoding="utf-8") if (base / "README.md").exists() else ""
        eval_text = (base / "eval/acceptance.md").read_text(encoding="utf-8")
        scenarios = bullets(readme, "适用场景")
        outputs = data.get("outputs", [])
        checklist_count = len(re.findall(r"(?m)^- \[ \]", eval_text))
        package_files = set(data.get("distribution", {}).get("package_files", []))
        specialized = [
            item for item in package_files
            if item.startswith(("references/", "assets/", "scripts/")) and item not in COMMON_FILES
        ]
        kind = classifications.get(data["name"], {}).get("label", "专项能力")
        checks = {
            "完整结果": (
                len(outputs) >= 3
                and (len(data.get("description", "")) >= 35 or "## Output contract" in skill)
            ) or (len(outputs) >= 2 and len(re.findall(r"(?m)^\d+\. ", skill)) >= 8 and "## Output contract" in skill),
            "多场景": len(scenarios) >= 3 or len(re.findall(r"场景|scenario", skill, re.I)) >= 3,
            "专业流程": len(re.findall(r"(?m)^\d+\. ", skill)) >= 5,
            "上下游决策": all(term in skill + readme for term in ["上游", "下游"]) and any(term in skill for term in ["决策", "tradeoff", "取舍"]),
            "异常恢复": any(term in skill for term in ["异常", "失败", "conflict", "冲突"]) and any(term in skill for term in ["回滚", "恢复", "rollback", "recovery"]),
            "实时证据": "Evidence freshness gate" in skill or all(term in skill + readme for term in ["来源", "版本"]),
            "使用者输入": (
                any(term in skill + eval_text for term in ["询问使用者", "现有数据", "用户提供", "使用者优先", "确认范围", "User intake gate"])
                and "## Data and compliant API intake gate" in skill
                and "references/data-source-and-api-gate.md" in package_files
                and "assets/data-source-intake-template.md" in package_files
            ),
            "专项资源": len(specialized) >= 2,
            "专项验收": checklist_count >= 8 and any(str(output) in eval_text for output in outputs[:3]),
            "合规权限": "references/compliance-baseline.md" in package_files and bool(data.get("compliance")),
        }
        failed = [name for name, passed in checks.items() if not passed]
        score = sum(checks.values()) * 10
        status = "通过" if not failed else "需增强" if score >= 70 else "需重构"
        top = (data.get("category_path") or ["project-root"])[0]
        results.append({
            "name": data["name"], "display_name": data["display_name"], "version": data["version"],
            "category": top, "kind": kind, "score": score, "status": status,
            "failed": failed, "focus": CATEGORY_FOCUS.get(top, "完整业务结果与公司适配"),
            "package_root": base.relative_to(root).as_posix(),
        })
    results.sort(key=lambda x: (x["category"], x["status"] != "需重构", x["status"] != "需增强", x["display_name"]))
    status_counts = Counter(item["status"] for item in results)
    category_counts = defaultdict(Counter)
    for item in results:
        category_counts[item["category"]][item["status"]] += 1
    payload = {"skills": len(results), "status": dict(status_counts), "results": results}
    (root / "registry/skill-full-audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# SkillForge 全量 Skill 语义审计", "",
        "本审计逐项检查完整业务结果、多场景、专业流程、上下游决策、异常恢复、实时证据、使用者输入、专项资源、专项验收和合规权限。十项全部通过才判定为通过；它比结构审计更严格，但仍需通过真实任务持续补充失败样本。", "",
        "## 总览", "",
        f"- 正式 Skill：{len(results)}",
        f"- 通过：{status_counts['通过']}；需增强：{status_counts['需增强']}；需重构：{status_counts['需重构']}", "",
        "## 分类结果", "",
        "| 分类 | 数量 | 通过 | 需增强 | 需重构 | 专业抽检重点 |", "|---|---:|---:|---:|---:|---|",
    ]
    for category in sorted(category_counts):
        counts = category_counts[category]
        total = sum(counts.values())
        lines.append(f"| {category} | {total} | {counts['通过']} | {counts['需增强']} | {counts['需重构']} | {CATEGORY_FOCUS.get(category, '')} |")
    lines.extend(["", "## 逐项结果", ""])
    current = None
    for item in results:
        if item["category"] != current:
            current = item["category"]
            lines.extend([f"### {current}", "", "| Skill | 类型 | 版本 | 分数 | 结论 | 待补项 |", "|---|---|---:|---:|---|---|"])
        failed = "、".join(item["failed"]) or "无"
        lines.append(f"| {item['display_name']} | {item['kind']} | {item['version']} | {item['score']} | {item['status']} | {failed} |")
    lines.extend(["", "## 审计边界", "", "- 分数只代表 Skill 包当前能否引导复杂任务，不代表某次实际输出一定正确。", "- 法律、财务、人事、平台规则、市场、Rank、价格和软件版本必须在调用时刷新当前证据。", "- 角色与周报的共用结构是刻意保留的，但业务指标、风险、决策和交付必须使用各角色专属维度。", "- 真实调用发现的新场景、失败样本和公司制度必须回写 Skill 并升级版本。", ""])
    (root / "SKILL_FULL_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


if __name__ == "__main__":
    result = audit(ROOT)
    print(f"Full-audited {result['skills']} skills: {result['status']}")
