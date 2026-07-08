# Post-Run Verification Summary

This report classifies completed model-run evidence after the task has already been executed. It is a post-run QA layer, not a model runner and not an LLM judge.

## Inputs

- `trace_evidence.md`

## Coverage

- Parsed rows: 20
- Passing scored rows: 7
- Failing scored rows: 13
- Unscored or missing-score rows: 0

## Post-Run Categories

| Category | Count | Action |
| --- | ---: | --- |
| `PASS_CLEAN` | 6 | Promote or keep in the near-promote queue after normal spot-check. |
| `PASS_BUT_STATIC_RISK` | 1 | Promote only after one extra human spot-check because static risk was high. |
| `NARROW_VERIFIER_FAILURE` | 5 | Repair the specific verifier/state mismatch, then rerun. |
| `PARTIAL_COMPLETION` | 3 | Repair missing final side effects or rerun with focused review. |
| `ENVIRONMENT_OR_NAVIGATION_FAILURE` | 2 | Separate environment/tooling issue from task quality before rejecting. |
| `TASK_OR_SEED_AMBIGUITY` | 1 | Manual prompt/seed review first; clarify the intended unique answer. |
| `BROAD_SIDE_EFFECT_FAILURE` | 2 | Keep in manual review or major repair; too many durable effects failed. |
| `UNSCORED_OR_TRACE_UNAVAILABLE` | 0 | Inspect the trace manually before making a delivery decision. |

## Static Bucket Coverage

| Static bucket | Parsed rows |
| --- | ---: |
| `A_likely_good_spot_check` | 5 |
| `B_close_verify_derivability` | 5 |
| `C_repair_candidate` | 5 |
| `D_high_risk_manual_review` | 5 |

## Highest-Signal Rows

| Priority | Category | Task | Session | Score | Evidence |
| ---: | --- | --- | --- | ---: | --- |
| 1 | `PASS_CLEAN` | `task_itcgbzweb4f...` | `a363ac79-ab15-47fd-a1d0-6e6457006055` | 1.00 | Passed. Verifier confirmed exactly 2 transfers totaling 5,358.75, exactly 4 transaction records, correct debits/credits, and expect_only_v2 with no unexpected changes. |
| 2 | `PASS_CLEAN` | `task_a3usg9top92...` | `9d254060-5d27-4861-9df7-b13fa9ea0843` | 1.00 | Passed. Verifier confirmed refill request, Yellow Fever Vaccine appointment on 2025-10-17 at 11:00, $62.47 payment, travel-window cancellations, refund, and calendar e... |
| 3 | `PASS_CLEAN` | `task_ru0dyrkku4o4...` | `82579f1a-7244-4850-b894-fbd92946538e` | 1.00 | Passed. Trace final output confirms an in-person new-patient dental visit for Oct 21 at 8:00 AM, completed check-in, creation of Medical calendar, and movement of the ... |
| 4 | `PASS_CLEAN` | `task_wlwpehpccpnu...` | `2e1cbb62-7215-46b3-9e86-fd645b149049` | 1.00 | Passed. Verifier confirmed correct patient, new Appointment with Dr. Wu calendar event, sent Rescheduled email to Priya Shah, 2:00 time reference, and no unexpected ch... |
| 5 | `PASS_CLEAN` | `task_iyzvzskxeh1...` | `2d913ac1-3331-435a-bec6-122fff809732` | 1.00 | Passed. Verifier confirmed Delta Air Lines amount $685.69, Harbor transfer of 68,569 cents, scheduled date 2025-10-21, transaction debit, account balance, and pending ... |
| 6 | `PASS_CLEAN` | `task_gyabeyvmumof...` | `d9d35679-1997-413b-8c45-e1e56c61d5cb` | 1.00 | Passed. Trace confirms Meridian dispute/refund was reconciled, Refund Confirmed Oct tag applied, and email sent with $224.69 filled into the required placeholders. |
| 7 | `PASS_BUT_STATIC_RISK` | `task_ivnptdiryl3z...` | `d1b4574b-9112-4124-af54-dc19ce468370` | 1.00 | Passed despite high static risk. Verifier confirmed payments for Omar and Maya, no payment for Jordan/Lena where appropriate, refund-confirmation message details, corr... |
| 8 | `NARROW_VERIFIER_FAILURE` | `task_i6zm3orie1xt...` | `b409d15c-3951-49ba-8c75-e76aa5d4b558` | 0.00 | Failed narrowly. Verifier found the todo was still incomplete, vendor notes did not match the expected cancellation state, and exactly 2 expected sent emails were miss... |
| 9 | `NARROW_VERIFIER_FAILURE` | `task_hscavs4v3fgy...` | `9e906006-40fd-426b-91cc-e26482adfd7d` | 0.00 | Failed on a concrete state mismatch: invoice and payment-email work mostly existed, but invoice 122 was still draft when verifier expected sent; database diff flagged ... |
| 10 | `NARROW_VERIFIER_FAILURE` | `task_xjpsgv3t5xg...` | `f6e64c52-f8d2-4eaa-9da1-5cec87d08d6f` | 0.00 | Mostly correct work with a diff failure. Verifier confirmed product/service setup, updated hourly rate, sent invoice, correct email, and calendar events, but failed on... |
| 11 | `NARROW_VERIFIER_FAILURE` | `task_iq4wtbrqg3i...` | `49fd1cf0-0852-4e13-a0e8-04575d29013a` | 0.00 | Concrete transfer mismatch. Some bank/accounting work passed, but verifier reported missing expected transaction records and wrong account balances/transfer amounts ve... |
| 12 | `NARROW_VERIFIER_FAILURE` | `task_dlmkv6otfy07...` | `ac65a76b-fe0e-4ca8-ac08-026848c73cc6` | 0.00 | High-value repair candidate. Verifier confirmed late-charge invoices and three follow-up emails with correct subjects/body/references, but final failure was specific: ... |

## How To Use This

1. Start with `PASS_CLEAN` and `PASS_BUT_STATIC_RISK` rows for promotion candidates.
2. Route `NARROW_VERIFIER_FAILURE` rows to targeted verifier or final-state repair.
3. Treat `PARTIAL_COMPLETION` rows as close runs that need missing side effects repaired or rerun.
4. Separate `ENVIRONMENT_OR_NAVIGATION_FAILURE` from true task-quality failures before rejecting.
5. Keep `TASK_OR_SEED_AMBIGUITY` and `BROAD_SIDE_EFFECT_FAILURE` in manual review.

## Limits

- Markdown trace rows are manually curated evidence; downloaded transcripts provide broader scale.
- The classifier is rule-based and intentionally explainable, so edge cases should be reviewed by a human.
- If a task key is shortened in the evidence file, the triage join uses best-effort prefix matching.
