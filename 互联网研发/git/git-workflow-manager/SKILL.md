---
name: git-workflow-manager
description: Inspect repository state and safely plan or execute branch creation, commits, merges, rebases, release promotion, conflict handling, and recovery while respecting repository-specific policies and preserving user changes. Use when an AI needs to choose or create a feature or fix branch, move changes through test, preproduction, and production branches, prepare commits, resolve integration conflicts, explain divergence, or prevent unsafe Git operations.
---

# Git Workflow Manager

Repository evidence overrides generic branch-flow assumptions.

## Load resources

- 涉及事实、统计、实时状态或系统写入时，必须读取 `references/data-source-and-api-gate.md` 并使用 `assets/data-source-intake-template.md` 向使用者确认静态数据与合规接口；不得用模型记忆补造数据。

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/safety-checks.md before any mutating Git operation.
- 在 SkillForge 仓库内必须读取 `公司上下文/git-policy.yaml`；独立分发时必须要求调用方提供等价分支策略快照。
- Use assets/git-change-plan.md when a multi-step promotion or recovery needs approval.



## User intake gate

- 正式执行前必须询问使用者并确认范围、目标、对象、国家/渠道/系统、时间窗口、owner、审批人和不可改变项。
- 必需输入：repository_and_requested_outcome。建议补充：branch_policy、target_branch、commit_range、release_context。已有数据、模板、词库、规则和历史结论必须先盘点版本与优先级。
- 缺少会改变结论的输入时，只能交付问题清单、调研计划或带假设的草案；不得自行补造事实。



## Data and compliant API intake gate

1. 先询问使用者是否有静态文件（CSV、Excel、JSON、Parquet、日志或文档）、系统导出、数据库视图/查询结果、官方 API、已授权第三方 API 或允许查询的当前公开来源，并确认哪些来源优先。
2. 对每个接口登记 owner、业务目的、授权依据、环境、认证方式、字段/行范围、时间粒度、刷新 SLA、限流、成本、个人/敏感数据、留存删除和下游发布权限。
3. 不在对话、Skill、脚本参数、日志或交付物中索要或保存明文 token、key、cookie、密码或私钥；使用环境变量、密钥管理或已授权连接器。
4. 数据可读不等于允许使用或公开。用途、字段、国家、主体或下游超出授权时，停止并标记 `REVIEW_REQUIRED`。
5. 接口不可用、数据过期、样本偏差、字段冲突或关键口径缺失时，保留缺口并降级为数据需求单、调研框架或带假设草案；不得由 LLM 补造销量、趋势、价格、库存、Rank、薪资、法规或经营结论。
6. 输出必须附数据源登记、数据截止、查询/版本、质量限制、静态快照有效期和下一次刷新 owner。

## Workflow

1. Inspect repository instructions, current branch, status, remotes, upstream, recent history, worktrees, and relevant branch existence.
2. Preserve unrelated and uncommitted user changes. Identify which files and commits belong to the requested task.
3. Determine the repository's real branching policy. Use feature/YYMMDD/name and fix/YYMMDD/name only when local policy does not say otherwise.
4. Record the current development branch as `return_branch`, then state the intended source, destination, commit set, integration method, tests, rollback point, and return path before changing history or shared branches.
5. For new work, branch from the verified base and keep commits scoped and intentional. Before `git commit`, validate the trimmed message: it must not be empty, its meaningful description must contain at least 5 characters, and it must explain what changed, why, and how it was verified. Reject the commit when this gate fails.
6. For integration, fetch current refs, compare divergence, inspect the actual diff and commits, then choose merge, rebase, cherry-pick, or pull request based on policy and collaboration state.
7. On conflict, list every conflicted path and Git status code, inspect base/ours/theirs and relevant commits, then classify it as expected or abnormal. Resolve only expected in-scope conflicts whose intent is evidenced; pause abnormal or ambiguous conflicts for an explicit decision. Rerun relevant tests and do not mark conflicts resolved merely because markers are gone.
8. Before promotion, verify test evidence, branch ancestry, version or migration requirements, and environment-specific changes.
   When the destination is not `test`, run a test-contamination audit against the approved development source: detect the test ref or test-only commits, merge parents, equivalent cherry-picked/squashed patches, and test-environment configuration entering the target. Any confirmed contamination is `ABNORMAL` and blocks integration or release.
9. After an integration or environment verification, return to `return_branch` when the repository is in a safe switchable state. If unresolved conflicts prevent switching, stop, preserve conflict evidence, and report the blocked return instead of forcing it.
10. Report exact resulting branch, commit, upstream state, remaining changes, verification, and any manual next step. A successful workflow must end on `return_branch` unless the user explicitly requested another final branch.

## Terminal exception and conflict contract

Any failed command, validation, hook, merge, rebase, test, push, branch return, or partial operation must print a structured terminal report and exit non-zero:

1. `FAILED_STEP`: exact operation and command class.
2. `RAW_ERROR`: relevant original stderr or tool error, redacting secrets only.
3. `LIKELY_CAUSE`: evidence-backed cause or `UNKNOWN`.
4. `REPOSITORY_STATE`: branch, merge/rebase/cherry-pick state, worktree changes, upstream and safe refs.
5. `IMPACT`: completed and incomplete effects, including risk to user work or shared history.
6. `SAFE_NEXT_ACTION`: read-only checks, retry prerequisites, recovery or required human authority.

For conflicts, additionally print `CONFLICT_PATH`, Git status code, base/ours/theirs evidence, `EXPECTED` or `ABNORMAL`, classification reason, affected behavior and decision owner. Treat a conflict as abnormal when it is outside approved scope, touches unrelated user changes, involves protected/environment branch misuse, has unexpected delete/rename, affects migrations, permissions, security configuration, dependency locks, generated or binary files, or lacks enough evidence to preserve both sides' intent. Abnormal or ambiguous conflicts must stop for review; never auto-select ours/theirs merely to complete the merge.

For test contamination, print the non-test target, test ref, approved source refs, offending commit or patch IDs, merge-parent evidence, environment-specific paths and the exact rule that fired. Use `BLOCK` for confirmed test-only history or test environment material, `WARNING` for ambiguous provenance requiring review, and `PASS` only when all configured checks complete. An unavailable or incomplete audit is not a pass.

## Safety rules

- Never use reset --hard, clean -fd, checkout --, force push, or history rewriting without explicit authority and a recovery plan.
- Do not stage or commit unrelated user changes.
- Do not create a commit with an empty, whitespace-only, placeholder, or fewer-than-5-character meaningful message. The message must explain the change, reason and verification.
- Do not assume master, main, test, or pre exists; verify refs.
- Treat existing `master`, `main`, `test`, and `pre` as protected or environment branches: do not develop, edit files, or commit directly on them.
- Never merge `test` into a non-`test` branch. Promote the verified development branch or an explicitly approved commit set; the test environment branch is not a release source.
- Before every non-`test` integration, verify that test-only commits, equivalent patches and test-environment configuration are absent. Do not infer safety merely because no merge commit is visible.
- Before temporarily switching branches, record the current development branch. Return to it after merge, verification, or release work; never use a destructive command merely to make the return possible.
- Prefer non-interactive commands and create a backup ref before approved risky history edits.
- Stop when credentials, protected-branch policy, unresolved product choices, or destructive conflict decisions require user authority.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。



## Evidence freshness gate

- 标明数据截止、采集时间、来源、版本、适用国家/渠道/系统和刷新周期。
- 市场、价格、Rank、趋势、库存、平台规则、法律、税务、汇率、软件版本和人员信息等时效事实必须在本次任务中重新核验，不得使用模型记忆冒充实时数据。
- 单次快照不能写成历史趋势；来源冲突、过期或不可访问时保留差异并降级为调研、草案或 `REVIEW_REQUIRED`。

## Output contract

For advice, return observed state, recommended flow, exact commands, risks, verification, and rollback. For execution, perform only authorized changes and return resulting refs, commits, tests, and remaining work.
