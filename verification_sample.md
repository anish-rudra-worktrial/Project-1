# Verification Sample

I manually checked a small sample of the tool output to make sure the static flags were useful and to identify false positives.

## High-Risk True Positive

Task: `task_vgekb6ez2mk_n_1781691388858_cx87x0003__ayush_20260624__worktrial_taskloss_20260707`

The tool flagged many cross-system dependencies, high branching, verifier-only amounts, and verifier-only user values. Manual inspection confirmed the verifier hard-codes values such as `Milo Property Services`, `North Loop Design Co`, `371.66`, `1875`, and `2025-10-21`. The prompt asks the agent to identify the two customers with the highest open balances and derive invoice/payment-link amounts, so these constants are not necessarily wrong, but they are exactly the facts that need seed-data derivability checks.

## High-Risk Mixed Result

Task: `task_uafdddxsii5f_n_1781580009873_ye68x4ssy__ayush_20260624__worktrial_taskloss_20260707`

The tool correctly flagged relative dates, heavy branching, many lookups, hidden verifier amounts, and a long prompt. Manual inspection found verifier constants such as `62.47` and `161.47`, which appear to encode the outstanding balance and cost-estimate calculation. The `PROMPT_APP_NOT_VERIFIED` flag was partly a false positive: health billing language was mapped to the Ledger/QuickBooks family even though the prompt is about Lifeline billing, so this mapping should be treated as a lead rather than a conclusion.

## Low-Risk Spot-Check

Task: `task_cytlhsftjt4w_n_1781809824975_0f53asur8__ayush_20260624__worktrial_taskloss_20260707`

The tool bucketed this as `A_likely_good_spot_check`. Manual inspection supports that as a reasonable first-pass classification: the prompt gives explicit vendors, amounts, bill terms, category, description, and payment method; the verifier covers QuickBooks/Ledger plus no-change guards for other apps. One wording issue remains: the intro says “send some emails,” but the actual instructions do not ask for any email action, and the verifier does not expect one.

## Takeaway

The tool is useful for prioritizing review and surfacing hidden constants, but every bucket needs human sampling. The next best automation step is to connect these flags to seed-data checks so the reviewer can quickly distinguish legitimate derivations from fabricated ground truth.
