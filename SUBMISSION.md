# Project One Submission Note

## Scope

The dataset export contains 520 tasks. After Fleet clarified that tasks with no visible sessions can be dropped for this project, the committed analysis is scoped to the 257 tasks with at least one visible session row.

- Included: 257 session-backed tasks.
- Dropped: 263 unrun/no-session tasks.
- In-scope environments: 150 consumer-finance tasks and 107 personal-health tasks.
- Session metadata joined: 712 sessions.

## Main Outputs

- `final_project_one_report.md`: concise writeup of method, results, recovery path, and limits.
- `reports/task_triage.csv`: ranked task-level triage with bucket, risk score, session count, findings, and prompt preview.
- `reports/manual_review_queue.md`: top 50 session-backed tasks by QA risk.
- `reports/derivability_worklist.csv`: verifier constants that need proof against seed/session evidence.
- `evidence_log.md`: human-in-the-loop sample across buckets and environments.
- `live_dashboard_check.md`: notes from dashboard/session/job inspection.

## Buckets

- `A_likely_good_spot_check`: 17 tasks.
- `B_close_verify_derivability`: 92 tasks.
- `C_repair_candidate`: 109 tasks.
- `D_high_risk_manual_review`: 39 tasks.

The ranking is not pass/fail. It is a recovery queue: start with low-risk spot checks and close/derivability tasks, then repair candidates, then high-risk manual review.

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

## Limits

The scripts are static QA accelerators. They do not replace seed-world or recording review, and they do not use an LLM as the final judge. Session metadata was useful for coverage, but scored run evidence was sparse at the time of review.
