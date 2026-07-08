# Session API Notes

## Why 712 Sessions But Only 257 Tasks?

The original local export has 520 task definitions. A task is a prompt/verifier/environment record.

The dashboard session API returned 712 sessions. A session is one model or agent run against a task. Sessions are many-to-one with tasks: one task can have multiple sessions, and some tasks can have none.

At the time of this pull, the 712 session rows mapped to 257 distinct task IDs. That means 257 tasks had at least one visible run/session, while 263 of the 520 tasks had no session rows visible yet.

Fleet later clarified that the no-session tasks can be dropped from Project One for now. The committed reports therefore use the 257 session-backed tasks as the main scope and exclude the 263 unrun tasks.

The corrected live dashboard view now also shows 257 tasks, which matches the committed analysis scope.

## What The Session API Returned

The observed session response included fields like:

- `model`
- `eval_task`, which is the internal task UUID
- `status`
- `job_id`
- model/provider join metadata

The task list API maps the internal task UUID back to the human-readable task key. The triage tool joins those two API responses before adding session counts and model coverage to the CSV.

## What It Did Not Return

The session response I observed did not include verifier scores, pass/fail grading, recording payloads, or full traces. Those fields were not part of the session metadata response used by the scripts.

## Dashboard Recheck

I rechecked the corrected live dashboard page on July 7, 2026. The dataset page showed:

- 257 tasks.
- 712 total sessions.
- 220 scored tasks.
- 658 scored sessions.
- 7.6% overall pass rate.
- 0.08 overall average score.

Model-level dashboard aggregate:

| Model | Pass rate | Avg score | Tasks | Scored sessions | Total sessions |
| --- | ---: | ---: | ---: | ---: | ---: |
| `anthropic/claude-opus-4.8` | 12.4% | 0.12 | 220 | 314 | 336 |
| `openai/gpt-5.5` | 6% | 0.06 | 104 | 182 | 183 |
| `qwen/qwen3.6-plus` | 0% | 0 | 125 | 125 | 139 |
| `qwen/qwen3.6-27b` | 0% | 0 | 24 | 36 | 52 |
| `anthropic/claude-fable-5` | 0% | 0 | 1 | 1 | 2 |

That makes the score layer useful as calibration, but not enough to replace task-level QA in the deliverable. The script still ranks tasks based on prompt/verifier/session metadata because the observed API export does not include score fields per task row.

## About The Team API Key

The key mentioned by the team is for programmatic access to Fleet APIs. I intentionally do not put live keys, bearer tokens, session headers, cookies, or Supabase authorization headers in public output files. The safer public pattern is to document the variable name and keep the real value local, for example `FLEET_API_KEY`.
