# Project One: Task Analysis And QA Sweep

## Executive Summary

I reviewed the `JUNE24-PSI-UNDELIVERED-EVALED` dataset with a four-layer process:

1. A repeatable static QA tool that scored the 257-task scope from the Fleet dashboard dataset.
2. A derivability worklist that extracts hidden verifier constants from that scoped task set and turns them into concrete review questions.
3. A dashboard trace sample that inspected completed sessions and captured actual verifier pass/fail output.
4. A post-run verifier that converts completed-run evidence into an auditable repair/promote queue.

I also kept a human evidence log across buckets to check prompt/verifier/session alignment, with the dashboard score snapshot used as supporting evidence rather than the final judge.

The goal was not to let an LLM decide what ships. The goal was to build a system that narrows the review queue, exposes likely failure modes, and leaves a human reviewer in control of the final call.

## Dataset Shape

- Source of truth: [Fleet dashboard dataset](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).
- Dashboard view checked on July 7, 2026: 257 tasks.
- In-scope tasks analyzed: 257 dashboard-scoped tasks.
- In-scope consumer finance tasks: 150.
- In-scope personal health tasks: 107.
- Current date in task environments: `2025-10-14`.
- Session metadata joined: 712 sessions across the 257 in-scope tasks.
- Dashboard score snapshot: 220 tasks scored, 658 scored sessions, 712 total sessions, 7.6% overall pass rate, and 0.08 overall average score.
- The observed session API export did not include row-level score fields, so score data is recorded as a dashboard-level snapshot rather than joined into each task row.
- Hidden verifier constants surfaced for review in the in-scope set: 1,843 across 254 tasks.
- Completed dashboard traces manually inspected for this handoff: 20 sessions, 5 from each recovery bucket.

## Static Triage Results

| Bucket | Count | Meaning |
| --- | ---: | --- |
| `A_likely_good_spot_check` | 17 | Low static risk. Should be spot-checked against seed/session evidence before promotion. |
| `B_close_verify_derivability` | 92 | Likely recoverable. Main work is proving hidden verifier constants are derivable from the world. |
| `C_repair_candidate` | 109 | Worth saving, but likely needs prompt/verifier reconciliation or stronger seed checks. |
| `D_high_risk_manual_review` | 39 | Highest risk. Review before spending recovery time. |

This means a conservative recovery path is:

- Promote the 17 likely-good tasks only after spot checks.
- Work the 92 close tasks next; many are probably recoverable if seed data supports the hidden answers.
- Use the 109 repair candidates as the main fix backlog.
- Treat the 39 high-risk tasks as manual-review-first, not automatic rejects.

## Tool Built

I built three scripts.

`triage_dataset.py` reads the dashboard dataset JSONL, joins task/session API exports, and applies the dashboard task scope used in this handoff.

It flags:

- relative date anchors;
- cross-system dependency load;
- conditional branching;
- lookup burden;
- prompt app cues versus verifier app usage;
- verifier-only amounts;
- verifier-only user-visible constants;
- health/finance side-effect risk;
- session counts and model coverage when available.

`constant_derivability_worklist.py` is the second pass. It extracts verifier constants that are not obviously present in the prompt and adds:

- constant type: amount, date, name/label, email, or phone;
- likely source app;
- triage bucket and risk score;
- verifier context;
- a human-readable derivability question.

`post_run_verifier.py` is the post-run pass. It does not run models. It parses completed-run evidence from `trace_evidence.md` or downloaded session transcripts, joins back to static triage when it can, and classifies observed outcomes into:

- `PASS_CLEAN`
- `PASS_BUT_STATIC_RISK`
- `NARROW_VERIFIER_FAILURE`
- `PARTIAL_COMPLETION`
- `ENVIRONMENT_OR_NAVIGATION_FAILURE`
- `TASK_OR_SEED_AMBIGUITY`
- `BROAD_SIDE_EFFECT_FAILURE`
- `UNSCORED_OR_TRACE_UNAVAILABLE`

Outputs:

- `reports/task_triage.csv`
- `reports/task_recovery_ranked.csv`
- `reports/task_triage.json`
- `reports/summary.md`
- `reports/manual_review_queue.md`
- `reports/derivability_worklist.csv`
- `reports/derivability_worklist.json`
- `reports/derivability_summary.md`
- `reports/post_run_verification.csv`
- `reports/post_run_verification.json`
- `reports/post_run_verification_summary.md`
- `trace_evidence.md`
- `evidence_log.md`
- `live_dashboard_check.md`

`reports/task_recovery_ranked.csv` is the clearest task-level ranking: it orders every in-scope task by recovery priority and includes the bucket, recommended action, risk score, run coverage, primary reason, and task key.

The scoped derivability worklist found 689 amounts, 710 dates, 315 names/labels, 120 emails, and 9 phone numbers that should be proven against seed/session evidence before promotion.

## Actual Trace Findings

I added a 20-session trace-backed spot check in `trace_evidence.md` because the strongest signal is not just "this task looks risky"; it is what actually happened when a model ran it.

| Bucket | Traces reviewed | What the traces showed |
| --- | ---: | --- |
| `A_likely_good_spot_check` | 5 | Several real pass traces, plus narrow failures around final sent/done state. This bucket is worth checking first. |
| `B_close_verify_derivability` | 5 | Many runs were close: successful prompt steps with missing final side effects such as Zelle payments, calendar events, or sent state. |
| `C_repair_candidate` | 5 | Repairable failures appeared often: unexpected message inserts, wrong transfer/accounting lines, blocked app navigation, or one missing side-effect path. |
| `D_high_risk_manual_review` | 5 | Mixed evidence: one high-risk task passed, but most traces showed ambiguity, broad missing side effects, or environment-sensitive actions. |

Concrete examples from the trace sample:

- `task_itcgbzweb4f...` passed with exactly 2 transfers, 4 transaction records, and no unexpected changes.
- `task_dlmkv6otfy07...` failed only after late-charge invoices and three follow-up emails passed; the narrow failure was missing 4 transaction lines.
- `task_us4sqtokm...` exposed a true task/seed ambiguity: no single doctor satisfied all stated constraints.

The full 20-row trace matrix is in `trace_evidence.md`.

I then ran those 20 inspected traces through `post_run_verifier.py`. The post-run queue classified them as:

| Post-run category | Count |
| --- | ---: |
| `PASS_CLEAN` | 6 |
| `PASS_BUT_STATIC_RISK` | 1 |
| `NARROW_VERIFIER_FAILURE` | 5 |
| `PARTIAL_COMPLETION` | 3 |
| `ENVIRONMENT_OR_NAVIGATION_FAILURE` | 2 |
| `TASK_OR_SEED_AMBIGUITY` | 1 |
| `BROAD_SIDE_EFFECT_FAILURE` | 2 |

These traces change the recovery plan:

- Promote or near-promote tasks with clean pass traces and low static risk first.
- Treat narrow verifier failures as repair candidates, not blanket rejects.
- Separate partial-completion or environment-navigation failures from prompt/verifier quality failures.
- Use static triage to choose what to inspect, then use traces to decide the actual action.

## Most Common Static Signals

| Finding | Count |
| --- | ---: |
| Finance side-effect review | 195 |
| Many cross-system dependencies | 178 |
| Verifier-only amounts | 121 |
| Health privacy review | 115 |
| Verifier-only user values | 97 |
| Relative date anchors | 93 |
| High branching | 86 |
| Many lookups | 31 |
| Long prompt | 23 |
| Prompt app family missing from verifier | 20 |

## Human QA Sample

I manually sampled eight tasks across all four buckets and both environments. The main question for each task was:

> Are the verifier's hidden constants and expected state changes uniquely derivable from the prompt and seed world?

Summary:

| Task | Bucket | Human decision |
| --- | --- | --- |
| `task_qehlqyjkuoqy_n_1781640416463_7t94nlq5c__ayush_20260624__worktrial_taskloss_20260707` | High-risk finance | Repair candidate until hardcoded expense IDs are proven derivable or replaced with dynamic checks. |
| `task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707` | High-risk health | Manual review required; appointment/billing constants may be valid but need seed proof. |
| `task_ogrtkp7dmz7_n_1781684912333_uubhq8apt__ayush_20260624__worktrial_taskloss_20260707` | Repair finance | Closer than static score suggests; likely good if AT&T / `$165.98` is uniquely derivable. |
| `task_wam3eaul71u_n_1781709090122_r7ys8u6oh__ayush_20260624__worktrial_taskloss_20260707` | Repair health | Close with prompt cleanup; check dentist title/time assumptions. |
| `task_xyxx2vpkrek_n_1781607774982_827vogeju__ayush_20260624__worktrial_taskloss_20260707` | Close finance | Close; verify financial constants before promotion. |
| `task_igpndla7ffq_n_1781736164354_kdb59x0wl__ayush_20260624__worktrial_taskloss_20260707` | Close health | Likely good if provider availability is unique. |
| `task_yktbgqjdiox_n_1781235421200_h1md9xdpg__ayush_20260624__worktrial_taskloss_20260707` | Likely-good finance | Likely good spot-check candidate. |
| `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707` | Likely-good health | Likely good after lab-draw and payment seed check. |

The full manual sample is in `evidence_log.md`; the concrete session examples are in `trace_evidence.md`.

## Common Recovery Patterns

### 1. Hidden Verifier Constants Are The Main Review Target

Many tasks ask the agent to derive a value from the world, while the verifier hardcodes the answer. That is acceptable only if the world makes the answer unique. Examples include specific amounts, doctor names, invoice/customer names, and appointment times.

I built the derivability worklist specifically for this problem. Recommended process: for every verifier-only constant, record whether it is:

- explicitly in the prompt;
- uniquely derivable from seed data;
- plausible but ambiguous;
- not derivable.

### 2. Hardcoded Database IDs Are Risky

Some verifiers check specific row IDs for records the prompt describes dynamically. This is fragile. If seed data changes, the verifier can silently become wrong.

Recommended fix: prefer dynamic lookups by stable user-visible attributes such as vendor, date, amount, doctor name, appointment time, or bill number.

### 3. Health Billing And Finance Billing Need Separate Heuristics

The static tool overflagged one health task because words like `bill`, `payment`, and `balance` look finance-like. The domain matters: Lifeline billing is not Ledger/QuickBooks.

Recommended fix: app-aware heuristics. A bill in Lifeline should map to health billing; a bill in Ledger should map to finance invoicing.

### 4. Dynamic Appointment Tasks Are Recoverable But Need Availability Proof

Health tasks often say “first available,” “latest in the day,” or “first dentist in New York.” These can be good tasks, but only if provider availability makes the intended answer unique.

Recommended fix: add a seed-data uniqueness check for appointment-selection prompts.

### 5. Relative Dates Are Usually Fine If Anchored

All tasks are anchored to `2025-10-14`, so words like “today,” “yesterday,” and “this week” are not automatically bad. They are review flags because prompt/verifier/calendar systems must agree on the same current date.

## Recommended Human Review Workflow

1. Run the triage tool with session exports and `--require-sessions` so the analysis matches the Fleet dashboard scope.
2. Run the derivability worklist and filter to high-priority rows in `D_high_risk_manual_review`, then `C_repair_candidate`, then `B_close_verify_derivability`.
3. Start with tasks that have sessions or many hidden constants.
4. For each task, inspect prompt, verifier, session metadata, and visible recordings/traces where available.
5. Fill an evidence row:
   - tool flags;
   - trace status, score, model, and final verifier output;
   - verifier-only constants;
   - seed derivability result;
   - final decision;
   - repair recommendation.
6. Run `post_run_verifier.py` over the trace evidence or downloaded completed-session transcripts.
7. Promote only tasks where the verifier checks the same task the prompt describes.

## What I Would Do Next

Immediate next pass:

- Deep-check the top 10 high-risk tasks with sessions/recordings.
- Spot-check 10 likely-good tasks with recordings or fresh single-task runs.
- Verify all verifier-only constants for those 20 tasks against seed data or recordings.
- Rebucket based on evidence, not static score alone.

Two-week system build:

- Add seed-data probes for the derivability worklist.
- Add a small reviewer UI that shows prompt, verifier constants, session coverage, and decision fields side by side.
- Add task-writer lint checks for app naming, hardcoded IDs, ambiguous dynamic criteria, and unverified prompt requirements.
- Add monitoring for pass-rate drift once tasks ship.

## Known Limits

- The static tool is not a substitute for seed-world verification.
- The derivability worklist is conservative and may include harmless verifier constants or no-change guards.
- The post-run verifier is rule-based and intentionally transparent; it organizes completed evidence but does not replace human judgment.
- The observed session API export did not include pass/fail scores or traces; trace details were inspected manually through the dashboard session viewer for the documented sample.
- The live score snapshot is aggregate, not task-row-level in the committed CSV. I did not treat pass rate as a replacement for prompt/verifier/seed QA.
- I did not use an LLM batch reviewer as the final judge.
- The current evidence sample covers 8/257 in-scope tasks manually, with 20 completed dashboard traces inspected in detail.

## Bottom Line

The dashboard scope likely contains a meaningful number of recoverable tasks. The fastest safe path is not to hand-review all 257 in-scope tasks from scratch; it is to use the tool to prioritize, then inspect actual traces and verifier output for the highest-impact buckets. The strongest recovery pool is the 92 close/verify-derivability tasks plus the 17 likely-good spot-check tasks, with trace-backed passes promoted first and narrow verifier failures routed to repair.
