# Project One QA Toolkit

This repo is a handoff for Fleet Project One. It contains a repeatable QA workflow for deciding which tasks in `JUNE24-PSI-UNDELIVERED-EVALED` are easiest to recover, which need repair, and which should go to deeper manual review.

The goal is not to let an LLM decide what ships. The goal is to make the repetitive QA work faster, consistent, and easy for a human reviewer to audit.

## Start Here

| If you are... | Open first | Why |
| --- | --- | --- |
| A product manager or operator | `SUBMISSION.md` | Short scope, outputs, and bottom-line handoff. |
| Reviewing task quality | `reports/task_recovery_ranked.csv` | Ordered queue of tasks to spot-check, recover, repair, or manually review. |
| Reviewing the analysis | `final_project_one_report.md` | Concise method, findings, bucket counts, and next steps. |
| Reviewing actual runs | `trace_evidence.md` and `reports/post_run_verification_summary.md` | Concrete completed-session findings plus a post-run category queue. |
| Reviewing the tool | `triage_dataset.py`, `constant_derivability_worklist.py`, and `post_run_verifier.py` | The scripts that generate the QA outputs. |
| Checking human judgment | `evidence_log.md` | Manual sample showing how I audited the tool output. |

## Current Scope

The source of truth for this handoff is the Fleet dashboard dataset:
[JUNE24-PSI-UNDELIVERED-EVALED](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).

I scoped the committed analysis to the dashboard/evaluated task set shown there.

| Item | Count |
| --- | ---: |
| Fleet dashboard task scope | 257 tasks |
| Consumer-finance tasks in scope | 150 tasks |
| Personal-health tasks in scope | 107 tasks |
| Total sessions in scope | 712 sessions |
| Scored sessions on dashboard | 658 sessions |
| Tasks scored on dashboard | 220 tasks |
| Dashboard pass rate | 7.6% |
| Dashboard average score | 0.08 |
| Trace spot-checks documented | 20 sessions |

## Main Deliverables

| File | What it is for |
| --- | --- |
| `reports/task_recovery_ranked.csv` | Main recovery queue. Start here when deciding what to review next. |
| `reports/task_triage.csv` | Full task-level static QA output with risk score, bucket, findings, session count, and prompt preview. |
| `reports/derivability_worklist.csv` | Verifier constants that need proof from the prompt, seed data, or session evidence. |
| `reports/post_run_verification.csv` | Completed-run evidence classified into pass, narrow repair, partial, environment, ambiguity, or broad-failure queues. |
| `reports/post_run_verification_summary.md` | Human-readable summary of the post-run verification layer. |
| `reports/manual_review_queue.md` | Top 50 high-risk tasks with manual-review checklist prompts. |
| `trace_evidence.md` | Concrete session-level examples: 5 completed traces from each recovery bucket. |
| `final_project_one_report.md` | Summary of method, results, recovery strategy, and limits. |
| `evidence_log.md` | Human-in-the-loop sample across buckets and environments. |
| `live_dashboard_check.md` | Dashboard score snapshot and task-set check. |

The dataset export, API keys, browser cookies, bearer tokens, and local request headers are intentionally not committed.

## How The Workflow Works

1. Start from the Fleet dashboard dataset scope and session metadata.
2. Run static triage over each task prompt and verifier.
3. Bucket each task by recovery priority.
4. Extract verifier constants that are not obviously present in the prompt.
5. Inspect actual completed traces for representative pass/fail behavior.
6. Run the post-run verifier to turn completed trace evidence into a repair/promote queue.
7. Turn static flags and trace outcomes into concrete repair/promote decisions.

## Recovery Buckets

| Bucket | Meaning | What to do |
| --- | --- | --- |
| `A_likely_good_spot_check` | Low static risk. | Spot-check seed/session evidence, then consider promotion. |
| `B_close_verify_derivability` | Likely recoverable. | Prove hidden verifier constants are derivable. |
| `C_repair_candidate` | Worth saving, but needs cleanup. | Reconcile prompt, verifier, and seed-world facts. |
| `D_high_risk_manual_review` | Highest static risk. | Inspect manually before spending recovery time. |

The bucket is not pass/fail. It is a review priority.

## Current Results

| Bucket | Count |
| --- | ---: |
| `A_likely_good_spot_check` | 17 |
| `B_close_verify_derivability` | 92 |
| `C_repair_candidate` | 109 |
| `D_high_risk_manual_review` | 39 |

The strongest near-term recovery pool is the 17 likely-good tasks plus the 92 close/derivability tasks. The 109 repair candidates are the main fix backlog. The 39 high-risk tasks should be inspected before investing recovery time.

The derivability worklist found 1,843 verifier constants across 254 scoped tasks. That is not a rejection count. It is a list of proof obligations: for each hidden amount, date, name, email, or phone number, a reviewer should confirm whether it is uniquely derivable from the prompt plus the seed world.

The trace sample adds concrete calibration:

- `task_nw14kiriuj0w...`: Ledger expense succeeded, but Harbor/Zelle and Latch reply did not complete.
- `task_dlmkv6otfy07...`: invoice and email work mostly passed, but the transfer/accounting-line check failed.
- `task_a3usg9top92...`: health task passed with clean appointment, refill, payment, cancellation, and calendar checks.

The post-run verifier classified the 20 inspected completed traces as 6 clean passes, 1 pass with high static risk, 5 narrow verifier/state failures, 3 partial completions, 2 environment/navigation failures, 1 task-or-seed ambiguity, and 2 broad side-effect failures.

## How To Run

From the repo root, with the dashboard dataset JSONL and API exports available locally:

```bash
python3 triage_dataset.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --task-api-json path/to/tasks_all.json \
  --sessions-json path/to/sessions_all.json \
  --require-sessions \
  --out-dir reports
```

Then generate the verifier-constant worklist:

```bash
python3 constant_derivability_worklist.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

Then classify completed-run evidence after model runs have finished:

```bash
python3 post_run_verifier.py \
  --trace-evidence trace_evidence.md \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

If you download raw completed-session transcripts from the dashboard, run the same post-run layer at larger scale:

```bash
python3 post_run_verifier.py \
  --transcript-dir path/to/downloaded/session_transcripts \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

## How To Read The Ranked CSV

Open `reports/task_recovery_ranked.csv`. The most useful columns are:

| Column | Meaning |
| --- | --- |
| `recovery_rank` | Suggested order for review. |
| `bucket` | Recovery category. |
| `recommended_action` | What a reviewer should do next. |
| `risk_score` | Static risk score from the triage script. |
| `session_count` / `completed_sessions` | Run coverage from session metadata. |
| `primary_reason` | Plain-English summary of why the task landed where it did. |
| `findings` | Machine-readable QA flags. |
| `verifier_only_amounts` / `verifier_only_user_values` | Hidden verifier constants to prove. |

## What The Tool Flags

Static triage flags:

- Relative-date anchors that need a shared current-date interpretation.
- Cross-system tasks with many app dependencies.
- Conditional branches and lookup-heavy prompts.
- Prompt app cues that do not appear in verifier app usage.
- Verifier-only money amounts, dates, names, emails, and phone numbers.
- Health and finance side effects that deserve careful review.

Post-run verification categories:

- `PASS_CLEAN`
- `PASS_BUT_STATIC_RISK`
- `NARROW_VERIFIER_FAILURE`
- `PARTIAL_COMPLETION`
- `ENVIRONMENT_OR_NAVIGATION_FAILURE`
- `TASK_OR_SEED_AMBIGUITY`
- `BROAD_SIDE_EFFECT_FAILURE`
- `UNSCORED_OR_TRACE_UNAVAILABLE`

These flags are review leads. They are not automatic failures.

## Known Limits

- The scripts are static QA accelerators, not final graders.
- The scripts do not open seed databases or session recordings by themselves; `trace_evidence.md` documents a manual dashboard trace sample, and `post_run_verifier.py` parses that evidence or downloaded transcripts.
- The dashboard score snapshot is aggregate; it is not joined to each task row.
- Verifier-only constants are not always bad. Many are valid hidden ground truth if they are uniquely derivable.
- App mapping is heuristic, especially where health billing and finance billing use similar words.
- Human review is still required before promoting or rejecting tasks.

## What I Would Build Next

The next improvement would connect `reports/derivability_worklist.csv` directly to seed-data probes or session traces. That would turn each hidden verifier constant into one of three labels: derivable, ambiguous, or not derivable. I would also add a lightweight review UI so operators can approve, repair, or reject tasks while preserving the evidence trail.
