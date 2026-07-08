# Project One QA Toolkit

This repo is a Fleet Project One handoff.

It contains a repeatable QA workflow for deciding which tasks in `JUNE24-PSI-UNDELIVERED-EVALED` are good, which are close, which need repair, and which need deeper manual review.

The goal is to protect the training signal for agents. A task can fail because the prompt is unclear, the verifier checks hidden facts, the model misses a step, or the environment/tooling gets in the way. This repo separates those cases so a human reviewer can make a cleaner decision.

## Start Here

Recommended entry points:

| Open | Why |
| --- | --- |
| [SUBMISSION.md](SUBMISSION.md) | Short handoff: scope, outputs, bucket counts, and how to run the tools. |
| [reports/task_recovery_ranked.csv](reports/task_recovery_ranked.csv) | The main task queue, sorted by what to review first. |
| [reports/post_run_verification_summary.md](reports/post_run_verification_summary.md) | The completed-run trace summary: clean passes, narrow repairs, partial completions, environment issues, ambiguity, and broad failures. |

For the fuller explanation, read [final_project_one_report.md](final_project_one_report.md).

## The Three QA Layers

The workflow has three QA layers. The first two are static checks over the task/verifier. The third is a post-run check over completed traces.

| Layer | Human Name | What It Answers | Script | Main Output |
| --- | --- | --- | --- | --- |
| 1 | Static task triage | "Which tasks look easiest to recover, and which look risky?" | [triage_dataset.py](triage_dataset.py) | [reports/task_recovery_ranked.csv](reports/task_recovery_ranked.csv) |
| 2 | Verifier constant review | "Is the verifier checking facts the agent could actually derive?" | [constant_derivability_worklist.py](constant_derivability_worklist.py) | [reports/derivability_worklist.csv](reports/derivability_worklist.csv) |
| 3 | Post-run trace review | "What actually happened when a model ran the task?" | [post_run_verifier.py](post_run_verifier.py) | [reports/post_run_verification.csv](reports/post_run_verification.csv) |

There are also two human-readable evidence files:

| File | What It Shows |
| --- | --- |
| [trace_evidence.md](trace_evidence.md) | 20 real completed traces: 5 from each bucket. |
| [verification_sample.md](verification_sample.md) | A readable sample explaining static checks plus the 5-traces-per-bucket trace calibration. |

## Layer 1: Static Task Triage

This is the first pass.

It reads the task dataset and checks each prompt/verifier for review signals:

- too many cross-system dependencies;
- relative date anchors;
- high branching or lookup burden;
- finance and health side-effect risk;
- prompt apps that may not be verified;
- verifier-only amounts or user-visible facts;
- session coverage when available.

It does not decide whether a task is good or bad. It creates a review queue.

Outputs:

- [reports/task_recovery_ranked.csv](reports/task_recovery_ranked.csv): best first file for task review.
- [reports/task_triage.csv](reports/task_triage.csv): full task-level static QA table.
- [reports/manual_review_queue.md](reports/manual_review_queue.md): top high-risk tasks.
- [reports/summary.md](reports/summary.md): static triage summary.

## Layer 2: Verifier Constant Review

This is the second pass.

It looks for constants inside verifiers that are not obvious in the prompt, such as:

- money amounts;
- dates;
- names and labels;
- emails;
- phone numbers.

Those constants are not automatically wrong. They are proof obligations. A reviewer should confirm whether each one is uniquely derivable from the prompt plus the seed world.

Outputs:

- [reports/derivability_worklist.csv](reports/derivability_worklist.csv): verifier constants to prove.
- [reports/derivability_summary.md](reports/derivability_summary.md): summary of constant counts and types.

## Layer 3: Post-Run Trace Review

This is the third pass.

It runs after model sessions already exist. It does not create Fleet runs, submit model responses, or post anything to Fleet's platform.

It parses completed-run evidence from:

- [trace_evidence.md](trace_evidence.md), or
- downloaded completed-session transcripts.

Then it classifies what happened:

- `PASS_CLEAN`
- `PASS_BUT_STATIC_RISK`
- `NARROW_VERIFIER_FAILURE`
- `PARTIAL_COMPLETION`
- `ENVIRONMENT_OR_NAVIGATION_FAILURE`
- `TASK_OR_SEED_AMBIGUITY`
- `BROAD_SIDE_EFFECT_FAILURE`
- `UNSCORED_OR_TRACE_UNAVAILABLE`

Outputs:

- [reports/post_run_verification.csv](reports/post_run_verification.csv): sortable completed-run QA queue.
- [reports/post_run_verification_summary.md](reports/post_run_verification_summary.md): readable post-run summary.

## Current Results

Source of truth: [JUNE24-PSI-UNDELIVERED-EVALED](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED)

| Metric | Count |
| --- | ---: |
| Dashboard task scope | 257 tasks |
| Consumer-finance tasks | 150 tasks |
| Personal-health tasks | 107 tasks |
| Total sessions joined | 712 sessions |
| Scored sessions on dashboard | 658 sessions |
| Tasks scored on dashboard | 220 tasks |
| Completed traces inspected | 20 sessions |

Static task buckets:

| Bucket | Count | Human Meaning |
| --- | ---: | --- |
| `A_likely_good_spot_check` | 17 | Start here. Low static risk; spot-check before promotion. |
| `B_close_verify_derivability` | 92 | Likely recoverable; prove hidden constants are derivable. |
| `C_repair_candidate` | 109 | Worth saving, but needs prompt/verifier/seed repair. |
| `D_high_risk_manual_review` | 39 | Inspect manually before spending repair time. |

Post-run trace summary from the 20 inspected completed sessions:

| Post-Run Category | Count |
| --- | ---: |
| `PASS_CLEAN` | 6 |
| `PASS_BUT_STATIC_RISK` | 1 |
| `NARROW_VERIFIER_FAILURE` | 5 |
| `PARTIAL_COMPLETION` | 3 |
| `ENVIRONMENT_OR_NAVIGATION_FAILURE` | 2 |
| `TASK_OR_SEED_AMBIGUITY` | 1 |
| `BROAD_SIDE_EFFECT_FAILURE` | 2 |

## How To Run

Run these commands from the repo root in Terminal.

The generated reports are already committed. You only need to rerun the scripts if you have fresh Fleet exports or new completed-session transcripts.

### 1. Run Static Task Triage

```bash
python3 triage_dataset.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --task-api-json path/to/tasks_all.json \
  --sessions-json path/to/sessions_all.json \
  --require-sessions \
  --out-dir reports
```

### 2. Run Verifier Constant Review

```bash
python3 constant_derivability_worklist.py \
  path/to/JUNE24-PSI-UNDELIVERED-EVALED.jsonl \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

### 3. Run Post-Run Trace Review

Use the committed trace evidence:

```bash
python3 post_run_verifier.py \
  --trace-evidence trace_evidence.md \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

Or use downloaded completed-session transcripts:

```bash
python3 post_run_verifier.py \
  --transcript-dir path/to/downloaded/session_transcripts \
  --triage-csv reports/task_triage.csv \
  --out-dir reports
```

## Known Limits

- The tools accelerate QA; they do not replace human review.
- The first two scripts are static checks, so they do not prove seed-world truth by themselves.
- The third script parses trace evidence after runs exist; it does not create Fleet runs.
- Verifier-only constants are not automatically bad. They need derivability proof.
- App mapping is heuristic, especially where health billing and finance billing share similar language.
- API keys, browser cookies, bearer tokens, request headers, and raw private exports are intentionally not committed.

## More Detail

| Want More Detail On... | Open |
| --- | --- |
| Overall method and conclusions | [final_project_one_report.md](final_project_one_report.md) |
| Short handoff note | [SUBMISSION.md](SUBMISSION.md) |
| Actual trace examples | [trace_evidence.md](trace_evidence.md) |
| Sample verification logic | [verification_sample.md](verification_sample.md) |
| Session/API notes | [session_api_notes.md](session_api_notes.md) |
| Dashboard score snapshot | [live_dashboard_check.md](live_dashboard_check.md) |
