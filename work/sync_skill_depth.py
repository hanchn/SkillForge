#!/usr/bin/env python3
"""Add complete-business-result depth resources to legacy formal skills."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKER = "<!-- generated-by: sync-skill-depth -->"

DATA_EXPECTATIONS = {
    "市场采购": "市场需求、关键词/趋势、竞品、价格、Rank、评价、费用、广告、退货、供应商、MOQ、报价、交期、质量、物流、关税和合规限制",
    "渠道运营": "站点/平台商品、流量、搜索词、转化、订单、价格、库存、广告、评价、退货、费用、账户健康和平台规则",
    "精准营销": "关键词、受众同意、投放、触点、创意、站点事件、订单利润、归因窗口、平台规则和内容表现",
    "数据看板": "指标定义、数据字典、表/接口血缘、时间粒度、时区、币种、状态、刷新、质量、权限和对账基准",
    "仓储库存": "SKU、仓库、库存状态、批次、预占、在途、订单、销量、预测、交期、采购、物流、盘点、成本和异常事件",
    "财务出纳": "主体、科目、期间、币种、银行、支付、订单、发票、税务、汇率、审批、总账/明细账和对账基准",
    "人事招聘": "组织编制、岗位事实、候选人授权资料、招聘漏斗、薪酬样本、工作地规则、培训/员工记录和隐私权限",
    "法律政务": "主体、司法辖区、产品/交易事实、合同版本、官方现行规则、证据材料、审批记录、期限和专业意见",
    "互联网研发": "真实仓库、分支/提交、依赖与框架版本、配置、接口契约、数据库 schema、日志、指标、trace、测试和部署状态",
    "创拍视觉": "商品事实、原始素材、版权/肖像/模特授权、品牌规范、渠道规格、关键词/标签库、模型版本、生成血缘和效果数据",
    "客售前后": "商品、价格、库存、优惠、订单、支付、物流、退款退货、保修赔付、评价、知识库、会话、线索、语言、权限和客户同意",
    "基础工具": "任务目标、事件/周期范围、静态文件或业务接口、消息平台连接器、责任人、状态、证据、权限、回执、验收和复盘记录",
    "project-root": "仓库文件、Skill 元数据、版本指纹、生成脚本、索引、审计、前端配置和用户明确修改",
}


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


def inject_skill(text: str, data: dict) -> str:
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
    if "references/data-source-and-api-gate.md" not in text:
        line = "- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。"
        marker = "## Load resources\n"
        text = text.replace(marker, marker + "\n" + line + "\n", 1) if marker in text else text + "\n\n" + line + "\n"
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
    if "## Evidence freshness gate" not in text:
        block = """

## Evidence freshness gate

- 标明数据截止、采集时间、来源、版本、适用国家/渠道/系统和刷新周期。
- 市场、价格、Rank、趋势、库存、平台规则、法律、税务、汇率、软件版本和人员信息等时效事实必须在本次任务中重新核验，不得使用模型记忆冒充实时数据。
- 单次快照不能写成历史趋势；来源冲突、过期或不可访问时保留差异并降级为调研、草案或 `REVIEW_REQUIRED`。
"""
        marker = "## Output contract"
        text = text.replace(marker, block + "\n" + marker, 1) if marker in text else text + block
    intake_terms = ["询问使用者", "现有数据", "用户提供", "使用者优先", "确认范围"]
    if not any(term in text for term in intake_terms):
        required = "、".join(data.get("inputs", {}).get("required", [])) or "目标与真实现状"
        optional = "、".join(data.get("inputs", {}).get("optional", [])) or "历史、模板、系统与约束资料"
        block = f"""

## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：{required}。建议补充：{optional}。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。
"""
        marker = "## Workflow"
        text = text.replace(marker, block + "\n" + marker, 1) if marker in text else text + block
    if "## Data and compliant API intake gate" not in text:
        block = """

## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。
"""
        marker = "## Workflow"
        text = text.replace(marker, block + "\n" + marker, 1) if marker in text else text + block
    return text


def data_source_gate(data: dict) -> str:
    category = (data.get("category_path") or ["project-root"])[0]
    expected = DATA_EXPECTATIONS.get(category, "完成任务所需的真实业务事实、当前状态、历史基线和约束")
    return f"""# {data['display_name']}数据与合规接口门禁

## 本 Skill 的最低数据面

优先确认：{expected}。

该清单不是要求所有字段都存在，而是要求先判断哪些字段会改变结论、是否已授权、是否足够新鲜。缺关键事实时必须降级，不能让 LLM 用常识补值。

## 向使用者提问

1. 是否已有 CSV、Excel、JSON、Parquet、日志、文档、报表、系统导出、数据库视图/查询结果或历史快照？位置、owner、版本、导出/截止时间和口径是什么？
2. 是否有官方 API、内部服务接口或已获许可的第三方 API？它们分别负责哪些功能和事实？
3. 哪个来源是每个关键字段的 source of truth？多个来源冲突由谁裁决？
4. 是否允许本次任务联网查询当前公开来源？是否有地域、账号、合同、robots、平台条款或再分发限制？
5. 哪些数据只允许内部分析，哪些可以进入交付物、前端、广告、PDP、llms、Schema 或其他公开内容？

## 合规与安全验证

- 验证接口提供方、合同/条款、业务目的、最小字段、账号和环境权限；能够调用不代表用途合法。
- 个人、候选人、客户、员工、支付、位置、生物识别或其他敏感数据默认最小化，并按司法辖区与公司制度升级。
- 不接收明文凭证；只记录凭证引用方式和授权 owner。日志、截图、错误与样例响应也必须脱敏。
- 明确分页、时间窗、时区、币种、状态、去重、限流、成本、缓存、重试、删除同步和审计留存。
- 对 CSV/Excel 等静态表检查编码、sheet/列定义、主键、粒度、单位、币种、时区、缺失、重复、异常值、导出时点和截断；文件能打开不代表数据可用于决策。
- 第三方估算、抓取、平台后台、公司订单和财务数据必须分层标识，不得混成同一真实性等级。

## 失败与降级

- `DATA_READY`：关键字段、授权、口径和新鲜度满足本次决策。
- `STATIC_SNAPSHOT`：只能说明快照时点，必须写有效期，不得冒充实时或趋势。
- `RESEARCH_ONLY`：只能输出待验证假设、数据需求和采集计划。
- `REVIEW_REQUIRED`：授权、敏感数据、口径冲突或发布范围需要 owner/法务/安全确认。
- `BLOCKED`：核心数据无法获得且继续执行会制造虚假结论或越权。
"""


def data_source_template(data: dict) -> str:
    return f"""# {data['display_name']}数据源与接口接入记录

## 任务与优先级

- 目标、范围、国家/渠道/系统、时间窗口：
- 使用者提供的来源是否优先，以及优先规则：
- 决策人、数据 owner、审批人、验收人：

## 静态数据与接口登记

| 来源 | 静态/API/查询 | Owner | 业务目的与授权 | 环境/位置 | 字段范围 | 时间粒度/截止 | 刷新 SLA | 质量限制 | 敏感等级 | 可否公开 | 降级方案 |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 字段事实源与冲突

| 关键字段/指标 | 主事实源 | 备选源 | 口径 | 冲突 | 裁决 Owner | 当前状态 |
|---|---|---|---|---|---|---|

## 凭证与运行安全

- 凭证引用方式（不得粘贴密钥）：
- 最小权限、限流、成本、分页、重试和缓存：
- 脱敏、留存、删除同步和审计：

## 数据就绪结论

- 状态：`DATA_READY / STATIC_SNAPSHOT / RESEARCH_ONLY / REVIEW_REQUIRED / BLOCKED`
- 缺口、影响、补数 owner 与截止：
- 静态快照有效期和下一次刷新：
"""


def inject_acceptance(text: str, data: dict) -> str:
    """Repair legacy checklist syntax and add deliverable-specific gates."""
    text = re.sub(r"(?m)^\+- \[ \]", "- [ ]", text)
    outputs = [str(item) for item in data.get("outputs", [])]
    if outputs and not all(item in text for item in outputs[:3]):
        checks = "\n".join(
            f"- [ ] `{item}` 已完整交付，并有下游使用者、验收证据和剩余风险"
            for item in outputs
        )
        text += f"""

## 交付物专项验收

- [ ] 已询问使用者现有数据、系统、模板、词库、规则、优先级和不可改变项
- [ ] 已标明时效事实的数据截止、采集时间、来源、版本和适用范围
{checks}
- [ ] 已覆盖正常路径、关键异常、暂停条件、人工升级、补偿或回滚
- [ ] 最终结论明确事实、假设、未知项、owner、审批和下一次复核时间
"""
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
        write_generated(base / "references/data-source-and-api-gate.md", data_source_gate(data))
        write_generated(base / "assets/data-source-intake-template.md", data_source_template(data))
        skill_path = base / "SKILL.md"
        before = skill_path.read_text(encoding="utf-8")
        after = inject_skill(before, data)
        if before != after:
            skill_path.write_text(after, encoding="utf-8"); changed += 1
        if readme_path.exists():
            after_readme = inject_readme(readme)
            if after_readme != readme:
                readme_path.write_text(after_readme, encoding="utf-8")
        acceptance_path = base / "eval/acceptance.md"
        if acceptance_path.exists():
            acceptance = acceptance_path.read_text(encoding="utf-8")
            updated_acceptance = inject_acceptance(acceptance, data)
            if updated_acceptance != acceptance:
                acceptance_path.write_text(updated_acceptance, encoding="utf-8")
        files = {
            path.relative_to(base).as_posix()
            for path in base.rglob("*")
            if path.is_file()
            and "__pycache__" not in path.parts
            and path.suffix != ".pyc"
            and path.name not in {".DS_Store"}
        }
        data.setdefault("distribution", {})["package_files"] = sorted(files)
        meta_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"skills": sum(1 for _ in root.rglob("skill.json")), "changed": changed}


if __name__ == "__main__":
    result = sync_depth(ROOT)
    print(f"Depth resources synchronized; skill entries changed {result['changed']}")
