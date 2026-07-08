# Live Dashboard Check

Checked in Chrome on July 8, 2026.

## Dataset-Level State

- Dataset: `JUNE24-PSI-UNDELIVERED-EVALED`
- Tasks: 520
- Total sessions visible after creating a spot-check run: 713
- Scored sessions: 0
- Overall pass rate / average score: unavailable
- Charts tab: visible, but chart area says no scores found.
- Discussion tab: no comments yet.
- Task Quality tab: 520 production tasks, 0 analyzed, 520 not analyzed.
- QualityHill Filter: no runs visible. I did not start the full QualityHill run because it appears to be a dataset-wide analysis job across all 520 tasks.

Fleet later clarified that no-session tasks can be dropped from Project One for now. The final committed triage therefore uses the 257 tasks with visible sessions as the main analysis scope, while this dashboard note preserves the full dataset-level state I observed.

## Later Dashboard Recheck After Mixed Batch

Rechecked the dataset dashboard after the 48-task mixed batch had time to register.

- Total sessions visible: 761.
- New sessions since the spot-check state: 48, matching the mixed batch size.
- Scored sessions visible: 7.
- Tasks scored: 6.
- Overall pass rate on scored sessions: 28.6%.
- Overall average score on scored sessions: 0.29.
- `anthropic/claude-fable-5`: 51 total sessions, 7 scored sessions, 6 scored tasks, 28.6% pass rate, 0.29 average score.
- Other visible model rows still showed no scored sessions: `openai/gpt-5.5`, `anthropic/claude-opus-4.8`, `qwen/qwen3.6-plus`, and `qwen/qwen3.6-27b`.

Interpretation: the mixed batch did register and some completed/scored runs are now visible, but only 7 scored sessions is still too small to use as the main quality signal for the 520-task dataset. I would treat this as validation that the run machinery works and as an early smoke test, not as a replacement for the static triage plus human derivability review.

## Spot-Check Run Created

- Job name: `codex-spotcheck-derivability`
- Job ID: `0f034d34-0a1d-412e-b4f5-d977d3e84d92`
- Task key: `task_mdikk1gtyd2_n_1781983231400_jtfmhmm1q__ayush_20260624__worktrial_taskloss_20260707`
- Environment: `psi-consumer-finance`
- Model: `anthropic/claude-fable-5`
- Pass@K: 1
- Max steps: 999
- Session ID: `411164dc-a942-4ee1-8020-527473a5797a`
- Observed status: `In Progress`
- Recording/transcript viewer: available and live.
- Score: not available yet.
- Grading runs: none visible during the check.

## Mixed Batch Run Created

- Job name: `codex-mixed-batch-48-stratified`
- Job ID: `704a285a-b5d1-437b-8322-c1be58b3e422`
- Dashboard URL: `https://fleetai.com/dashboard/jobs/704a285a-b5d1-437b-8322-c1be58b3e422`
- Sampling method: stratified 48-task sample, 6 tasks from each environment x triage bucket combination.
- Model: `anthropic/claude-fable-5`
- Pass@K: 1
- Max steps: 999
- Sessions created: 48
- Observed status after launch: `In Progress`
- Score: not available at launch.

## Interpretation

This confirms that sessions and recordings are accessible now, and that new runs can be created from the task-level dashboard. The later recheck added a small amount of pass/fail evidence, but it is still sparse: 7 scored sessions across 6 tasks out of 520.

For the deliverable, I would treat live sessions as a final validation layer rather than a blocker. The existing toolkit is already useful because it analyzes the 257 session-backed task definitions and turns verifier risk into concrete human review queues. If more time is available, the highest-value follow-up is to run or inspect a small, representative set of sessions across the `A`, `B`, `C`, and `D` buckets, not to wait passively for the entire dataset to become scored.
