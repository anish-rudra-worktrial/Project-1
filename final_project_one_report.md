# Project One: Task Analysis And QA Sweep

## Executive Summary

I reviewed the `JUNE24-PSI-UNDELIVERED-EVALED` dataset with a three-layer process:

1. A repeatable static QA tool that scored all 520 tasks.
2. A derivability worklist that extracts hidden verifier constants and turns them into concrete review questions.
3. A human evidence log that sampled tasks across buckets and checked prompt/verifier/session alignment.

The goal was not to let an LLM decide what ships. The goal was to build a system that narrows the review queue, exposes likely failure modes, and leaves a human reviewer in control of the final call.

## Dataset Shape

- Total tasks: 520.
- Consumer finance tasks: 313.
- Personal health tasks: 207.
- Current date in task environments: `2025-10-14`.
- Session metadata joined: 712 sessions across 257 tasks.
- Session rows with verifier scores/traces available in the observed API response: none.
- Live dashboard check after a one-task spot-check run: 713 total sessions, 0 scored sessions, 520/520 tasks not analyzed in Task Quality.
- Later dashboard recheck after the 48-task mixed batch registered: 761 total sessions, 7 scored sessions, 6 scored tasks, 28.6% pass rate, and 0.29 average score on the scored slice.
- Hidden verifier constants surfaced for review: 3,729 across 513 tasks.

## Static Triage Results

| Bucket | Count | Meaning |
| --- | ---: | --- |
| `A_likely_good_spot_check` | 39 | Low static risk. Should be spot-checked against seed/session evidence before promotion. |
| `B_close_verify_derivability` | 201 | Likely recoverable. Main work is proving hidden verifier constants are derivable from the world. |
| `C_repair_candidate` | 214 | Worth saving, but likely needs prompt/verifier reconciliation or stronger seed checks. |
| `D_high_risk_manual_review` | 66 | Highest risk. Review before spending recovery time. |

This means a conservative recovery path is:

- Promote the 39 likely-good tasks only after spot checks.
- Work the 201 close tasks next; many are probably recoverable if seed data supports the hidden answers.
- Use the 214 repair candidates as the main fix backlog.
- Treat the 66 high-risk tasks as manual-review-first, not automatic rejects.

## Tool Built

I built two scripts.

`triage_dataset.py` reads the dataset JSONL and optionally joins task/session API exports.

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

Outputs:

- `reports/task_triage.csv`
- `reports/task_triage.json`
- `reports/summary.md`
- `reports/manual_review_queue.md`
- `reports/derivability_worklist.csv`
- `reports/derivability_worklist.json`
- `reports/derivability_summary.md`
- `evidence_log.md`
- `live_dashboard_check.md`

The derivability worklist found 1,462 amounts, 1,425 dates, 606 names/labels, 222 emails, and 14 phone numbers that should be proven against seed/session evidence before promotion.

## Most Common Static Signals

| Finding | Count |
| --- | ---: |
| Finance side-effect review | 408 |
| Many cross-system dependencies | 337 |
| Verifier-only amounts | 247 |
| Health privacy review | 220 |
| Verifier-only user values | 193 |
| Relative date anchors | 190 |
| High branching | 152 |
| Many lookups | 77 |
| Long prompt | 40 |
| Prompt app family missing from verifier | 34 |

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

The full sample is in `evidence_log.md`.

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

1. Run the triage tool over the full dataset.
2. Run the derivability worklist and filter to high-priority rows in `D_high_risk_manual_review`, then `C_repair_candidate`, then `B_close_verify_derivability`.
3. Start with tasks that have sessions or many hidden constants.
4. For each task, inspect prompt, verifier, session metadata, and visible recordings/traces if available.
5. Fill an evidence row:
   - tool flags;
   - verifier-only constants;
   - seed derivability result;
   - final decision;
   - repair recommendation.
6. Promote only tasks where the verifier checks the same task the prompt describes.

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
- Session metadata did not include pass/fail scores or traces in the observed response.
- The final dashboard recheck showed only 7 scored sessions across 6 tasks, so live run evidence is still sparse and should not be over-weighted.
- I did not use an LLM batch reviewer as the final judge.
- The current evidence sample covers 8/520 tasks manually.

## Bottom Line

The dataset likely contains a meaningful number of recoverable tasks. The fastest safe path is not to hand-review all 520 from scratch; it is to use the tool to prioritize, then manually verify derivability for the highest-impact buckets. The strongest recovery pool is the 201 close/verify-derivability tasks plus the 39 likely-good spot-check tasks.
