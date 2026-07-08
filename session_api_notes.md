# Session API Notes

## Why 712 Sessions But Only 257 Tasks?

The dataset has 520 tasks. A task is a prompt/verifier/environment record.

The dashboard session API returned 712 sessions. A session is one model or agent run against a task. Sessions are many-to-one with tasks: one task can have multiple sessions, and some tasks can have none.

At the time of this pull, the 712 session rows mapped to 257 distinct task IDs. That means 257 tasks had at least one visible run/session, while 263 of the 520 tasks had no session rows visible yet.

Fleet later clarified that the no-session tasks can be dropped from Project One for now. The committed reports therefore use the 257 session-backed tasks as the main scope and exclude the 263 unrun tasks.

## What The Session API Returned

The observed session response included fields like:

- `model`
- `eval_task`, which is the internal task UUID
- `status`
- `job_id`
- model/provider join metadata

The task list API maps the internal task UUID back to the human-readable task key. The triage tool joins those two API responses before adding session counts and model coverage to the CSV.

## What It Did Not Return Yet

The session response I observed did not include verifier scores, pass/fail grading, recording payloads, or full traces. The dashboard may expose recordings from task detail pages once access finishes propagating, but those were not part of the session metadata response used in this first pass.

## Dashboard Recheck

I also checked the dataset and a sample session in the dashboard. The dataset page showed:

- 520 tasks.
- 712 total sessions.
- 0 scored tasks.
- 0 scored sessions.
- Model run counts for `gpt-5.5`, `claude-opus-4.8`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-27b`, and `claude-fable-5`.

A sample task detail page exposed session links and job links. A sampled session page showed `Completed`, model/duration metadata, and a Theatre/Timeline interface, but the visible fields still had blank score/tokens, `Step: 0 / 0`, and `No conversation found`. That makes the session layer useful for coverage metadata, but not enough to use as pass/fail evidence in the deliverable.

## About The Team API Key

The key mentioned by the team is for programmatic access to Fleet APIs. I intentionally do not put live keys, bearer tokens, session headers, cookies, or Supabase authorization headers in public output files. The safer public pattern is to document the variable name and keep the real value local, for example `FLEET_API_KEY`.
