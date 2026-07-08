# Live Dashboard Check

Checked in Chrome on July 7, 2026.

## Dashboard Dataset View

- Dataset: `JUNE24-PSI-UNDELIVERED-EVALED`
- URL checked: `https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED`
- Dashboard task count: 257 tasks.
- Total sessions: 712.
- Scored sessions: 658.
- Tasks scored: 220.
- Overall pass rate: 7.6%.
- Overall average score: 0.08.

This dashboard view is the source of truth for the 257-task scope used in the committed reports.

## Model Breakdown

| Model | Pass rate | Avg score | Tasks | Scored sessions | Total sessions |
| --- | ---: | ---: | ---: | ---: | ---: |
| `anthropic/claude-opus-4.8` | 12.4% | 0.12 | 220 | 314 | 336 |
| `openai/gpt-5.5` | 6% | 0.06 | 104 | 182 | 183 |
| `qwen/qwen3.6-plus` | 0% | 0 | 125 | 125 | 139 |
| `qwen/qwen3.6-27b` | 0% | 0 | 24 | 36 | 52 |
| `anthropic/claude-fable-5` | 0% | 0 | 1 | 1 | 2 |

## Task-Set Check

The live Tasks tab shows the same dataset slug and a 257-task table. I spot-checked visible task prefixes from the dashboard against the generated `reports/task_triage.csv`; all checked keys were present in the scoped local analysis:

- `task_nw14kiriuj0w`
- `task_dlmkv6otfy07`
- `task_hdtrki2gbci`
- `task_trdudiabd5z`
- `task_k6hyu6r1uar1`

Interpretation: this is the Project One dataset used for the deliverable, and the generated reports match the visible 257-task dashboard scope.

## How I Use The Scores

The dashboard scores are useful calibration: a 7.6% overall pass rate confirms that the dataset has real quality/recovery work to do. I do not use the aggregate pass rate as a shipping decision for individual tasks, because the committed session API export did not expose per-task score fields. The task-level handoff still relies on:

- `reports/task_recovery_ranked.csv` for the ordered recovery queue;
- `reports/task_triage.csv` for static QA signals and bucket assignment;
- `reports/derivability_worklist.csv` for verifier constants that need proof;
- `evidence_log.md` for the human-reviewed sample.
