# Project One Human Evidence Log

This log is the human-in-the-loop layer on top of the static triage tool. I sampled tasks across all four buckets and both environments, then manually checked prompt/verifier alignment and available session metadata. This is not a full end-to-end seed-data audit; it is a focused review pass designed to show which static flags deserve deeper environment verification.

For concrete dashboard run evidence, see `trace_evidence.md`. That file records three completed sessions with actual scores, final verifier output, and observed trace behavior.

## Coverage

- Source of truth: [Fleet dashboard dataset](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).
- Committed Project One scope: 257 dashboard-scoped tasks.
- Static tool coverage in committed reports: 257/257 scoped tasks.
- Dashboard score snapshot: 220 tasks scored, 658 scored sessions, 7.6% overall pass rate.
- Session metadata joined: 712 sessions across 257 tasks.
- Manual evidence sample in this log: 8 tasks.
- Completed dashboard traces inspected in detail: 3 sessions.
- Full seed/environment verification completed: 0 tasks so far.

## Sample Selection

I selected two tasks from each bucket where possible, balancing finance and health and preferring tasks with visible sessions.

| Bucket | Finance task | Health task |
| --- | --- | --- |
| High-risk manual review | `task_qehlqyjkuoqy_n_1781640416463_7t94nlq5c__ayush_20260624__worktrial_taskloss_20260707` | `task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707` |
| Repair candidate | `task_ogrtkp7dmz7_n_1781684912333_uubhq8apt__ayush_20260624__worktrial_taskloss_20260707` | `task_wam3eaul71u_n_1781709090122_r7ys8u6oh__ayush_20260624__worktrial_taskloss_20260707` |
| Close / verify derivability | `task_xyxx2vpkrek_n_1781607774982_827vogeju__ayush_20260624__worktrial_taskloss_20260707` | `task_igpndla7ffq_n_1781736164354_kdb59x0wl__ayush_20260624__worktrial_taskloss_20260707` |
| Likely-good spot check | `task_yktbgqjdiox_n_1781235421200_h1md9xdpg__ayush_20260624__worktrial_taskloss_20260707` | `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707` |

## Trace-Backed Findings Added After Reviewer Calibration

After the team emphasized actual traces, I inspected three completed dashboard sessions and added `trace_evidence.md`.

| Task | Trace result | Actual finding |
| --- | --- | --- |
| `task_nw14kiriuj0w...` | Failed, score `0.00` | Ledger expense was correct, but Zelle reimbursement and Latch reply were not completed. |
| `task_dlmkv6otfy07...` | Failed, score `0.00` | Late-charge invoices and follow-up emails mostly passed; failure concentrated on missing transfer/accounting transaction lines. |
| `task_a3usg9top92...` | Passed, score `1.00` | Health workflow passed refill, appointment, payment, cancellation/refund, and calendar-event checks. |

These examples are now the model for future review rows: cite the session, cite the exact verifier output, then decide promote/repair/reject.

## Findings By Task

### 1. High-Risk Finance

Task: `task_qehlqyjkuoqy_n_1781640416463_7t94nlq5c__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `D_high_risk_manual_review`.
- Sessions visible: 4.
- Tool flags: relative dates, many cross-system dependencies, branching, many lookups, verifier-only amounts.
- What I checked: prompt asks the agent to derive Meridian transactions over $50 between October 6 and October 12, exclude telecom/fuel, match Ledger expenses, recategorize pharmacy expenses, delete a rental expense without permit number, transfer the deleted amount, and send a Latch email.
- Verifier evidence: verifier expects Ledger expense IDs `523` and `526` to become `Home office supplies`, and expense ID `155` to be deleted. It also includes hidden amounts `402.48` and `858.75`.
- Human judgment: high-risk but likely repairable. The issue is not necessarily that the task is bad; the issue is that the verifier relies on hardcoded expense IDs for facts the prompt asks the model to derive. This must be checked against seed data before shipping.
- Decision: `repair_candidate_until_seed_derivability_confirmed`.
- Suggested fix: replace hardcoded ID checks with dynamic lookups by date, vendor, amount, and permit presence, or make the target records explicit in the prompt.

### 2. High-Risk Health

Task: `task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `D_high_risk_manual_review`.
- Sessions visible: 4.
- Tool flags: relative dates, branching, prompt app mismatch, verifier-only amounts, verifier-only user values.
- What I checked: prompt asks for rescheduling an existing appointment, booking dermatology one hour later, finding a dentist in New York or Michigan, paying a Lifeline bill, and creating Latch calendar events for October/November appointments.
- Verifier evidence: verifier expects specific values not present in the prompt, including `Dr. James Wu`, `Dr. Priya Patel`, `Dr. Joseph Martin`, `2025-10-23`, and payment amount `62.47`.
- Human judgment: high-risk and needs environment verification. These hidden constants may be derivable from Medora/Lifeline, but the task combines multiple dynamic appointment choices with billing and calendar synchronization. Also, the tool overflagged finance/Ledger language because this is health billing, not QuickBooks/Ledger.
- Decision: `manual_review_required`.
- Suggested fix: verify that the specific doctors/times/bill amount are uniquely derivable. If not, tighten the prompt or loosen verifier expectations around acceptable dentist selection.

### 3. Repair Candidate Finance

Task: `task_ogrtkp7dmz7_n_1781684912333_uubhq8apt__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `C_repair_candidate`.
- Sessions visible: 4.
- Tool flags: many cross-system dependencies, branching, finance side-effect review.
- What I checked: prompt asks for the largest ordinary Meridian charge since the last statement, excluding travel/transport/refunds, then tags it, moves a calculated savings amount, emails Ledger Receipts, adds a task, and creates a calendar event.
- Verifier evidence: verifier expects `AT&T` as the merchant, `$165.98` as the charge, `receipts@ledger.example`, October 20 task due date, and October 31 all-day event.
- Human judgment: this looks closer than the static bucket suggests. If `AT&T` and `$165.98` are uniquely derivable from the statement filters, this is a good long-horizon task. The main risk is whether “ordinary purchase” and exclusion criteria are unambiguous enough.
- Decision: `close_verify_derivability`.
- Suggested fix: confirm statement data has exactly one largest qualifying non-travel, non-transport, non-refund transaction.

### 4. Repair Candidate Health

Task: `task_wam3eaul71u_n_1781709090122_r7ys8u6oh__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `C_repair_candidate`.
- Sessions visible: 5.
- Tool flags: many cross-system dependencies, verifier-only values, health privacy review.
- What I checked: prompt asks for dental insurance update, first dentist with video availability on or after October 15, check-in completion, calendar event, boss email, and conditional cancellation of Dr. Wu if same day.
- Verifier evidence: verifier expects appointment on October 17 at 12:20 PM, calendar start around 11:50/12:00, `Dentist Appointment` event, specific boss email, and cancellation behavior tied to Dr. Wu.
- Human judgment: likely recoverable but needs a wording/verifier check. The prompt asks for a dentist, but the calendar body template says `Dr. [Insert Full Name], MD`, which may be semantically odd for a dentist. The verifier’s specific time must be proven to be the first valid availability.
- Decision: `close_with_prompt_cleanup`.
- Suggested fix: change the calendar body template to avoid `MD` unless the selected provider actually has that title, and verify the first-availability logic.

### 5. Close Candidate Finance

Task: `task_xyxx2vpkrek_n_1781607774982_827vogeju__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `B_close_verify_derivability`.
- Sessions visible: 4.
- Tool flags: verifier-only amounts, finance side-effect review.
- What I checked: prompt asks to pay Meridian statement balance, add Harbor savings in Meridian, add offers/benefits, pay pending/overdue Ledger bills by wire, email paid vendors, and set a monthly transfer.
- Verifier evidence: verifier expects specific amounts including `14486.83`, `16800`, `18.63`, and `486.83`, plus vendor email `billing@streambox.example`.
- Human judgment: close but not safe to ship without seed confirmation. The prompt is clear, but the verifier has several hidden financial constants that must line up with current Meridian/Ledger/Harbor data.
- Decision: `close_verify_financial_constants`.
- Suggested fix: inspect seed data for statement balance, overdue bill set, and monthly transfer total. If all are derivable, ship as a good multi-system finance task.

### 6. Close Candidate Health

Task: `task_igpndla7ffq_n_1781736164354_kdb59x0wl__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `B_close_verify_derivability`.
- Sessions visible: 4.
- Tool flags: cross-system dependencies, verifier-only user values, health privacy review.
- What I checked: prompt asks to add dental plan, book first available Raleigh dentist appointment on October 15, book earliest PCP asthma appointment on October 20, add calendar events, and message Lifeline billing.
- Verifier evidence: verifier expects `Dr. Joseph Flores`, `Dr. James Wu`, `Appointment with Dr. Joseph Flores`, `Appointment with Dr. James Wu`, and dates October 15/20.
- Human judgment: likely good if provider availability is unique. The prompt has enough specificity and the verifier constants appear to be expected derivations rather than contradictions.
- Decision: `likely_good_after_provider_availability_check`.
- Suggested fix: confirm that Dr. Joseph Flores is the first available in-network dentist for the specified dental plan/location/date.

### 7. Likely-Good Finance

Task: `task_yktbgqjdiox_n_1781235421200_h1md9xdpg__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `A_likely_good_spot_check`.
- Sessions visible: 3.
- Tool flags: finance side-effect review only.
- What I checked: prompt asks to reconcile a StreamBox bill if a Harbor transaction matches it, send cancellation emails for Cloudvault and StreamBox, and pause/delete recurring Ledger transactions based on subscription state.
- Verifier evidence: verifier checks no unexpected Harbor/Meridian changes, QuickBooks/Ledger recurring transaction updates, StreamBox bill payment behavior, and two cancellation emails.
- Human judgment: the tool’s low-risk classification looks reasonable. The conditional bill-payment branch is meaningful but not overcomplicated. The one thing to confirm is that Latch has the cancellation email addresses and Ledger has a clean recurring transaction set.
- Decision: `likely_good_spot_check`.
- Suggested fix: no prompt fix yet; do one environment spot check.

### 8. Likely-Good Health

Task: `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707`

- Tool bucket: `A_likely_good_spot_check`.
- Sessions visible: 5.
- Tool flags: verifier-only amounts, health privacy review.
- What I checked: prompt asks for a two-month refill, payment of Lifeline balances below $200, a GP appointment two hours after a calendar lab draw, calendar event creation, and cancellation of Medora appointments during travel.
- Verifier evidence: verifier expects a Yellow Fever Vaccine appointment, payment amount `62.47`, default credit-card payment, and appointment/calendar changes.
- Human judgment: low-risk but still needs derivability confirmation. The verifier’s payment amount should be fine if Lifeline has exactly that balance under $200, and the lab-draw calendar anchor should make the appointment timing deterministic.
- Decision: `likely_good_after_seed_check`.
- Suggested fix: confirm the lab draw event exists and that the first eligible GP appointment is unique.

## Tool Accuracy Notes

- Useful flags: verifier-only amounts and user-visible constants consistently pointed to the right manual question: “Is this hidden answer derivable from the world?”
- Useful prioritization: high-risk tasks generally combined dynamic lookup, branch logic, and hidden verifier constants.
- False positive: health billing language can trigger finance/Ledger heuristics because the words “bill,” “payment,” and “balance” overlap across domains.
- Calibration change made earlier: noisy verifier logging/docstrings were filtered so `VERIFIER_ONLY_USER_VALUES` focuses more on user-visible constants.

## Recommended Next Manual Pass

1. Deep-check the top 10 high-risk tasks with sessions.
2. Spot-check 10 likely-good tasks, especially those with 3+ sessions.
3. For each checked task, record the trace result, final verifier output, and whether verifier-only constants are uniquely derivable from prompt + seed world.
4. Promote only tasks that pass that derivability check or have a clean passing trace; otherwise mark as repairable and specify whether the prompt, verifier, or environment flow should move.
