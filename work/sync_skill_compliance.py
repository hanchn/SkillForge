#!/usr/bin/env python3
"""Attach a portable, category-aware compliance baseline to every formal skill."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_RELATIVE = "references/compliance-baseline.md"

COMMON = [
    "只处理完成当前任务所必需的数据、文件和系统范围；未知权限、来源、适用国家或授权状态必须暂停并标记待确认。",
    "区分建议、草案、审批和真实执行；未经授权不得写入生产系统、对外发布、付款、下单、签约、删除、封禁或修改正式记录。",
    "不得在输出、日志、示例或附件中暴露密码、密钥、令牌、身份证件、银行凭证或非必要个人信息。",
    "涉及法律、税务、会计、劳动、产品安全或监管判断时，Skill 只做风险识别和材料准备，按门槛升级贵司授权人员或合格专业人士。",
    "保留来源、日期、版本、决策人、执行人、变更、审批、失败和回滚证据；不得声称已合规、已批准或已执行，除非存在对应记录。",
]

PROFILES = {
    "互联网研发": {
        "name": "product-engineering",
        "title": "产研合规基线",
        "rules": [
            "落实最小权限、数据分类、隐私保护、密钥管理、输入验证、对象授权、依赖供应链和安全日志要求。",
            "使用开源代码、模型、字体、素材、数据集或第三方 SDK 前核验许可证、商业使用、署名、再分发和数据传输条款。",
            "生产变更必须有评审、测试、发布授权、灰度、观测和回滚；不得用开发环境通过代替生产安全。",
            "AI 产品必须定义模型输入输出、供应商数据保留、人工复核、错误处置、评估、漂移和版本审计。",
            "执行 Git 操作时必须优先读取贵司分支治理规则；在 SkillForge 仓库内读取 `公司上下文/git-policy.yaml`。不得以通用 Git Flow 覆盖贵司已确认的保护分支与环境隔离规则。",
            "`master`、`main`、`test`、`pre` 属于受保护或环境分支：禁止直接编写代码、直接提交或把未审查工作留在这些分支；开发必须在独立 feature、fix 或经批准的开发分支完成。",
            "禁止将 `test` 合并到任何非 `test` 分支；发布应从原开发分支或经核验的提交集按批准流程进入目标环境，不能把测试环境分支当作代码来源。",
            "任何临时切换分支的合并、验证或发布动作结束后，即使失败或发生冲突，也必须在安全可切换时返回操作前记录的开发分支，并报告最终分支；存在未解决冲突时不得强行切换。",
        ],
    },
    "渠道运营": {
        "name": "channel-commerce",
        "title": "渠道经营合规基线",
        "rules": [
            "商品、价格、折扣、库存、评价、销量、送达和售后声明必须可追溯到真实证据，不得制造虚假稀缺、虚假评价或误导性比较。",
            "上线前核验销售国家、平台政策、商品准入、标签警示、消费者权益、税费和召回责任。",
            "账户、Listing、价格、促销、库存和订单写入必须经过对应 owner 授权并保留变更与回滚记录。",
        ],
    },
    "客服售前": {
        "name": "customer-presales",
        "title": "客服售前合规基线",
        "rules": [
            "不得承诺未经批准的功能、效果、库存、价格、折扣、送达、退款、保修或赔偿。",
            "客户信息按最小必要采集；营销同意、敏感信息、聊天记录共享和跨系统流转必须遵守贵司隐私与保留规则。",
            "高风险产品、安全、法律、医疗、未成年人、歧视、威胁或重大投诉必须转人工和指定 owner。",
        ],
    },
    "精准营销": {
        "name": "precision-marketing",
        "title": "营销合规基线",
        "rules": [
            "广告声明、比较、折扣、环保、健康、达人背书和用户评价必须有证据并按目标市场与平台要求披露。",
            "邮件、短信、Cookie、广告受众、再营销和 CRM 触达必须核验合法来源、同意、退订、频控和数据最小化。",
            "不得使用敏感属性、歧视性代理变量、暗黑模式、虚假互动或无法证明增量的误导性归因。",
        ],
    },
    "创拍视觉": {
        "name": "creative-production",
        "title": "创意与 AIGC 合规基线",
        "rules": [
            "拍摄、UGC、虚拟模特和 AIGC 必须核验肖像、声音、音乐、字体、商标、场地、素材和商业使用授权的地域、渠道、期限与修改范围。",
            "不得通过拍摄、修图、生成或剪辑改变商品关键事实、伪造用户体验、隐藏商业关系或制造误导性前后对比。",
            "AI 输入、模型、参数、输出、人工修改和必要披露必须可追溯；人物、未成年人、敏感属性和权利不明素材必须转人工。",
        ],
    },
    "市场采购": {
        "name": "market-procurement",
        "title": "采购与供应合规基线",
        "rules": [
            "供应商准入必须核验主体、受益所有人、产地、材料、产品合规、制裁出口管制、劳工环境和反商业贿赂风险。",
            "报价、样品、规格、MOQ、付款、交期、质检、知识产权和变更必须有书面版本与审批，不得超授权承诺。",
            "高风险制裁命中、强迫劳动、产品安全、假证、重大质量或利益冲突必须暂停采购并升级。",
        ],
    },
    "仓储库存": {
        "name": "warehouse-inventory",
        "title": "仓储库存合规基线",
        "rules": [
            "实物、单据和系统库存必须可对账；盘点、调整、报废和损耗不得由同一人无证据完成保管、审批与记账。",
            "仓容、消防、设备、危险品、劳动安全、数据访问和承运交接必须遵守所在地规则与贵司 SOP。",
            "不得把冻结、残次、召回、未检验、预占或不可靠在途库存作为可售；重大差异和安全事件必须隔离升级。",
        ],
    },
    "数据看板": {
        "name": "data-analytics",
        "title": "数据分析合规基线",
        "rules": [
            "分析数据必须有合法来源、访问权限、用途范围、保留规则和可对账口径；个人数据优先聚合、去标识与最小化。",
            "不得用受保护或敏感属性进行歧视性分群、定价、雇佣或待遇决策，也不得把相关性写成因果。",
            "对外报表必须控制行级数据、商业秘密、小样本重识别和导出权限，并披露数据截止、缺失和不确定性。",
        ],
    },
    "法律政务": {
        "name": "legal",
        "title": "法律工作合规基线",
        "rules": [
            "先确认司法辖区、主体、事实时间、合同版本、适用法律和时效；不得跨国家套用结论。",
            "Skill 输出不构成正式法律意见，不冒充律师；诉讼、监管调查、重大争议和高风险交易必须升级合格律师。",
            "控制律师保密特权、案件策略、举报人、调查、证据和个人信息的知情范围，不得修改、删除或选择性隐藏证据。",
        ],
    },
    "财务出纳": {
        "name": "finance-treasury",
        "title": "财务出纳合规基线",
        "rules": [
            "申请、审批、付款、记账、对账和账户管理必须职责分离；银行账户变更、大额或异常付款执行双人复核。",
            "法定会计、税务、发票、外汇、关税、反洗钱和资金用途按主体与司法辖区核验，不得以管理口径替代申报口径。",
            "不得暴露网银密码、UKey、印鉴、验证码或完整银行敏感信息；异常收款人、重复付款和欺诈信号必须暂停。",
        ],
    },
    "人事招聘": {
        "name": "hr-recruiting",
        "title": "人事招聘合规基线",
        "rules": [
            "招聘、面试、培训、绩效、调查和离职只使用岗位或业务相关证据，禁止基于受保护特征或无关敏感信息作决定。",
            "候选人和员工数据遵循告知、必要、授权、访问、保留和删除要求；背景核验、监控和跨境传输必须单独评估。",
            "薪酬承诺、劳动合同、纪律、解雇、歧视、工时和跨境用工必须按工作地规则由 HR、法务和授权负责人处理。",
        ],
    },
    "project-root": {
        "name": "repository-governance",
        "title": "项目治理合规基线",
        "rules": [
            "仓库治理不得覆盖用户已有修改、删除有效业务资产或暴露本地秘密。",
            "分类、版本、下载、索引和打包变更必须可复现、可验证并保留迁移记录。",
        ],
    },
}


def profile_for(payload: dict) -> dict:
    path = payload.get("category_path") or []
    top = path[0] if path else "project-root"
    return PROFILES.get(top, {"name": "general-business", "title": "通用业务合规基线", "rules": []})


def baseline_text(payload: dict, profile: dict) -> str:
    rules = "\n".join(f"- {rule}" for rule in [*COMMON, *profile["rules"]])
    return f"""# {payload.get('display_name', payload['name'])}合规基线

> 合规配置：`{profile['name']}`  
> 适用方式：执行前强制检查，执行中触发即暂停或转人工，交付时记录证据。

## 强制规则

{rules}

## 执行门禁

1. 确认国家或地区、业务主体、目标对象、数据来源、系统权限和对外影响。
2. 确认适用的贵司制度、平台规则、合同、授权和当前官方要求；规则不明时不得自行判定合规。
3. 将事项分为 `ALLOW`、`REVIEW_REQUIRED`、`COMPLIANCE_REJECTED`。
4. `REVIEW_REQUIRED` 必须给出风险、缺失证据、指定审批角色和暂停范围。
5. `COMPLIANCE_REJECTED` 不得通过改写提示词、拆分任务或换工具绕过。
6. 输出记录 Skill 版本、输入来源、规则版本、判断、审批、执行人与时间。

## Skill 无法单独保证的事项

- 真实系统权限隔离、网络与数据传输控制。
- 合同、许可证、授权书、主体或证据真伪。
- 不可篡改日志、双人审批和生产强制门禁。
- 当前法律的最终适用与正式专业意见。

因此，本文件是第一层规则与检查门禁，必须与贵司系统控制、审批流程、法务合规和审计机制组合使用。
"""


def inject_skill_reference(text: str) -> str:
    line = "- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。"
    if line in text:
        return text
    marker = "## Load resources\n"
    if marker in text:
        return text.replace(marker, marker + "\n" + line + "\n", 1)
    heading = next((value for value in text.splitlines() if value.startswith("# ")), None)
    if heading:
        return text.replace(heading, heading + "\n\n## Compliance gate\n\n" + line, 1)
    return text + "\n\n## Compliance gate\n\n" + line + "\n"


def inject_readme(text: str, profile: dict) -> str:
    heading = "## 合规与权限"
    block = f"""{heading}

- 合规配置：`{profile['name']}`（{profile['title']}）。
- 执行前必须读取 `references/compliance-baseline.md`，完成司法辖区、数据、权限、授权、人工复核和审计检查。
- Skill 只能提供第一层规则约束，不能替代系统权限、真实授权、正式审批或专业法律意见。

"""
    if heading in text:
        return text
    marker = "## 不适用范围与边界"
    if marker in text:
        return text.replace(marker, block + marker, 1)
    return text + "\n\n" + block


def sync_compliance(root: Path = ROOT) -> dict:
    count = 0
    for meta_path in sorted(root.rglob("skill.json")):
        relative = meta_path.relative_to(root)
        if relative.parts[0] in {"templates", "work"}:
            continue
        payload = json.loads(meta_path.read_text(encoding="utf-8"))
        package = meta_path.parent
        profile = profile_for(payload)
        reference = package / BASELINE_RELATIVE
        reference.parent.mkdir(exist_ok=True)
        reference.write_text(baseline_text(payload, profile), encoding="utf-8")
        skill_path = package / "SKILL.md"
        skill_path.write_text(inject_skill_reference(skill_path.read_text(encoding="utf-8")), encoding="utf-8")
        readme_path = package / "README.md"
        if readme_path.exists():
            readme_path.write_text(inject_readme(readme_path.read_text(encoding="utf-8"), profile), encoding="utf-8")
        payload["compliance"] = {
            "profile": profile["name"],
            "baseline": BASELINE_RELATIVE,
            "decision_states": ["ALLOW", "REVIEW_REQUIRED", "COMPLIANCE_REJECTED"],
            "human_review_required_when_uncertain": True,
            "does_not_replace_system_controls_or_professional_advice": True,
        }
        distribution = payload.setdefault("distribution", {})
        files = set(distribution.get("package_files") or distribution.get("required_files") or [])
        files.add(BASELINE_RELATIVE)
        distribution["package_files"] = sorted(files)
        meta_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
    return {"skills": count}


if __name__ == "__main__":
    result = sync_compliance(ROOT)
    print(f"Compliance baselines synchronized for {result['skills']} skills")
