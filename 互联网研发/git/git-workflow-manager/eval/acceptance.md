# Acceptance

- [ ] Repository instructions and actual refs were inspected.
- [ ] Current branch, upstream, ahead/behind, status, and worktrees are known.
- [ ] The original development branch is recorded as `return_branch`.
- [ ] No code was developed or committed directly on `master`, `main`, `test`, or `pre`.
- [ ] `test` was not merged into any non-`test` branch.
- [ ] Every non-test integration checked test-tip ancestry, test-only commits, merge parents, equivalent patches and test-environment files against approved source refs.
- [ ] Test contamination output is `PASS`, `WARNING`, or `BLOCK` with target, refs and evidence; incomplete checks never report `PASS`.
- [ ] Unrelated user changes remain untouched.
- [ ] Source, destination, commit range, method, verification, and rollback are explicit.
- [ ] Branch naming follows local policy or clearly stated fallback conventions.
- [ ] Conflict resolution preserves intent and is verified by tests or targeted checks.
- [ ] Every conflict reports path, Git status, base/ours/theirs, relevant commits, expected/abnormal classification, reason, impact and decision owner.
- [ ] Abnormal or ambiguous conflicts stop for review and are not auto-resolved by selecting ours or theirs.
- [ ] Confirmed test-only history or environment material blocks the merge/release and reports safe remediation without rewriting shared history.
- [ ] No destructive or history-rewriting operation occurs without explicit authority.
- [ ] Commit messages were rejected when empty, placeholder-like or shorter than 5 meaningful characters.
- [ ] Every created commit explains what changed, why it changed and how it was verified.
- [ ] Terminal failures show failed step, raw error, cause or `UNKNOWN`, repository state, impact, safe next action and a non-zero result.
- [ ] Final state reports branch, commit, upstream, remaining changes, and tests.
- [ ] The workflow returned to `return_branch`, or an unresolved-conflict blocker was reported without destructive cleanup.


## 交付物专项验收

- [ ] 已询问使用者现有数据、系统、模板、词库、规则、优先级和不可改变项
- [ ] 已标明时效事实的数据截止、采集时间、来源、版本和适用范围
- [ ] `git_state_and_plan.md` 已完整交付，并有下游使用者、验收证据和剩余风险
- [ ] `executed_ref_summary` 已完整交付，并有下游使用者、验收证据和剩余风险
- [ ] 已覆盖正常路径、关键异常、暂停条件、人工升级、补偿或回滚
- [ ] 最终结论明确事实、假设、未知项、owner、审批和下一次复核时间
