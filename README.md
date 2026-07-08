# Project One QA Toolkit

This repo is a handoff for Fleet Project One. It contains a repeatable QA workflow for deciding which tasks in `JUNE24-PSI-UNDELIVERED-EVALED` are easiest to recover, which need repair, and which should go to deeper manual review.

The goal is not to let an LLM decide what ships. The goal is to make the repetitive QA work faster, consistent, and easy for a human reviewer to audit.

## Start Here

| If you are... | Open first | Why |
| --- | --- | --- |
| A product manager or operator | `SUBMISSION.md` | Short scope, outputs, and bottom-line handoff. |
| Reviewing task quality | `reports/task_recovery_ranked.csv` | Ordered queue of tasks to spot-check, recover, repair, or manually review. |
| Reviewing the analysis | `final_project_one_report.md` | Concise method, findings, bucket counts, and next steps. |
| Reviewing the tool | `triage_dataset.py` and `constant_derivability_worklist.py` | The two scripts that generate the QA outputs. |
| Checking human judgment | `evidence_log.md` | Manual sample showing how I audited the tool output. |

## Current Scope

Fleet clarified that tasks with no visible runs can be dropped from this analysis for now. I therefore scoped the committed analysis to the run-backed/evaluated slice.

| Item | Count |
| --- | ---: |
| Original local export | 520 tasks |
| In-scope session-backed tasks | 257 tasks |
| Dropped no-session tasks | 263 tasks |
| Consumer-finance tasks in scope | 150 tasks |
| Personal-health tasks in scope | 107 tasks |
| Total sessions in scope | 712 sessions |
| Scored sessions on corrected dashboard | 658 sessions |
| Tasks scored on corrected dashboard | 220 tasks |
| Dashboard pass rate | 7.6% |
| Dashboard average score | 0.08 |

The downloaded JSONL export still contains 520 rows. The corrected live dashboard shows 257 tasks, matching the session-backed scope used here.

## Main Deliverables

| File | What it is for |
| --- | --- |
| `reports/task_recovery_ranked.csv` | Main recovery queue. Start here when deciding what to review next. |
| `reports/task_triage.csv` | Full task-level static QA output with risk score, bucket, findings, session count, and prompt preview. |
| `reports/derivability_worklist.csv` | Verifier constants that need proof from the prompt, seed data, or session evidence. |
| `reports/manual_review_queue.md` | Top 50 high-risk tasks with manual-review checklist prompts. |
| `final_project_one_report.md` | Summary of method, results, recovery strategy, and limits. |
| `evidence_log.md` | Human-in-the-loop sample across buckets and environments. |
| `live_dashboard_check.md` | Corrected dashboard score snapshot and task-set check. |

The dataset export, API keys, browser cookies, bearer tokens, and local request headers are intentionally not committed.

## How The Workflow Works

1. Scope the dataset to tasks with visible sessions, per Fleet guidance.
2. Run static triage over each task prompt and verifier.
3. Bucket each task by recovery priority.
4. Extract verifier constants that are not obviously present in the prompt.
5. Turn those constants into proof questions for a human reviewer.
6. Validate the approach with a manual sample across buckets and environments.

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

## How To Run

From the repo root, with the dataset JSONL and dashboard API exports available locally:

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

For a broader static-only exploration pass, omit the session arguments and `--require-sessions`.

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

- Relative-date anchors that need a shared current-date interpretation.
- Cross-system tasks with many app dependencies.
- Conditional branches and lookup-heavy prompts.
- Prompt app cues that do not appear in verifier app usage.
- Verifier-only money amounts, dates, names, emails, and phone numbers.
- Health and finance side effects that deserve careful review.

These flags are review leads. They are not automatic failures.

## Known Limits

- The scripts are static QA accelerators, not final graders.
- The tool does not open seed databases or session recordings.
- The corrected dashboard score snapshot is aggregate; it is not joined to each task row.
- Verifier-only constants are not always bad. Many are valid hidden ground truth if they are uniquely derivable.
- App mapping is heuristic, especially where health billing and finance billing use similar words.
- Human review is still required before promoting or rejecting tasks.

## What I Would Build Next

The next improvement would connect `reports/derivability_worklist.csv` directly to seed-data probes or session traces. That would turn each hidden verifier constant into one of three labels: derivable, ambiguous, or not derivable. I would also add a lightweight review UI so operators can approve, repair, or reject tasks while preserving the evidence trail.
