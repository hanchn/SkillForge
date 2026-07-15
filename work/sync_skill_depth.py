#!/usr/bin/env python3
"""Add complete-business-result depth resources to legacy formal skills."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- generated-by: sync-skill-depth -->"


def list_section(text: str, heading: str) -> list[str]:
    match = re.search(rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text)
    if not match:
        return []
    return [line[2:].strip() for line in match.group(1).splitlines() if line.startswith("- ")]


def scenario_values(data: dict, readme: str) -> list[str]:
    values = list_section(readme, "适用场景")
    if values:
        return values[:6]
    keywords = [value for value in data.get("search_keywords", []) if isinstance(value, str) and len(value) >= 4]
    return keywords[:4] or [data.get("description", "完成该 Skill 的核心业务任务")]


def write_generated(path: Path, content: str) -> None:
    if not path.exists() or MARKER in path.read_text(encoding="utf-8"):
        path.parent.mkdir(exist_ok=True)
        path.write_text(MARKER + "\n" + content, encoding="utf-8")


def inject_skill(text: str) -> str:
    load_lines = (
        "- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。\n"
        "- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。"
    )
    if "references/scenario-playbook.md" not in text:
        marker = "## Load resources\n"
        if marker in text:
            text = text.replace(marker, marker + "\n" + load_lines + "\n", 1)
        else:
            first_heading = next((line for line in text.splitlines() if line.startswith("# ")), "")
            if first_heading:
                text = text.replace(first_heading, first_heading + "\n\n## Load resources\n\n" + load_lines, 1)
    if "## Complete-business-result depth gate" not in text and "## Depth requirements" not in text:
        block = """

## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。
"""
        marker = "## Output contract"
        text = text.replace(marker, block + "\n" + marker, 1) if marker in text else text + block
    return text


def inject_readme(text: str) -> str:
    if "## 深度执行标准" not in text:
        block = """## 深度执行标准

- 覆盖完整业务理解、主场景与相邻变体、上下游、方案取舍、工具失败、异常、交付、验收和复盘。
- 复杂任务先读 `references/scenario-playbook.md`；存在决策或审批时使用 `assets/decision-record-template.md`。
- 不以篇幅代替深度，每项判断必须关联真实对象、证据、责任和结果。

"""
        marker = "## 技能包组成"
        text = text.replace(marker, block + marker, 1) if marker in text else text + "\n\n" + block
    return text


def playbook(data: dict, scenarios: list[str]) -> str:
    outputs = "、".join(data.get("outputs", [])) or "可验收业务交付物"
    required = "、".join(data.get("inputs", {}).get("required", [])) or "业务目标与真实证据"
    optional = "、".join(data.get("inputs", {}).get("optional", [])) or "历史、系统和约束资料"
    constraints = "；".join(data.get("constraints", [])) or "遵守任务边界与授权"
    sections = []
    for index, scenario in enumerate(scenarios, 1):
        sections.append(f"""## 场景 {index}：{scenario}

- 业务理解：解释本场景的对象、术语、启动原因、结果使用者和错误后果。
- 输入与补证：必需 {required}；建议补充 {optional}；来源、日期、版本和可信度必须记录。
- 上下游：确认输入 owner、下游消费者、系统事实源、审批人、执行人和交接 SLA。
- 决策：比较维持现状、推荐方案和低风险备选，记录适用条件、反证、成本、风险与可逆性。
- 异常：覆盖缺数据、口径冲突、权限不足、依赖失败、超时、部分成功、人工升级、补偿和回滚。
- 完成：交付 {outputs}，并附验收证据、责任人、截止、停止条件和复盘时间。
""")
    return f"""# {data['display_name']}场景作战手册

本文件用于把现有专业流程扩展为完整业务结果。必须选择一个主场景，并说明是否叠加其他场景。

""" + "\n".join(sections) + f"""
## 不可突破的边界

{constraints}

## 跨场景检查

- 人员：谁提出、谁提供事实、谁决策、谁执行、谁验收、谁承担失败后果。
- 系统：source of truth、状态、版本、权限、写回、幂等、对账、日志和留存。
- 经营：收入、利润、现金、客户、质量、时效、合规和可逆性之间的取舍。
- 学习：领先指标、结果指标、护栏指标、失败样本、下次刷新和 Skill 更新 owner。
"""


def decision_template(data: dict) -> str:
    outputs = "、".join(data.get("outputs", [])) or "业务交付物"
    return f"""# {data['display_name']}决策记录

## 背景与业务对象

- 主场景、目标和错误后果：
- 上游、下游与 source of truth：
- 决策人、审批人、执行人和验收人：

## 事实、假设与未知

| 项目 | 类型 | 来源/版本 | 可信度 | 影响 | 补证 owner |
|---|---|---|---|---|---|

## 方案比较

| 方案 | 适用条件 | 预期收益 | 成本与依赖 | 反证/风险 | 可逆性 | 选择/放弃理由 |
|---|---|---|---|---|---|---|

## 异常、止损与恢复

| 触发器 | 检测证据 | 暂停范围 | 人工升级 | 补偿/回滚 | 恢复验收 |
|---|---|---|---|---|---|

## 交付与验收

预期交付：{outputs}

| 动作/交付 | Owner | 依赖 | 截止 | 验收证据 | 护栏 |
|---|---|---|---|---|---|

## 复盘

- 结果、领先和护栏指标：
- 失败样本与未知项：
- 下次复盘、规则版本和维护人：
"""


def sync_depth(root: Path = ROOT) -> dict:
    changed = 0
    for meta_path in sorted(root.rglob("skill.json")):
        rel = meta_path.relative_to(root)
        if rel.parts[0] in {"templates", "work"}:
            continue
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        base = meta_path.parent
        readme_path = base / "README.md"
        readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
        scenarios = scenario_values(data, readme)
        write_generated(base / "references/scenario-playbook.md", playbook(data, scenarios))
        write_generated(base / "assets/decision-record-template.md", decision_template(data))
        skill_path = base / "SKILL.md"
        before = skill_path.read_text(encoding="utf-8")
        after = inject_skill(before)
        if before != after:
            skill_path.write_text(after, encoding="utf-8"); changed += 1
        if readme_path.exists():
            after_readme = inject_readme(readme)
            if after_readme != readme:
                readme_path.write_text(after_readme, encoding="utf-8")
        files = set(data.setdefault("distribution", {}).get("package_files") or [])
        files.update({"references/scenario-playbook.md", "assets/decision-record-template.md"})
        data["distribution"]["package_files"] = sorted(files)
        meta_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"skills": sum(1 for _ in root.rglob("skill.json")), "changed": changed}


if __name__ == "__main__":
    result = sync_depth(ROOT)
    print(f"Depth resources synchronized; skill entries changed {result['changed']}")
