# Project One Trace Evidence

This is the concrete run-evidence layer on top of the static triage. I used the Fleet dashboard session viewer to inspect completed sessions and record actual verifier output, final-answer behavior, and visible trace failures.

The point is to show what happened in real runs, not just why a task looked risky from static analysis.

## Coverage

- Dashboard dataset: [JUNE24-PSI-UNDELIVERED-EVALED](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).
- Dataset score snapshot: 257 tasks, 712 sessions, 658 scored sessions, 220 scored tasks, 7.6% pass rate.
- Trace spot-checks in this note: 20 completed sessions.
- Bucket coverage: 5 traces from each recovery bucket.
- Environments covered: consumer finance and personal health.
- Selection method: start from `reports/task_recovery_ranked.csv`, prefer tasks with completed sessions, and skip traces that did not expose useful score/verifier/final-answer evidence when clearer traces were available.

This is not a claim that every task was trace-reviewed. It is a targeted evidence sample that calibrates the static triage against real runs.

## A: Likely Good Spot Check

| Rank | Task | Session | Score / Model | Actual Trace Finding | Handoff Call |
| ---: | --- | --- | --- | --- | --- |
| 2 | `task_itcgbzweb4f...` | `a363ac79-ab15-47fd-a1d0-6e6457006055` | `1.00`, `claude-opus-4.8` | Passed. Verifier confirmed exactly 2 transfers totaling 5,358.75, exactly 4 transaction records, correct debits/credits, and `expect_only_v2` with no unexpected changes. | Promote after light spot-check. |
| 5 | `task_i6zm3orie1xt...` | `b409d15c-3951-49ba-8c75-e76aa5d4b558` | `0.00`, `gpt-5.5` | Failed narrowly. Verifier found the todo was still incomplete, vendor notes did not match the expected cancellation state, and exactly 2 expected sent emails were missing. | Repair task workflow around final todo/email completion. |
| 6 | `task_a3usg9top92...` | `9d254060-5d27-4861-9df7-b13fa9ea0843` | `1.00`, `gpt-5.5` | Passed. Verifier confirmed refill request, Yellow Fever Vaccine appointment on `2025-10-17` at `11:00`, `$62.47` payment, travel-window cancellations, refund, and calendar event with no unexpected durable changes. | Promote candidate. |
| 9 | `task_hscavs4v3fgy...` | `9e906006-40fd-426b-91cc-e26482adfd7d` | `0.00`, `gpt-5.5` | Failed on a concrete state mismatch: invoice and payment-email work mostly existed, but invoice `122` was still `draft` when verifier expected `sent`; database diff flagged the unexpected invoice status. | Repair/send-state issue; likely recoverable. |
| 10 | `task_ru0dyrkku4o4...` | `82579f1a-7244-4850-b894-fbd92946538e` | `1.00`, `claude-opus-4.8` | Passed. Trace final output confirms an in-person new-patient dental visit for Oct 21 at 8:00 AM, completed check-in, creation of Medical calendar, and movement of the appointment event to that calendar. | Promote candidate after seed sanity check. |

Takeaway: the A bucket is not perfect, but it has real passing traces and narrow repair cases. It should be worked first because failures are generally specific and recoverable.

## B: Close / Verify Derivability

| Rank | Task | Session | Score / Model | Actual Trace Finding | Handoff Call |
| ---: | --- | --- | --- | --- | --- |
| 18 | `task_zidagf17yxuq...` | `e34d7c81-cc3d-49d1-a022-8c93d6d4018a` | `0.00`, `gpt-5.5` | Partial success. Verifier found the new invoice, payment link, correct `$3,400` amount, customer email, and description, but invoice status was `draft` instead of `sent`, and the expected Integration Meeting calendar event/email were missing. | Repair final send/calendar steps. |
| 20 | `task_wlwpehpccpnu...` | `2e1cbb62-7215-46b3-9e86-fd645b149049` | `1.00`, `claude-opus-4.8` | Passed. Verifier confirmed correct patient, new `Appointment with Dr. Wu` calendar event, sent `Rescheduled` email to Priya Shah, 2:00 time reference, and no unexpected changes. | Promote candidate. |
| 22 | `task_iyzvzskxeh1...` | `2d913ac1-3331-435a-bec6-122fff809732` | `1.00`, `claude-opus-4.8` | Passed. Verifier confirmed Delta Air Lines amount `$685.69`, Harbor transfer of 68,569 cents, scheduled date `2025-10-21`, transaction debit, account balance, and pending debit changes. | Promote candidate after confirming derivability of the Delta amount. |
| 23 | `task_ih05dzesrzu...` | `31f7f93f-c9cb-43bc-bac6-917f056be6f7` | `0.00`, `gpt-5.5` | Mixed result. Verifier confirmed the Latch reply was sent to Leander Little League with correct subject/body, but found no new Zelle contact, no Zelle payment, no Zelle transaction record, unchanged balances, and no sponsors dinner calendar event. | Repair payment/calendar side effects. |
| 56 | `task_nw14kiriuj0w...` | `c8941e2e-54ea-45dc-a15a-189916959744` | `0.00`, `claude-opus-4.8` | Partial success. Ledger expense was correct: `Party Depot`, `2025-10-14`, `$35.67`, `bank_transfer`, `Party Supplies`, `Training and Education`, `EXP-0527`. Verifier failed because Zelle contact/payment/transaction and Priya Shah sent reply were missing. | Good close/repair example; do not promote until cross-app completion is reliable. |

Takeaway: B really is the "close but verify" bucket. The traces show many tasks are mostly right, but hidden constants and final side effects still need proof.

## C: Repair Candidate

| Rank | Task | Session | Score / Model | Actual Trace Finding | Handoff Call |
| ---: | --- | --- | --- | --- | --- |
| 111 | `task_xjpsgv3t5xg...` | `f6e64c52-f8d2-4eaa-9da1-5cec87d08d6f` | `0.00`, `claude-opus-4.8` | Mostly correct work with a diff failure. Verifier confirmed product/service setup, updated hourly rate, sent invoice, correct email, and calendar events, but failed on an unexpected extra `messages` insertion. | Repair verifier/message side-effect boundary. |
| 115 | `task_xcpzxskowvyw...` | `e38e10e0-c886-482a-94a4-5d629214eb73` | `0.00`, `claude-opus-4.8` | Environment/flow blockage. Trace says the agent completed the other pieces but could not complete an Epic/Lifeline message subtask after repeated navigation/tool failures. | Manual review: distinguish environment issue from task quality issue. |
| 117 | `task_iq4wtbrqg3i...` | `49fd1cf0-0852-4e13-a0e8-04575d29013a` | `0.00`, `claude-opus-4.8` | Concrete transfer mismatch. Some bank/accounting work passed, but verifier reported missing expected transaction records and wrong account balances/transfer amounts versus expected 266,439-cent movement. | Repair money derivation and transfer target logic. |
| 119 | `task_gyabeyvmumof...` | `d9d35679-1997-413b-8c45-e1e56c61d5cb` | `1.00`, `claude-opus-4.8` | Passed. Trace confirms Meridian dispute/refund was reconciled, `Refund Confirmed Oct` tag applied, and email sent with `$224.69` filled into the required placeholders. | Promote candidate; static C score was conservative. |
| 168 | `task_dlmkv6otfy07...` | `ac65a76b-fe0e-4ca8-ac08-026848c73cc6` | `0.00`, `gpt-5.5` | High-value repair candidate. Verifier confirmed late-charge invoices and three follow-up emails with correct subjects/body/references, but final failure was specific: expected exactly 4 new transaction lines, found 0. | Repair buffer-transfer/accounting-line side effect. |

Takeaway: C contains recoverable tasks, not just rejects. Several failures are narrow enough to repair if the team fixes verifier expectations or one missing side-effect path.

## D: High-Risk Manual Review

| Rank | Task | Session | Score / Model | Actual Trace Finding | Handoff Call |
| ---: | --- | --- | --- | --- | --- |
| 221 | `task_ivnptdiryl3z...` | `d1b4574b-9112-4124-af54-dc19ce468370` | `1.00`, `claude-opus-4.8` | Passed despite high static risk. Verifier confirmed payments for Omar and Maya, no payment for Jordan/Lena where appropriate, refund-confirmation message details, correct pool assignment, and `expect_only_v2`. | Promote only after one more spot-check; static risk was conservative here. |
| 222 | `task_us4sqtokm...` | `c9e33e4d-75cd-4ada-8aa8-ab4b0f17ec2c` | `0.00`, `claude-opus-4.8` | Trace exposes task ambiguity. The agent reasoned that no single doctor satisfied all stated constraints: Henry Ford affiliation, Portuguese language, Arizona tiebreaker, and visit type. It chose Dr. Joseph Martin after unresolved conflict. | Manual review first; likely prompt/seed inconsistency. |
| 223 | `task_yqupdaywlvqb...` | `6453589b-881a-45ad-bf8f-297ad28844a5` | `0.00`, `gpt-5.5` | Broad multi-system failure. Some Medical Out of Pocket and Meridian tag checks passed, but verifier found no expected transfer, no transaction records, wrong account balances, missing `Deductible-2025` tag, no sent reimbursement email, and no claim-status calendar event. | Keep in manual review / major repair. |
| 226 | `task_itxsazhocgr...` | `2ff37fe0-e033-4a5d-b6a0-7458270c1115` | `0.00`, `gpt-5.5` | Broad finance side-effect failure. Verifier found missing Zelle transaction, missing savings transfer, missing credit-card payment/payment transaction, unchanged card balance/minimum payment/available credit, missing discount email, and missing savings-transfer todo. | Manual-review first; too many side effects failed. |
| 227 | `task_qehlqyjkuoqy...` | `235e41ca-2974-4bed-869d-600a3f790b61` | `0.00`, `claude-opus-4.8` | Partial completion with environment/UI failure. Trace says amounts matched and a `$402.48` Harbor transfer plus Meridian support email were completed, but deleting the National Car Rental Ledger transaction did not register despite attempts. | Repair deletion flow/verifier expectation before promotion. |

Takeaway: D deserves manual review. It includes some false positives and one passing trace, but most evidence shows ambiguity, broad side-effect misses, or environment-sensitive actions.

## What These Traces Changed

- Static findings are useful for prioritization, but actual traces explain why a task failed.
- Some failed runs are not full task failures. `task_dlmkv6otfy07...` completed most invoice/email requirements and failed a narrow transfer-accounting check.
- Some low-risk tasks still fail in concrete ways, usually from final send/complete/status issues.
- Some high-risk tasks pass, so the high-risk bucket should not be treated as automatic rejection.
- For handoff, I would rank tasks by both static bucket and observed trace evidence: pass traces first, narrow verifier failures next, partial-completion/environment-navigation failures after that, then broad ambiguous failures.
