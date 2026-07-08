# Manual Review Queue

These are the top 50 tasks by static QA risk. Use this as a worklist, not as a rejection list.

## 1. task_uafdddxsii5f_n_1781580009873_ye68x4ssy__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `14.85`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|invoice_bill|math_or_aggregation|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `161.47|62.47`
- Verifier-only user values: ``

> I need to get my payments sorted for my health stuff as I have been getting calls, texts, etc., asking for payments. However, I have no idea why I still have money due. I thought I had paid it all off last month. Coul...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 2. task_vgekb6ez2mk_n_1781691388858_cx87x0003__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `14.55`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1875|246.66|371.66|875`
- Verifier-only user values: `2025-10-21 || Milo Property Services || North Loop Design Co || Review payment status for Milo Property Services || Review payment status for North Loop Design Co || billing+1@example.com || billing+3@example.com`

> I want to proactively follow up on customers with outstanding balances while ensuring that expected incoming payments are properly tracked and reserved. In Ledger, identify the two customers with the highest open bala...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 3. task_matgvxxwzl4t_n_1781541869363_1kostyx0x__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `14.3`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `35|62.47`
- Verifier-only user values: `2025-11-03 || 350 Fifth Avenue || 350 Fifth Avenue, Suite 4200, New York, NY 10118 || New York`

> I want to manage the asthma follow-up preparation, medication refill coordination, appointment management, calendar updates, and outstanding billing across Lifeline, Medora, and Latch. Start in Lifeline and review the...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 4. task_g9jcqlioeg_n_1781363550879_h4ee24f4t__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.75`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `120|240|2400|40|4800|5040|738.75`
- Verifier-only user values: `%Dashboard Build% || %Dashboard Design% || 2025-10-14 || 2025-11-28 || billing+5@example.com`

> I'm getting a draft invoice ready for one of my customers and, as part of a promotion, I'd also like to send them a small reward while I finalize everything. In Ledger, find the customer "Elevate Embedded LLC" and upd...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 5. task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.7`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1089.99|21587.33|271.42|4735.41|480|486.83|587.33|6.83|735.41|89.99|9271.42`
- Verifier-only user values: `14/10/2025`

> Hiya, it's been a hectic afternoon, and we've been asked to provide a final cash position summary today for proper corporate accounting. Let us settle our outstanding credit card liability using an optimized rewards s...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 6. task_qmr6zgds3jyt_n_1781554267041_qznhql8vr__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.65`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|HEALTH_PRIVACY_REVIEW`
- Dependencies: `calendar_source|conditional_branch|email_source|math_or_aggregation|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `30`
- Verifier-only user values: `2012-08-27 || 2025-10-20 || 2025-11-04 || Appointment with Dr Wu || Dr. Wu || Maya Rivera || Wu Internal Medicine || lena.rivera@riverapierce.example`

> I am overdue on a general check-up so I want to schedule that today. Also, I am so glad I have finally been added to a dental insurance plan at work so I can finally book a dental consultation for my daughter, Lena. I...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 7. task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `123.8|17.66|18.63|18.77|19.91|21.96|32.21|37.49|44.48|54.31|78.06`
- Verifier-only user values: `%Adobe Creative% || %Canva Pro% || %Everyday Checking% || %Google Workspace% || %Ledger Online% || 2025-10-13 || 2025-10-16 || April 08, 2025 || April 8, 2025 || Google Workspace email || June 15, 2025 || October 10, 2025`

> I need your help with a subscription billing audit. First, review the relevant subscription activity in Harbor and Ledger: - Compare the StreamBox bill payment in scheduled transfers in Harbor (Pay & Transfer) with th...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 8. task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1517|517`
- Verifier-only user values: `%Emergency Savings% || 10/19/2025 || 2025-10-19 || 2025-11-18 || ops@canopyanalytics.example`

> I just checked my inbox and found a recent email from Canopy Analytics this week regarding an invoice. They said that the invoice is tied to a grant reporting pack and that they need a confirmation or receipt before t...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 9. task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.35`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `100|450|575.46|8575.46`
- Verifier-only user values: `2025-10-28 || 2025-11-14 || credit card(s) for Maya Rivera: ids=`

> I requested a credit line increase on our Meridian account. Before I can complete the application, I need to verify income and housing expenses. I also want to evaluate whether Meridian's current balance transfer offe...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 10. task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.2`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|personal_profile`
- Prompt apps: `fakelook|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `14486.83|4735.41|600|735.41|9751.42`
- Verifier-only user values: `2025-10-14 || Harbor Bank Alerts || Meridian Card Services || alerts@harbor.example || statements@meridian.example`

> I have some spare time and I need to look into the bank alert that was sent to me on Latch yesterday. I flagged it to look into later, but now is the perfect time! Find the email and head to the mentioned app to look ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 11. task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.15`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|HIGH_BRANCHING|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|invoice_bill|medical_record`
- Prompt apps: `fakelook|lifeline|medora|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `124.93|187.4|30|62.47`
- Verifier-only user values: `2025-10-23 || Dentist appointment with Dr. Joseph Martin on Nov 4 || Dermatologist appointment with Dr. Priya on Oct 23 at 11 AM || Dr. James Wu || Dr. Joseph Martin || Dr. Priya Patel || Maya Rivera || Rescheduled appointment with Dr. James Wu on Oct 23 at 10 AM || Video visit with Dr. James Wu on Nov 3 || Video visit with Dr. James Wu on Oct 20`

> I have a medical appointment coming up this week (10/17/2025), but I also have other commitments I must attend to. I need to reschedule this to 10/23/2025 for 10 AM. I also need to schedule a dermatologist appointment...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 12. task_iuxflcdhcj1y_n_1781704569850_f35noviu1__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `13.15`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-21 || Danielle Park || Dr. Danielle Park || James Wu || Oct 20 || Oct 21 || Upcoming video visit with Dr. James Wu || jordan.pierce@riverapierce.example || maya.rivera@riverapierce.example`

> I would like to book an appointment with a specialist because I have had some concerning symptoms flare up. I have been experiencing heartburn and an irregular heart beat recently for the first time. I need to schedul...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 13. task_dq9a2ad6xvfw_n_1781641058767_tkzomw5l4__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.9`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `140|154|87|97.9`
- Verifier-only user values: `2025-11-03 || Doctors Appointments || July 2 2025 || Upcoming Doctors Appointment || doesn't match Doctor's Appointments calendar id= || is 3/4 of balance`

> It's approaching the weekend and I need to cover any outstanding bills I have after my last appointment. In Lifeline, check my insurance claims. I'm positive I've paid all my insurance claims, but just to be sure, che...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 14. task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.85`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|medical_record|personal_profile`
- Prompt apps: `harbor|lifeline|medora|outlook|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `harbor|ledger`
- Verifier-only amounts: `20|62.47`
- Verifier-only user values: `10/06/2025 || 11/03/2025 || jordan.pierce@riverapierce.example`

> I want to pay most of the Lifeline bills, except for Jordan's. I don't think I have access to pay for those. If he has a bill, send him an email using the last email address he emailed me from. The subject is "Bill fo...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 15. task_g7z1w88tzgi_n_1781373040055_28w1j82eb__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `31.23|531.34`
- Verifier-only user values: `Milo Property Services || Slate Studio || billing+2@example.com || billing+3@example.com`

> A few client invoices in Ledger need attention before the next payment batch closes. Pull up the Sales Invoices view and check the status filter for Overdue, then separately check for Sent, combining both result sets....

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 16. task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.15`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1642.5|2517.5|629.38|62937.5|642.5|875`
- Verifier-only user values: `03/18/2025 || 09/06/2025 || 2025-03-18 || 2025-09-06 || Accounts Receivable || North Loop || North Loop Design Co || Pecan Street Studio || Undeposited Funds || ap@northloop.example || payments@pecanstreet.example`

> Some freelance payments came into my Harbor Everyday Checking account as remote deposits between March 1, 2025, and October 14, 2025, that I never got around to recording in Ledger, and I want the books to reflect wha...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 17. task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.05`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `159.68|1875|31.23|31.94|371.66|6.25|74.33`
- Verifier-only user values: `2025-10-14 || Hi Milo Property Services || Milo Property Services || Slate Studio || billing+2@example.com || billing+3@example.com`

> I’m mostly up to date with my invoice reconciliation in Ledger, but there are still a couple outstanding that I need to reconcile. For any invoices that are not already paid or draft, please cross check them against m...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 18. task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.05`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|MANY_LOOKUPS|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `conditional_branch|credit_card|email_source|math_or_aggregation|medical_record|personal_profile`
- Prompt apps: `fakelook|harbor|lifeline|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `lifeline`
- Verifier-only amounts: `11243.75|128500|134925|180598|925`
- Verifier-only user values: `support@meridian.example`

> I am trying to get together updated information to request a credit line increase with Meridian. I was invited to update them on my yearly salary and monthly spending a few days ago and would like to take the opportun...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 19. task_z4ahj9ulywql_n_1781550013842_qu78voj1r__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.05`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `187.4|62.47`
- Verifier-only user values: `2025-10-15 || 2025-10-16 || Maya Rivera || Meeting Invitation`

> I’ve got a suspicion that I’m going to have to tackle my high cholesterol problem sooner rather than later. Go find the results of my most recent fasting metabolic and lipid follow-up panel. If my LDL cholesterol numb...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 20. task_asvghzavjtzg_n_1781585241181_ywf3rxzj3__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.0`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1213.99|213.99`
- Verifier-only user values: `2025-10-05 || 2025-10-07 || 2025-10-09 || 2025-10-10 || 2025-10-16 || is not Oct 5, 7, or 9 || is outside Oct 5-10 range || is within Oct 5-10 date range`

> I was on a trip with my friend from October 5 to October 10 and paid for some of the expenses that we had together to simplify things. We agreed that we would split up these expenses later. Now, after the trip, I want...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 21. task_iegiud4ie8sa_n_1781547489845_yey638yu1__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.0`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `40|62.47`
- Verifier-only user values: `2025-10-15 || 212-555-0185 || 7344 Anderson Ln || 7344 Anderson Ln, Raleigh, NC 27601 || Urgent Care Visit`

> I broke my tooth and I need to schedule an urgent visit to a dentist ASAP. Please schedule an appointment in Medora with a dentist that has availability for an urgent visit at the earliest time, on 10/15. I can't spea...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 22. task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `12.0`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `14486.83|157.6|16800|486.83|4881.57|4981.57|800|881.57|981.57`
- Verifier-only user values: `2025-10-14`

> Today I'm responsible for organizing some things regarding payment and the bank account and I'll need your help. To start, in Meridian, pay the open bill that's due on October 18th, using the account with the highest ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 23. task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.95`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `10/18/2025 || 11/15/2025 || 2025-10-18 || 2025-11-15 || October 2025 Target transaction(s) on Gold Card || calendar@windsor-park-soccer-club.example || events@bookpeople.example || jordan.pierce@riverapierce.example`

> I am planning my Saturday. I will be spending time with Nora and running some errands. I don't want to forget anything, so I need you to make a list. In Latch, add all the tasks I mention to my day for the Saturday fo...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 24. task_edbhacdtf15c_n_1781591126430_n3nla40f5__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.85`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `harbor|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `18.63|30|514.82`
- Verifier-only user values: `2025-10-14 || 2025-11-13`

> My tasks for today are to pay outstanding bills for this month, to update bills in Ledger, if necessary, and to check if I have enough money on my Harbor account for upcoming expenses and bills. I also do not want to ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 25. task_h5krxt4vgizt_n_1781612831028_di2o7s7lk__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.85`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `140|250|286.6|389.6|427.85|500|572.15|627.97`
- Verifier-only user values: `2025-10-15 || 2025-10-17`

> Hi, a bunch of payments are about to hit my Harbor checking over the next day or two, and my Meridian card payment is coming out of the same account, so I want to make sure my checking does not drop below my safety fl...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 26. task_pdzpnhz0cm7p_n_1781625470054_jq7yq6rxw__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.75`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card`
- Prompt apps: `harbor|meridian`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `120|14366.83|14486.83|200|2313.17|2433.17|290.69|340.69`
- Verifier-only user values: `Maya Rivera`

> So, my wedding anniversary is coming up. I want to plan a beautiful gateway for me and my husband. But I am also on a budget constraint. I would like it if I could as less cash as possible. An option I want to explore...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 27. task_uegzt3a3alnr_n_1781718004093_kojk830fp__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.65`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1875|200`
- Verifier-only user values: `2025-10-13 || 2025-10-14 || 512-555-0198 || Alex and Priya || Rivera-Pierce || alex.morgan.contractor@example.com || jordan.pierce@riverapierce.example || priya.shah.reimbursements@example.com`

> I've just been approached by a new client who wants me to design a working dashboard for them within a week. I agreed, but only if they pay half of the total price as a deposit by tomorrow before I begin. I'll also ne...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 28. task_w6gnjtwmquh5_n_1781290281803_tqfgsxjic__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.65`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|personal_profile|provider_search`
- Prompt apps: `fakelook|harbor|medora|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `medora`
- Verifier-only amounts: `18.63|18.99|21.6|32|44.48|54.31`
- Verifier-only user values: `StreamBox Family Plan || support+23@vendor.example`

> I finally have time to clean up our subscriptions. An old StreamBox to-do has been sitting in my Latch tasks for months, and our reminder list in Ledger no longer matches what we actually pay. Start with the recurring...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 29. task_wpigk0jmkp3_n_1781556283663_7la5bw13h__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.6`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|math_or_aggregation|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-14 || 2025-10-16 || Dr. King || Dr. Thompson || is before Thursday 2025-10-16 || is not after 2025-10-14 || is on or after Thursday 2025-10-16`

> I have been dealing with a few issues, and I want to schedule some appointments in Medora. First, I have been having some ongoing issues with an upset stomach that is starting to greatly impact my life, and I would li...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 30. task_uie3badamyzk_n_1781520506149_84x4sunuf__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.5`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `128500|141350|1875|82400|90640`
- Verifier-only user values: `%Milo Property Services% || 2025-10-14 || Dear North Loop Design Co || Payment Link for North Loop Design Co || billing+1@example.com`

> Firstly, my annual income and total assets have risen by 10% each. Hence, could you help increase my annual income and total assets value stated in Meridian by correctly calculating their new values? Next, find the un...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 31. task_z2rocn884bvz_n_1781645366910_a7nbbrdn8__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.5`
- Environment: `psi-consumer-finance`
- Findings: `HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `121|2149|315.7|372.36`
- Verifier-only user values: `%Genesis Data% || %Hourly Advisory% || %Process Optimization Consulting% || %Workflow Automation Tools% || 2025-10-14 || 2025-11-28`

> I have been somewhat complacent about verifying customer deposits, specifically for the month of May 2025. Please take a look at my Bank of Harbor checking account for the month of May. Determine whether the expected ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 32. task_zgp4orqdpb0_n_1781512927273_bw57xtk3a__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.45`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|medical_record|personal_profile`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `62.47`
- Verifier-only user values: `350 Fifth Avenue || 350 Fifth Avenue, Suite 4200, New York, NY 10118 || New York`

> I want to prepare for my upcoming appointments, and schedule new appointments. In Medora, please navigate to all upcoming appointments that require additional preparation. For any of these that do not have a photo ID ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 33. task_pukb1eshzc1k_n_1781701090123_uwa276ndg__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.4`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `14486.83|16371.92|16800|371.92|4817.45|486.83|817.45|858.75`
- Verifier-only user values: `%Household Finance% || 2025-10-14 || 2025-10-30`

> I want to sort my card payment and savings sorted today before I forget again. In Meridian, pay the credit card in full using the linked Harbor Bank payment account. Use the full total balance shown in Meridian, and k...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 34. task_vzcjibyaetrk_n_1781615300595_i4qiu5ili__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.4`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|invoice_bill|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `127.44|142.44|15`
- Verifier-only user values: `%Orchid Dispatch% || support+13@vendor.example || support+1@vendor.example`

> There is so much I need to get done today, so I need your help with a couple of vendor issues. While you're in Ledger, find the bill BILL-00072 for the Harbor vendor and create an October planning duplicate version fr...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 35. task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.35`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `12064.59|125|1470.86|15.97|247.42|287.81|470.36|470.86|4735.41|486.83|504|735.41`
- Verifier-only user values: `2025-10-14 || jordan.pierce@riverapierce.example`

> I've let my spending go a little too freely this past month. I need to go through my finances today to make sure I have everything under control. Let's start with Bank of Harbor. My goal is to contribute at least $250...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 36. task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.35`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1264.59|264.59|3083.55|4735.41|6000|83.55|916.45`
- Verifier-only user values: `2025-10-15 || jordan.pierce@riverapierce.example`

> I’m planning to switch most of my bills over to my Meridian card so that I can get more rewards. We use a lot of points for trips. I need you to look at my last 4 available statements on my Harbor reward card and get ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 37. task_im4kbgyiwrpj_n_1781447840042_frjo4ut91__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.3`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `159.68|167.66|18.58|1875|31.23|32.79|324|371.66|390.24|7.98`
- Verifier-only user values: ``

> So I should be getting a freelance payment from Canopy Analytics. Can you check if it's been received, and then if you see it, please reconcile it in Ledger. Start with checking in Latch to see if I've received any in...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 38. task_gth4zs74wcai_n_1781415785576_qzz51p63n__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.25`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|medical_record`
- Prompt apps: `harbor|lifeline|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `lifeline`
- Verifier-only amounts: `141.25|1500|200|251.42|450|500|676.2|850|858.75`
- Verifier-only user values: `2025-10-16`

> Our finance dept has asked us to tie up our operational expenses for the month. We have a few crucial service invoices to log, an email update to send out, and some cash flow adjustments to handle across our accounts ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 39. task_sfjed1tt1gst_n_1781652381399_3vhhv330i__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.25`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `31.23`
- Verifier-only user values: `INV-00009 is overdue as of 02/23/2025 || INV-00044 is overdue as of 02/02/2025 || INV-00119 is overdue as of 03/25/2025 || Milo Property Services || Slate Studio || billing+2@example.com || billing+3@example.com`

> I have a couple of overdue invoices that need to be resolved. We're going to start with invoices that are 'not due yet' and then work on 'overdue'. In Ledger, filter for invoices that show up having the status 'not du...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 40. task_izn1wcinqm0z_n_1781652793067_3qijsf8bc__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.2`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|invoice_bill|math_or_aggregation|medical_record`
- Prompt apps: `lifeline|meridian|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `lifeline`
- Verifier-only amounts: `159.68|31.23|371.66|562.57`
- Verifier-only user values: `%Hilton Honors% || 2025-10-22 || 2025-10-24 || 2025-10-26 || 2025-11-01`

> I need to manage my card, update Ledger to include two new bills and do some banking. I want to get this done before the weekend, so I can relax and not have to think about it. So, let's get this all done today! I nee...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 41. task_zo1had3vycvn_n_1781706559433_y744ddaat__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.15`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-21 || 2025-10-22 || 857 First St || Donald Lee || Hi Jordan || Jordan Pierce || Prenatal Appointment Scheduled for October 22 || jordan.pierce@riverapierce.example`

> My gynecologist canceled on me, and I'm only in my first trimester, so I'd like to schedule a new appointment with a gynecologist in Medora who accepts my current medical insurance. I need an appointment for prenatal ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 42. task_i8xzvmzsxsql_n_1781700231775_h6zh3s0cg__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.1`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `159.68`
- Verifier-only user values: `%Milo Property Services% || 2025-10-16 || Check with Milo Property Services || Milo Property Services || billing+3@example.com`

> In Ledger, find the customer whose total amount owed is around $500. Then, look up their overdue invoice for March. Next, open Harbor and look at the history of our checking account to see if there is a payment for th...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 43. task_v7koqmbuaya5_n_1781552099121_jk2e798b6__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.05`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|email_source|invoice_bill|medical_record`
- Prompt apps: `fakelook|lifeline|outlook|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `12.47|137.4|187.4|62.47`
- Verifier-only user values: `2028-10-14 || 2028-10-15 || amy.rivera@riverapierce.example || jordan.pierce@riverapierce.example`

> I'm looking to grant access on Lifeline to a couple of my family members. First, head over to Latch. Gather the contact email for Jordan Pierce and Amy Rivera. After doing so, head back into Lifeline to give them both...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 44. task_oovp9nyfyo0_n_1781566654585_xyu47p2qg__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `11.0`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|invoice_bill|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `135|89|98.2`
- Verifier-only user values: `2025-10-20`

> I have scheduled an appointment with Dr. James Wu, MD in Medora - to review asthma action plan and October refill timing after portal result notice. I have been having a series of asthma attacks, so I need this follow...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 45. task_snomzyg0aaz_n_1781541336492_kon2jr7io__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.95`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `conditional_branch|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1324|1875|875`
- Verifier-only user values: `ops@canopyanalytics.example`

> Check my emails with Canopy Analytics. They said they sent payment for an invoice by deposit to my bank account. Check whether I received that full payment to my bank account. If I did, mark that invoice as paid and w...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 46. task_fl7vfmuvegbg_n_1781660573933_rxumgonk3__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.9`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `110.55|1237.63|159.68|237.63|31.23|324.15|371.66|483.83|79.32|865.97`
- Verifier-only user values: `Interest Applied to INV-00009 || Interest Applied to INV-00044 || Interest Applied to INV-00119 || billing+2@example.com || billing+3@example.com`

> I was reviewing aged receivables and noticed that a number of invoices have remained outstanding for an unusually long period of time. Rather than continuing to carry these balances unchanged, I would like the records...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 47. task_wyrsgiwdci3q_n_1781529659099_779nii14o__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.85`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|math_or_aggregation|personal_profile|provider_search`
- Prompt apps: `medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `20|62.47`
- Verifier-only user values: `2025-10-21 || Oct 22`

> My husband has been nudging me for some time to get a new credit card that offers better rewards points for our medical related expenses, which I finally have. We’ve also been planning to book Omar’s annual physical c...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 48. task_abnoxqu8myxh_n_1781539233132_asy21q4wt__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card`
- Prompt apps: `fakelook|harbor|meridian`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `13777.05|14486.83|182.55|22.95|3022.95|709.78|777.05`
- Verifier-only user values: `2025-10-14 || 2025-10-31`

> One formatting note, write any dollar amount as $0.00, like $1,234.56. First, the card. Open my Meridian Gold Card and check whether AutoPay is on. If AutoPay is on, then the minimum is already covered, so instead I w...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 49. task_ilyr5jkkljrf_n_1781571007260_wxumiflc4__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `30`
- Verifier-only user values: `2019-12-12 || 2025-10-16 || 2025-10-17 || 2025-10-20 || 2025-11-03 || 2025-12-02 || Appointment with Dr. James Wu, MD || Appointment with Dr. Priya Patel, MD`

> I have some upcoming appointments in Medora health, can you please make sure they are all in my Latch calendar? If they are there but have different information than what I would like then please update them, otherwis...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 50. task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1115.44|115.44|14486.83|16800|17|18.63|2313.17|354.92|486.83`
- Verifier-only user values: `2025-11-08 || 2025-11-10`

> We are nearing the end of this month (October, 2025), and I'm thinking that I should evaluate how my spending has been, along with paying the credit card bill and sorting out my emergency fund savings account. Help me...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.
