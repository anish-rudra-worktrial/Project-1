# Project One QA Toolkit

This package runs a repeatable QA pass over the Fleet Project One dataset export. It is designed to speed up review, not replace it: the output is a prioritized review queue with explainable flags and concrete proof obligations for a human reviewer.

## GitHub Handoff

Upload this folder as the Project One repository/root. The dataset export itself is not committed; download/export it from the Fleet dashboard and pass its local path into the scripts. The most important files for reviewers are:

- `final_project_one_report.md`: concise findings and recovery strategy.
- `triage_dataset.py`: full-dataset static triage script.
- `constant_derivability_worklist.py`: verifier-constant proof-obligation script.
- `reports/task_triage.csv`: one row per task, bucketed for review.
- `reports/derivability_worklist.csv`: hidden verifier constants that need seed/session proof.
- `evidence_log.md` and `verification_sample.md`: human-in-the-loop checks showing how I audited the tool output.
- `live_dashboard_check.md` and `mixed_batch_run_plan.md`: live dashboard/session run notes.

Do not upload API keys, browser cookies, bearer tokens, or local dashboard request headers. The repo is meant to contain the tool, generated reports, and human QA evidence.

## What It Does

- Reads the exported dataset JSONL.
- Extracts prompt app cues, verifier app usage, relative dates, lookup burden, conditional branches, money literals, and dependency types.
- Compares prompt app families against verifier app families.
- Surfaces verifier-only amounts and user-visible constants that may need derivability checks.
- Optionally joins dashboard task/session API exports so each task row includes run count, status count, and model coverage.
- Writes a CSV, JSON, summary report, and manual review queue.

The second layer, `constant_derivability_worklist.py`, takes the most important static signal and makes it actionable:

- Extracts hidden verifier amounts, dates, names/labels, emails, and phone numbers.
- Filters out prompt-mentioned constants by default.
- Adds likely source app, task bucket, risk score, session count, verifier context, and a review question.
- Produces a worklist for proving whether each verifier constant is uniquely derivable from seed data.

## How To Run

From the repo root, with the dataset JSONL available locally:

```bash
python3 triage_dataset.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --out-dir reports
```

With optional session enrichment:

```bash
python3 triage_dataset.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --task-api-json path/to/tasks_all.json \
  --sessions-json path/to/sessions_all.json \
  --out-dir reports
```

Then generate the constant-derivability worklist:

```bash
python3 constant_derivability_worklist.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

Generated files:

- `final_project_one_report.md`: final writeup with methodology, bucket counts, evidence sample summary, and next steps.
- `evidence_log.md`: human-in-the-loop sample review across buckets and environments.
- `reports/task_triage.csv`: one row per task with tags, scores, and bucket.
- `reports/task_triage.json`: same data as JSON.
- `reports/summary.md`: dataset-level counts and top review queues.
- `reports/manual_review_queue.md`: top 50 manual-review candidates with checkboxes.
- `reports/derivability_worklist.csv`: one row per hidden verifier constant that should be proven against seed/session evidence.
- `reports/derivability_worklist.json`: same derivability worklist as JSON.
- `reports/derivability_summary.md`: summary of constant counts by type, source app, bucket, and priority.
- `verification_sample.md`: small sample showing where the tool was useful and where it over-flagged.
- `session_api_notes.md`: explanation of task records versus model-run sessions.
- `live_dashboard_check.md`: Chrome dashboard check covering sessions, charts, discussion, Task Quality, and the spot-check run I created.
- `mixed_batch_run_plan.md`: stratified 48-task run plan and dashboard job metadata for the mixed batch validation run.

## Current Results

On the `JUNE24-PSI-UNDELIVERED-EVALED` export:

- 520 tasks total.
- 313 consumer-finance tasks.
- 207 personal-health tasks.
- 712 sessions joined to 257 tasks. This does not mean there are only 257 tasks; it means 257 of the 520 tasks currently have at least one visible run/session record in the observed dashboard API response.
- A later live dashboard spot check showed 713 total sessions after creating one single-task spot-check run.
- A mixed 48-task batch run was created from a stratified sample across both environments and all four triage buckets. A later dashboard recheck showed 761 total sessions, 7 scored sessions, 6 scored tasks, 28.6% pass rate, and 0.29 average score on the scored slice.
- Static buckets: 39 low-risk spot-check candidates, 201 close/verify-derivability, 214 repair candidates, 66 high-risk manual-review tasks.
- Derivability worklist: 3,729 hidden verifier constants across 513 tasks, including 1,462 amounts, 1,425 dates, 606 names/labels, 222 emails, and 14 phone numbers.

That second number is not a rejection count. It is the review workload made explicit: for each flagged constant, the human question is whether the value is uniquely derivable from the prompt plus seed world.

## What Session Enrichment Means

In Fleet's dashboard, a task is the authored prompt/verifier/environment record. A session is an execution attempt against a task, usually from a model run or evaluation job. One task can have zero sessions, one session, or several sessions from different models. In this dataset, the dashboard showed 712 total sessions across 257 distinct tasks, while the dataset itself still contains 520 tasks.

The session API data used here came from the dashboard's own task/session listing calls. It currently gives useful coverage signals such as run count, model name, and status (`completed`, `errored`, `cancelled`, or `in_progress`). The observed response did not include verifier scores or pass/fail results, so the tool does not treat session count as quality by itself.

## Known Limits

- It does not open the seeded environment databases or session recordings.
- App mapping is heuristic. For example, health billing language can be over-mapped to Ledger/QuickBooks.
- Verifier-only amounts or names are not automatically bad; they may be valid hidden ground truth that the agent is supposed to derive.
- The derivability worklist is intentionally conservative. It can still include harmless verifier constants or no-change guards.
- Session records currently provide status/model coverage, but no verifier scores were present in the observed API response.
- The later live dashboard recheck surfaced only 7 scored sessions across 6 tasks, so run results should be treated as a smoke test rather than a dataset-level conclusion.
- API keys and session headers are intentionally excluded from these files. Use local environment variables or dashboard-authenticated exports rather than publishing live credentials.

## What I Would Build Next

Given more time, I would connect the derivability worklist directly to recordings/traces as they become visible. I would also add environment probes that launch or inspect seed databases for targeted verifier constants, turning “likely hidden ground truth” into “derivable / not derivable / ambiguous.” Finally, I would add a lightweight review UI where a human can approve, repair, or reject each task while preserving the evidence trail.
