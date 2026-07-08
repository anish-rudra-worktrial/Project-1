# Project One Submission Note

## Scope

The source of truth for this handoff is the Fleet dashboard dataset:
[JUNE24-PSI-UNDELIVERED-EVALED](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).

The committed analysis covers the 257-task dashboard scope.

- Included: 257 dashboard-scoped tasks.
- In-scope environments: 150 consumer-finance tasks and 107 personal-health tasks.
- Session metadata joined: 712 sessions.
- Dashboard score snapshot: 220 tasks scored, 658 scored sessions, 7.6% overall pass rate, 0.08 overall average score.
- Completed traces manually inspected for this handoff: 20 sessions, 5 from each recovery bucket.

## Main Outputs

- `final_project_one_report.md`: concise writeup of method, results, recovery path, and limits.
- `reports/task_triage.csv`: ranked task-level triage with bucket, risk score, session count, findings, and prompt preview.
- `reports/task_recovery_ranked.csv`: ordered recovery queue with category, recommended action, and reason.
- `trace_evidence.md`: concrete dashboard trace findings from 20 completed runs, 5 from each recovery bucket.
- `reports/post_run_verification.csv`: completed-run evidence converted into pass, repair, ambiguity, environment, and broad-failure queues.
- `reports/post_run_verification_summary.md`: readable summary of the post-run verification layer.
- `reports/manual_review_queue.md`: top 50 dashboard-scoped tasks by QA risk.
- `reports/derivability_worklist.csv`: verifier constants that need proof against seed/session evidence.
- `evidence_log.md`: human-in-the-loop sample across buckets and environments.
- `live_dashboard_check.md`: notes from dashboard/session/job inspection.

## Three QA Layers

| Layer | What it does | Main file |
| --- | --- | --- |
| 1. Static task triage | Ranks tasks by static risk and recovery priority. | `reports/task_recovery_ranked.csv` |
| 2. Verifier constant review | Pulls hidden amounts, dates, names, emails, and phones that need seed-world proof. | `reports/derivability_worklist.csv` |
| 3. Post-run trace review | Classifies completed runs into pass, narrow repair, partial completion, environment issue, ambiguity, or broad failure. | `reports/post_run_verification_summary.md` |

## Buckets

- `A_likely_good_spot_check`: 17 tasks.
- `B_close_verify_derivability`: 92 tasks.
- `C_repair_candidate`: 109 tasks.
- `D_high_risk_manual_review`: 39 tasks.

The ranking is not pass/fail. It is a recovery queue: start with low-risk spot checks and close/derivability tasks, then repair candidates, then high-risk manual review. The explicit queue is in `reports/task_recovery_ranked.csv`.

## Tool

Run the scoped triage:

```bash
python3 triage_dataset.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --task-api-json path/to/tasks_all.json \
  --sessions-json path/to/sessions_all.json \
  --require-sessions \
  --out-dir reports
```

Run the verifier-constant worklist:

```bash
python3 constant_derivability_worklist.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

Run the post-run verifier after traces or completed-session transcripts are available:

```bash
python3 post_run_verifier.py \
  --trace-evidence trace_evidence.md \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

For larger batches, download completed-session transcripts from the dashboard and swap in:

```bash
python3 post_run_verifier.py \
  --transcript-dir path/to/downloaded/session_transcripts \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

## Limits

The scripts are QA accelerators. They do not replace seed-world or recording review, and they do not use an LLM as the final judge. I added a dashboard trace sample and a post-run classifier so the handoff includes actual observed pass/fail behavior, not only static flags. The dashboard has aggregate score data, but the observed session API export did not include row-level scores, so the task-level decision path still rests on prompt/verifier/seed derivability plus visible trace review.
