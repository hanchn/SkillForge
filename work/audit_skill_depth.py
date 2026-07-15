#!/usr/bin/env python3
"""Audit formal skills against SkillForge's complete-business-result depth standard."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def audit_one(meta_path: Path) -> dict:
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    base = meta_path.parent
    skill = (base / "SKILL.md").read_text(encoding="utf-8")
    readme = (base / "README.md").read_text(encoding="utf-8") if (base / "README.md").exists() else ""
    checks = {
        "business_scope": len(data.get("description", "")) >= 40 and "##" in skill,
        "workflow": len(re.findall(r"(?m)^\d+\. ", skill)) >= 5,
        "decision_dimensions": len(data.get("search_keywords", [])) >= 3 or "decision" in skill.lower() or "决策" in skill,
        "boundaries": bool(data.get("constraints")) and any(x in skill for x in ["Guardrails", "边界", "Safety"]),
        "evidence": any(x in skill for x in ["证据", "evidence", "source of truth", "来源"]),
        "exceptions": any(x in skill for x in ["异常", "冲突", "失败", "exception", "conflict"]),
        "recovery": any(x in skill for x in ["回滚", "恢复", "rollback", "recovery"]),
        "upstream_downstream": any(x in skill + readme for x in ["上游", "下游", "交接", "consumer", "接口"]),
        "scenario_depth": (base / "references/scenario-playbook.md").exists() or len(re.findall(r"场景|scenario", skill + readme, re.I)) >= 3,
        "decision_record": (base / "assets/decision-record-template.md").exists() or "方案比较" in skill + readme,
        "compliance": (base / "references/compliance-baseline.md").exists() and bool(data.get("compliance")),
        "acceptance": (base / "eval/acceptance.md").exists() and any(x in skill + readme for x in ["验收", "acceptance", "验证"]),
    }
    score = sum(checks.values())
    grade = "A" if score >= 11 else "B" if score >= 9 else "C" if score >= 7 else "D"
    missing = [name for name, passed in checks.items() if not passed]
    return {
        "name": data["name"],
        "display_name": data["display_name"],
        "version": data["version"],
        "category_path": data.get("category_path", []),
        "package_root": base.relative_to(ROOT).as_posix(),
        "score": score,
        "grade": grade,
        "missing": missing,
    }


def audit_depth(root: Path = ROOT) -> dict:
    results = []
    for path in sorted(root.rglob("skill.json")):
        rel = path.relative_to(root)
        if rel.parts[0] in {"templates", "work"}:
            continue
        results.append(audit_one(path))
    results.sort(key=lambda x: (x["grade"], -x["score"], x["category_path"], x["name"]))
    grades = Counter(item["grade"] for item in results)
    payload = {
        "standard": "SKILL_DEPTH_STANDARD.md",
        "skills": len(results),
        "grades": dict(sorted(grades.items())),
        "results": results,
    }
    (root / "registry/skill-depth-audit.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# SkillForge Skill 深度审计", "",
        "审计标准见 `SKILL_DEPTH_STANDARD.md`。等级用于定位仍需深化的能力，不等于业务绩效或正式合规结论。", "",
        "## 总览", "",
        f"- 正式 Skill：{len(results)}",
        f"- A：{grades.get('A', 0)}；B：{grades.get('B', 0)}；C：{grades.get('C', 0)}；D：{grades.get('D', 0)}", "",
        "## B/C/D 待深化项", "",
    ]
    pending = [item for item in results if item["grade"] != "A"]
    if not pending:
        lines.append("- 当前结构化检查均达到 A；仍需在真实调用中持续补充失败样本和公司规则。")
    else:
        for item in pending:
            missing = "、".join(item["missing"]) or "无"
            lines.append(f"- **{item['display_name']}**（{item['grade']}，{item['score']}/12）：缺少 {missing}；`{item['package_root']}`")
    lines.extend(["", "## 说明", "", "- 自动审计检查结构与执行门禁，不能替代业务专家对内容正确性的抽样评审。", "- 新 Skill 不得仅通过堆字数提分；每个场景、异常和交付必须与具体业务对象相关。", ""])
    (root / "SKILL_DEPTH_AUDIT.md").write_text("\n".join(lines), encoding="utf-8")
    return payload


if __name__ == "__main__":
    result = audit_depth(ROOT)
    print(f"Depth-audited {result['skills']} skills: {result['grades']}")
