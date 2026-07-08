# Verification Sample

I manually checked a small sample of the tool output to make sure the static flags were useful and to identify false positives. I also reviewed real completed dashboard traces so the sample was grounded in observed model behavior, not only prompt/verifier inspection.

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

I also checked five representative completed dashboard traces. These are the examples I used to calibrate the static buckets against actual run outcomes.

| Trace Type | Task | Session | What Happened | Why It Matters |
| --- | --- | --- | --- | --- |
| Clean pass | `task_a3usg9top92...` | `9d254060-5d27-4861-9df7-b13fa9ea0843` | The run passed. The verifier confirmed the refill request, Yellow Fever Vaccine appointment on `2025-10-17` at `11:00`, `$62.47` payment, travel-window cancellations, refund, and calendar event. | Shows that some low-risk/static-review tasks are genuinely promotable after a light seed sanity check. |
| Narrow verifier/state failure | `task_dlmkv6otfy07...` | `ac65a76b-fe0e-4ca8-ac08-026848c73cc6` | The run completed late-charge invoices and three follow-up emails, but failed because the verifier expected exactly four new transaction lines and found zero. | This is not a broad task failure; it is a targeted repair around a missing accounting side effect. |
| Partial completion | `task_nw14kiriuj0w...` | `c8941e2e-54ea-45dc-a15a-189916959744` | The Ledger expense was correct, including vendor, date, amount, method, category, and reference. The run failed because Zelle contact/payment/transaction and the Priya Shah reply were missing. | Confirms the `B_close_verify_derivability` bucket is often close, but cross-app completion still needs repair. |
| Environment/navigation issue | `task_xcpzxskowvyw...` | `e38e10e0-c886-482a-94a4-5d629214eb73` | The trace said the agent completed other pieces but could not complete an Epic/Lifeline message subtask after repeated navigation/tool failures. | Separates task quality from environment or tool reliability; this should not be treated the same as a bad prompt. |
| Task/seed ambiguity | `task_us4sqtokm...` | `c9e33e4d-75cd-4ada-8aa8-ab4b0f17ec2c` | The agent reasoned that no single doctor satisfied all stated constraints: Henry Ford affiliation, Portuguese language, Arizona tiebreaker, and visit type. | This is a prompt/seed-world issue first; the task should be clarified before model performance is judged. |

These five traces are why I added the post-run verification layer. The static tool tells reviewers where to look; trace review tells them whether the failure was a clean pass, a narrow repair, a partial completion, an environment issue, or a task/seed ambiguity.

## Takeaway

The tool is useful for prioritizing review and surfacing hidden constants, but every bucket needs human sampling against actual traces. The next best automation step is to connect static flags, seed-data checks, and completed-run traces so the reviewer can quickly distinguish legitimate derivations, model execution misses, environment failures, and fabricated ground truth.
