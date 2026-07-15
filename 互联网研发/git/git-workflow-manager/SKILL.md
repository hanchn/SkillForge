---
name: git-workflow-manager
description: Inspect repository state and safely plan or execute branch creation, commits, merges, rebases, release promotion, conflict handling, and recovery while respecting repository-specific policies and preserving user changes. Use when an AI needs to choose or create a feature or fix branch, move changes through test, preproduction, and production branches, prepare commits, resolve integration conflicts, explain divergence, or prevent unsafe Git operations.
---

# Git Workflow Manager

Repository evidence overrides generic branch-flow assumptions.

## Load resources

- 必须读取 `references/scenario-playbook.md`，选择主场景、相邻变体、异常路径和完成门槛。
- 存在方案取舍、审批、跨团队交接或不可逆动作时，必须使用 `assets/decision-record-template.md`。

- 必须读取 `references/compliance-baseline.md`，先完成合规、权限和人工升级门禁；业务要求不得覆盖该基线。

- Read references/safety-checks.md before any mutating Git operation.
- 在 SkillForge 仓库内必须读取 `公司上下文/git-policy.yaml`；独立分发时必须要求调用方提供等价分支策略快照。
- Use assets/git-change-plan.md when a multi-step promotion or recovery needs approval.

## Workflow

1. Inspect repository instructions, current branch, status, remotes, upstream, recent history, worktrees, and relevant branch existence.
2. Preserve unrelated and uncommitted user changes. Identify which files and commits belong to the requested task.
3. Determine the repository's real branching policy. Use feature/YYMMDD/name and fix/YYMMDD/name only when local policy does not say otherwise.
4. Record the current development branch as `return_branch`, then state the intended source, destination, commit set, integration method, tests, rollback point, and return path before changing history or shared branches.
5. For new work, branch from the verified base and keep commits scoped and intentional.
6. For integration, fetch current refs, compare divergence, inspect the actual diff and commits, then choose merge, rebase, cherry-pick, or pull request based on policy and collaboration state.
7. Resolve conflicts by preserving both sides' intent and rerun relevant tests. Do not mark conflicts resolved merely because markers are gone.
8. Before promotion, verify test evidence, branch ancestry, version or migration requirements, and environment-specific changes.
9. After an integration or environment verification, return to `return_branch` when the repository is in a safe switchable state. If unresolved conflicts prevent switching, stop, preserve conflict evidence, and report the blocked return instead of forcing it.
10. Report exact resulting branch, commit, upstream state, remaining changes, verification, and any manual next step. A successful workflow must end on `return_branch` unless the user explicitly requested another final branch.

## Safety rules

- Never use reset --hard, clean -fd, checkout --, force push, or history rewriting without explicit authority and a recovery plan.
- Do not stage or commit unrelated user changes.
- Do not assume master, main, test, or pre exists; verify refs.
- Treat existing `master`, `main`, `test`, and `pre` as protected or environment branches: do not develop, edit files, or commit directly on them.
- Never merge `test` into a non-`test` branch. Promote the verified development branch or an explicitly approved commit set; the test environment branch is not a release source.
- Before temporarily switching branches, record the current development branch. Return to it after merge, verification, or release work; never use a destructive command merely to make the return possible.
- Prefer non-interactive commands and create a backup ref before approved risky history edits.
- Stop when credentials, protected-branch policy, unresolved product choices, or destructive conflict decisions require user authority.



## Complete-business-result depth gate

- 先解释业务对象、专业术语、为什么要做、结果由谁使用及错误结果的业务后果。
- 明确上游输入、下游消费者、系统事实源、责任边界、决策权、审批与人工交接点。
- 不只处理理想路径；必须覆盖缺数据、口径冲突、权限不足、依赖失败、低置信度、超时、部分成功和人工升级。
- 至少比较维持现状、推荐方案和低风险备选，说明证据、适用条件、反证、成本、风险、可逆性和放弃理由。
- Tool 或脚本执行不等于完成；交付物必须被验证，并带 owner、依赖、验收、止损、回滚、审计和复盘。

## Output contract

For advice, return observed state, recommended flow, exact commands, risks, verification, and rollback. For execution, perform only authorized changes and return resulting refs, commits, tests, and remaining work.
