# Verification Sample

A small sample of the tool output was manually checked to make sure the static flags were useful and to identify false positives. Real completed dashboard traces were also reviewed so the sample was grounded in observed model behavior, not only prompt/verifier inspection.

The static review answered: "Did the tool flag the right review leads?"

The trace review answered: "What actually happened when a model attempted the task?"

## High-Risk True Positive

Task: `task_vgekb6ez2mk_n_1781691388858_cx87x0003__ayush_20260624__worktrial_taskloss_20260707`

The tool flagged many cross-system dependencies, high branching, verifier-only amounts, and verifier-only user values. Manual inspection confirmed the verifier hard-codes values such as `Milo Property Services`, `North Loop Design Co`, `371.66`, `1875`, and `2025-10-21`. The prompt asks the agent to identify the two customers with the highest open balances and derive invoice/payment-link amounts, so these constants are not necessarily wrong, but they are exactly the facts that need seed-data derivability checks.

## High-Risk Mixed Result

Task: `task_uafdddxsii5f_n_1781580009873_ye68x4ssy__ayush_20260624__worktrial_taskloss_20260707`

The tool correctly flagged relative dates, heavy branching, many lookups, hidden verifier amounts, and a long prompt. Manual inspection found verifier constants such as `62.47` and `161.47`, which appear to encode the outstanding balance and cost-estimate calculation. The `PROMPT_APP_NOT_VERIFIED` flag was partly a false positive: health billing language was mapped to the Ledger/QuickBooks family even though the prompt is about Lifeline billing, so this mapping should be treated as a lead rather than a conclusion.

## Low-Risk Spot-Check

Task: `task_cytlhsftjt4w_n_1781809824975_0f53asur8__ayush_20260624__worktrial_taskloss_20260707`

The tool bucketed this as `A_likely_good_spot_check`. Manual inspection supports that as a reasonable first-pass classification: the prompt gives explicit vendors, amounts, bill terms, category, description, and payment method; the verifier covers QuickBooks/Ledger plus no-change guards for other apps. One wording issue remains: the intro says “send some emails,” but the actual instructions do not ask for any email action, and the verifier does not expect one.

## Real Trace Calibration

The trace sample covers 20 representative completed dashboard traces: 5 from each recovery bucket. These examples calibrate the static buckets against actual run outcomes.

### A: Likely Good Spot Check

| Task | Score | What Happened | Review Call |
| --- | ---: | --- | --- |
| `task_itcgbzweb4f...` | 1.00 | Passed with exactly 2 transfers, 4 transaction records, correct debits/credits, and no unexpected changes. | Promote after light spot-check. |
| `task_i6zm3orie1xt...` | 0.00 | Failed narrowly: todo still incomplete, vendor notes did not match cancellation state, and 2 sent emails were missing. | Repair final todo/email completion. |
| `task_a3usg9top92...` | 1.00 | Passed refill, vaccine appointment, `$62.47` payment, cancellations, refund, and calendar checks. | Promote candidate. |
| `task_hscavs4v3fgy...` | 0.00 | Invoice/payment-email work mostly existed, but invoice `122` stayed `draft` when verifier expected `sent`. | Repair send-state issue. |
| `task_ru0dyrkku4o4...` | 1.00 | Passed dental visit, check-in, Medical calendar creation, and appointment movement. | Promote after seed sanity check. |

Takeaway: A is not automatic pass, but the failures are specific and recoverable.

### B: Close / Verify Derivability

| Task | Score | What Happened | Review Call |
| --- | ---: | --- | --- |
| `task_zidagf17yxuq...` | 0.00 | Invoice, payment link, amount, customer email, and description were right, but invoice stayed `draft` and calendar/email steps were missing. | Repair final send/calendar steps. |
| `task_wlwpehpccpnu...` | 1.00 | Passed patient, calendar event, Priya Shah email, time reference, and no unexpected changes. | Promote candidate. |
| `task_iyzvzskxeh1...` | 1.00 | Passed Delta amount, Harbor transfer, scheduled date, transaction debit, balance, and pending debit changes. | Promote after confirming Delta amount derivability. |
| `task_ih05dzesrzu...` | 0.00 | Latch reply was sent correctly, but Zelle contact/payment/transaction, balances, and sponsors dinner calendar event were missing. | Repair payment/calendar side effects. |
| `task_nw14kiriuj0w...` | 0.00 | Ledger expense was correct, but Zelle contact/payment/transaction and Priya Shah reply were missing. | Close repair; cross-app completion is the gap. |

Takeaway: B is genuinely close, but hidden constants and final side effects need proof before promotion.

### C: Repair Candidate

| Task | Score | What Happened | Review Call |
| --- | ---: | --- | --- |
| `task_xjpsgv3t5xg...` | 0.00 | Product/service, rate, invoice, email, and calendar events were correct, but an unexpected extra `messages` insertion caused failure. | Repair verifier/message side-effect boundary. |
| `task_xcpzxskowvyw...` | 0.00 | Agent completed other pieces but could not finish an Epic/Lifeline message after repeated navigation/tool failures. | Separate environment issue from task quality. |
| `task_iq4wtbrqg3i...` | 0.00 | Some bank/accounting work passed, but transaction records and balances did not match the expected transfer. | Repair money derivation and transfer logic. |
| `task_gyabeyvmumof...` | 1.00 | Passed dispute/refund reconciliation, tag application, and `$224.69` email placeholder completion. | Promote; static C score was conservative. |
| `task_dlmkv6otfy07...` | 0.00 | Late-charge invoices and follow-up emails passed, but expected 4 transaction lines were missing. | Repair accounting-line side effect. |

Takeaway: C contains repairable tasks, not just rejects.

### D: High-Risk Manual Review

| Task | Score | What Happened | Review Call |
| --- | ---: | --- | --- |
| `task_ivnptdiryl3z...` | 1.00 | Passed despite high static risk: payments/refunds/messages/pool assignment/no unexpected changes all checked out. | Promote only after one more spot-check. |
| `task_us4sqtokm...` | 0.00 | Trace exposed ambiguity: no single doctor satisfied Henry Ford, Portuguese, Arizona, and visit-type constraints. | Manual prompt/seed review first. |
| `task_yqupdaywlvqb...` | 0.00 | Broad multi-system miss: missing transfer, records, balances, tag, reimbursement email, and claim-status calendar event. | Keep in manual review / major repair. |
| `task_itxsazhocgr...` | 0.00 | Broad finance side-effect miss: missing Zelle, savings transfer, card payment, discount email, and todo. | Manual review before repair investment. |
| `task_qehlqyjkuoqy...` | 0.00 | Amounts and support email were partly right, but Ledger deletion did not register despite attempts. | Repair deletion flow/verifier expectation. |

Takeaway: D needs manual review, but it still contains false positives and one real pass.

These 20 traces motivate the post-run verification layer. The static tool tells reviewers where to look; trace review tells them whether the failure was a clean pass, a narrow repair, a partial completion, an environment issue, a task/seed ambiguity, or a broad side-effect failure.

## Takeaway

The tool is useful for prioritizing review and surfacing hidden constants, but every bucket needs human sampling against actual traces. The next best automation step is to connect static flags, seed-data checks, and completed-run traces so the reviewer can quickly distinguish legitimate derivations, model execution misses, environment failures, and fabricated ground truth.
