# Project One Trace Evidence

This is the concrete run-evidence layer on top of the static triage. I used the Fleet dashboard session viewer to inspect completed sessions for a small set of tasks. The point is to show actual task behavior and verifier output, not just theoretical risk.

## Trace Coverage

- Dashboard dataset: [JUNE24-PSI-UNDELIVERED-EVALED](https://www.fleetai.com/dashboard/datasets/JUNE24-PSI-UNDELIVERED-EVALED).
- Dataset score snapshot: 257 tasks, 712 sessions, 658 scored sessions, 220 scored tasks, 7.6% pass rate.
- Trace spot-checks in this note: 3 sessions.
- Environments covered: consumer finance and personal health.
- What was checked: session status, model, score, duration, step/tool counts where visible, final answer, and verifier pass/fail output.

This is not a claim that every task was trace-reviewed. It is a targeted evidence sample that calibrates the static triage against real runs.

## Trace 1: Finance Partial Completion

- Task: `task_nw14kiriuj0w_n_1781131770786_owoqtdvge__ayush_20260624`
- Local triage key: `task_nw14kiriuj0w_n_1781131770786_owoqtdvge__ayush_20260624__worktrial_taskloss_20260707`
- Bucket: `B_close_verify_derivability`
- Session: `c8941e2e-54ea-45dc-a15a-189916959744`
- Model: `claude-opus-4.8`
- Result: failed, score `0.00`
- Duration / trace size: 48m39s, 405 steps, 216 computer tool calls, 1 final answer

Observed behavior:

- The agent successfully created the Ledger expense.
- Verifier confirmed the created expense was for `Party Depot`, dated `2025-10-14`, amount `$35.67`, payment method `bank_transfer`, memo containing `Party Supplies`, category `Training and Education`, paid from Harbor Everyday Checking, and transaction number `EXP-0527`.
- The agent did not complete the Harbor/Zelle reimbursement or sent email reply.
- Final answer stated that Harbor navigation failed because attempted direct hosts were blocked by the environment allowlist.

Verifier failure:

- Expected one new Zelle contact for Jordan Pierce, found zero.
- Expected one new Zelle payment to Jordan Pierce, found zero.
- Expected at least one new Zelle transaction record for account 1.
- Expected Harbor account balances to decrease, but balances did not change.
- No sent reply found in Priya Shah's conversation thread.
- Messages table had unexpected extra draft/message changes.

Finding:

This is not a bad prompt on its face. The trace shows partial task completion: Ledger succeeded, but app navigation and message-send completion failed. Recovery path is to rerun or debug environment navigation across Ledger, Harbor, and Latch; the task should not be promoted from static analysis alone.

## Trace 2: Finance Verifier Failure After Mostly Correct Work

- Task: `task_dlmkv6otfy07_n_1781138793510_cvrqys0hh__ayush_20260624`
- Local triage key: `task_dlmkv6otfy07_n_1781138793510_cvrqys0hh__ayush_20260624__worktrial_taskloss_20260707`
- Bucket: `C_repair_candidate`
- Session: `ac65a76b-fe0e-4ca8-ac08-026848c73cc6`
- Model: `gpt-5.5`
- Result: failed, score `0.00`
- Duration / trace size: 27m42s, 130 steps, 129 tool calls

Observed behavior:

- The agent created the late-charge invoices for the two qualifying overdue invoices.
- Verifier confirmed invoice dates, Net 15 due dates, totals, line descriptions, product/service match, exactly two new invoice items, and exactly two new sales transactions.
- Verifier confirmed exactly three sent follow-up emails, correct subjects, expected body content, Harbor reference numbers, correct recipients, sent status, sender, and required phrasing.
- Verifier confirmed no unexpected changes before the final payment/transfer check.

Verifier failure:

- Final failing check: expected exactly four new transaction lines, found zero.

Finding:

This is a high-value repair candidate. The trace shows most of the task was completed correctly, and the failure is concentrated in the buffer-transfer/payment-accounting side effect. The next repair step is specific: inspect whether the prompt, environment UI, and verifier agree on how the Emergency Savings to Everyday Checking transfer should be recorded as transaction lines.

## Trace 3: Health Task That Passed

- Task: `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624`
- Local triage key: `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707`
- Bucket: `A_likely_good_spot_check`
- Session: `9d254060-5d27-4861-9df7-b13fa9ea0843`
- Model: `gpt-5.5`
- Result: passed, score `1.00`
- Duration / trace size: 18m8s, 117 steps, 117 tool calls

Observed behavior and verifier confirmations:

- Refill request created for prescription `9011`, 60-day supply.
- Yellow Fever Vaccine appointment created.
- Appointment scheduled on `2025-10-17` at `11:00`, one-hour duration, location `Primary Care - Room 202`.
- GP/provider condition satisfied, attendee `Maya Rivera`.
- Payment succeeded for `$62.47` using the default credit card, amount due became `$0`.
- Travel-window appointments `902` and `913` were cancelled with reason `Work Trip`, time slots released, and payment `910` refunded `$35.00`.
- Calendar event was created with correct title, date, time, duration, location, and 120-minute reminder.
- Durable database diff validation passed with no unexpected changes.

Finding:

This supports the `A_likely_good_spot_check` bucket. The task has hidden verifier constants, but the completed trace proves at least one model run could derive and satisfy them. This is a good promotion candidate after a light second spot-check or seed-data confirmation.

## What These Traces Changed

- Static findings are useful for prioritization, but actual traces explain why a task failed.
- Some failed runs are not full task failures. `task_dlmkv6otfy07...` completed most invoice/email requirements and failed a narrow transfer-accounting check.
- Some low-risk tasks are genuinely recoverable. `task_a3usg9top92...` passed with clean verifier output.
- For handoff, I would rank tasks by both static bucket and observed trace evidence: pass traces first, narrow verifier failures next, partial-completion/environment-navigation failures after that, then broad ambiguous failures.
