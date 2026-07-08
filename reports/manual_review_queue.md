# Manual Review Queue

These are the top 50 tasks by static QA risk. Use this as a worklist, not as a rejection list.

## 1. task_matgvxxwzl4t_n_1781541869363_1kostyx0x__ayush_20260624__worktrial_taskloss_20260707

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

## 2. task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707

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

## 3. task_qmr6zgds3jyt_n_1781554267041_qznhql8vr__ayush_20260624__worktrial_taskloss_20260707

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

## 4. task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707

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

## 5. task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707

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

## 6. task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707

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

## 7. task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707

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

## 8. task_iuxflcdhcj1y_n_1781704569850_f35noviu1__ayush_20260624__worktrial_taskloss_20260707

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

## 9. task_dq9a2ad6xvfw_n_1781641058767_tkzomw5l4__ayush_20260624__worktrial_taskloss_20260707

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

## 10. task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707

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

## 11. task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707

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

## 12. task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707

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

## 13. task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707

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

## 14. task_z4ahj9ulywql_n_1781550013842_qu78voj1r__ayush_20260624__worktrial_taskloss_20260707

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

## 15. task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707

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

## 16. task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707

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

## 17. task_uegzt3a3alnr_n_1781718004093_kojk830fp__ayush_20260624__worktrial_taskloss_20260707

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

## 18. task_w6gnjtwmquh5_n_1781290281803_tqfgsxjic__ayush_20260624__worktrial_taskloss_20260707

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

## 19. task_vzcjibyaetrk_n_1781615300595_i4qiu5ili__ayush_20260624__worktrial_taskloss_20260707

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

## 20. task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707

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

## 21. task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707

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

## 22. task_im4kbgyiwrpj_n_1781447840042_frjo4ut91__ayush_20260624__worktrial_taskloss_20260707

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

## 23. task_gth4zs74wcai_n_1781415785576_qzz51p63n__ayush_20260624__worktrial_taskloss_20260707

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

## 24. task_izn1wcinqm0z_n_1781652793067_3qijsf8bc__ayush_20260624__worktrial_taskloss_20260707

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

## 25. task_zo1had3vycvn_n_1781706559433_y744ddaat__ayush_20260624__worktrial_taskloss_20260707

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

## 26. task_i8xzvmzsxsql_n_1781700231775_h6zh3s0cg__ayush_20260624__worktrial_taskloss_20260707

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

## 27. task_oovp9nyfyo0_n_1781566654585_xyu47p2qg__ayush_20260624__worktrial_taskloss_20260707

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

## 28. task_snomzyg0aaz_n_1781541336492_kon2jr7io__ayush_20260624__worktrial_taskloss_20260707

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

## 29. task_ilyr5jkkljrf_n_1781571007260_wxumiflc4__ayush_20260624__worktrial_taskloss_20260707

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

## 30. task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707

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

## 31. task_olqncx5cxrq4_n_1781574270429_uhfhk55t2__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-16 || 2025-10-23 || 3000 Madison St || Dr. James Wu, MD || Dr. Margaret Hall, MD`

> I would like some help booking an appointment at a specialist as well as getting an appointment booked online for my primary care doctor for a referral or else my insurance doesn't cover the specialist visit. Find me ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 32. task_poegykqfexl8_n_1781525501332_9z2rupgb3__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `155.23|37.49|39.68|78.06`
- Verifier-only user values: `2025-10-13 || 2025-10-14 || 2025-10-15 || 2025-10-31 || 2025-11-13 || 2025-11-14 || 2025-11-15`

> To save some money each month, I'm going to start cancelling some of my Meridian Gold Card subscriptions. Pull up this month's card activity and find what I spent this month on three I'm done using: Adobe Creative Clo...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 33. task_qehlqyjkuoqy_n_1781640416463_7t94nlq5c__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.8`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `402.48|858.75`
- Verifier-only user values: `2025-10-14`

> I want to ensure that my recent transactions are properly categorized, and also reconcile my expenses for the last week. Go to Meridian and go through my statements and activity. Note the vendor and amount for all tra...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 34. task_glvi0nyc1p6y_n_1781782792093_gihqex5xi__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `114.91|11702.54|14486.83|16800|486.83|702.54`
- Verifier-only user values: `2025-10-14 || Missing Meridian ACH debit transaction on account 1`

> I want to clear my credit card balances today and make sure everything is set up properly afterward, then send my husband a quick update once it's all done. In Meridian, identify the total outstanding balance on the c...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 35. task_yqupdaywlvqb_n_1781306014106_ejs854ja4__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.55`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|medical_record`
- Prompt apps: `fakelook|harbor|lifeline|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `lifeline`
- Verifier-only amounts: `187.5|6`
- Verifier-only user values: `October Medical OOP expenses have BrightPath claim memo || is not categorized as Medical Out of Pocket || support+5@vendor.example`

> We're on a high-deductible plan with BrightPath Insurance and I track our medical out-of-pocket spending every month. I want October's claim filed and the books squared away today. Start by making sure the books are c...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 36. task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.5`
- Environment: `psi-personal-health`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|credit_card|email_source|invoice_bill|math_or_aggregation|medical_record`
- Prompt apps: `fakelook|lifeline|outlook|quickbooks`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: `ledger`
- Verifier-only amounts: `20|30|35|62.47|82.47`
- Verifier-only user values: `Jul 5, 2025 || Reminder Jordan to pay his Lifeline balance`

> It's my monthly household medical-bill cleanup in Lifeline. I manage four records there: my own (Maya Rivera, MRN-RP-9001), Lena Rivera (MRN-RP-9003), Jordan Pierce (MRN-RP-9002), and Omar Pierce (MRN-RP-9004). Go thr...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 37. task_us4sqtokm_n_1781710895603_wujeck8m9__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.5`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `40`
- Verifier-only user values: `2025-10-27 || 2025-10-28 || 3833 Lewis St || Dr. Donna Anderson, MD || Midtown Clinic || Oct 28`

> I'm currently in New York and will be traveling to Arizona soon. Since I'll be there for a while, I'd like to schedule a dental appointment in Arizona during my stay. In Medora, first check if I already have a dentist...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 38. task_bldwgko1jup_n_1781355522269_qwmhwh80q__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.2`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|PROMPT_APP_NOT_VERIFIED|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|credit_card|email_source|invoice_bill|math_or_aggregation|medical_record|personal_profile`
- Prompt apps: `harbor|lifeline|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: `lifeline`
- Verifier-only amounts: `14486.83|2400|400|546`
- Verifier-only user values: `2025-10-13 || 2025-10-14 || 2025-11-13 || billing+11@example.com`

> Let's update Ledger with expenses and an invoice from yesterday and today. First, we need to link my Meridian Gold credit card with Ledger. Name the account Meridian Credit Card, the bank should just be Meridian, and ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 39. task_tvfwhbgglh_n_1781741268121_a1rgym0s6__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `D_high_risk_manual_review`
- Risk score: `10.2`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|email_source|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `40`
- Verifier-only user values: `2025-10-14 || Appointment Date label || Appointment Time label || Benjamin Lopez || Dr. Benjamin Lopez || appointment date 2025-10-14 || provider name Benjamin Lopez`

> In Lifeline, open the conversation "Dermatology appointment waitlist and insurance card" and verify that the active in-network insurance plan is Aetna Choice POS II Commercial. Then, in Medora, search for Dermatology ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 40. task_i9oc3bualpdt_n_1781194988200_9cibwav0i__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.95`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|email_source|invoice_bill|personal_profile`
- Prompt apps: `fakelook|harbor|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `85.88|858.75`
- Verifier-only user values: `2025-10-14 || Garden Gate Furniture Delivery || dispatch@garden-gate-furniture-delivery.example`

> There have been some home maintenance and renovation scheduled recently. Go to Latch and find the most recent email with "Furniture Delivery" in the sender name. Extract the sender contact information and go to Quickb...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 41. task_xtkbdlah8qjb_n_1781611160477_smfh8nikh__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.9`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|HEALTH_PRIVACY_REVIEW`
- Dependencies: `calendar_source|conditional_branch|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `62.47`
- Verifier-only user values: `2025-10-15 || Andrew Mitchell, DO`

> I need to take care of a few things for my parent, Omar Pierce. First, in my Lifeline profile, check if there are any outstanding bills in Lifeline. If there are any outstanding bills, pay the full amount due for each...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 42. task_imh4x0euefpz_n_1781685541540_34riemivo__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.8`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|MANY_LOOKUPS|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-22 || 801 Medical Plaza || Dr. Ramos || New York`

> I have obtained a BCBS Basic HMO coverage, so set it as my medical insurance. You don't have to enter the membership ID. Using this coverage, search for a cardiologist who is available two days after my appointment wh...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 43. task_bshwzmkvvma2_n_1781628770617_53s1xjj5t__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.75`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_USER_VALUES|HEALTH_PRIVACY_REVIEW`
- Dependencies: `calendar_source|conditional_branch|email_source|medical_record|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `2025-10-17 || 2025-10-20 || 2025-11-03 || 2025-12-02 || December 2 || Dr Patel || Dr. Wu calendar events || James Wu || November 3 || Oct 17 || Oct 20 || October 17`

> I just moved to Arizona for grad school and my schedule is already a mess before classes even start. I have four appointments coming up in Medora and I need to get organized before I lose track of everything. In Medor...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 44. task_hlt1v2oseidr_n_1781499374015_4d1avgc01__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.75`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|invoice_bill|personal_profile`
- Prompt apps: `meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: ``
- Verifier-only user values: `%To Dispute%`

> I have received an email that I need to add my mailing address and update my ATM PIN. Using Meridian, verify whether a home address is on my profile. If a home address exists, update my mailing address to be the same ...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 45. task_dto2ool7uks3_n_1781761877684_t7kvv6x09__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.7`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|LONG_PROMPT|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|email_source|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora|outlook`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `40`
- Verifier-only user values: `2025-10-17 || 705 Clinic Way || Park Cardiologist Clinic`

> I have been meaning to arrange a cardiology consultation for some time, but finding a suitable appointment that works around family commitments has been difficult. Since my spouse will likely be driving me to and from...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 46. task_m7tc4brunifj_n_1781636191630_fg6qpd5ch__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.7`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `2858.86|5971.69|858.86|971.69`
- Verifier-only user values: `2025-10-14 || 2025-10-15 || Meeting Invitation || elena.pierce@riverapierce.example || is not Dining or Shopping || jordan.pierce@riverapierce.example || luis.rivera@riverapierce.example || maya.rivera@riverapierce.example || tom.alvarez@mapleridge.example`

> In Meridian, add a tag of "optional" to all transactions in the "Dining" or "Shopping" category that have occurred since the last Meridian Gold Card statement. Send a Latch email to Jordan Pierce, Luis Rivera, and Ele...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 47. task_lhywptsxf6rj_n_1781648186758_kafn22w68__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|invoice_bill|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `12343.5|143.33|14486.83|14656.67|2143.33|343.5|484.75|858.75`
- Verifier-only user values: `2025-10-14 || 2025-10-15 || Bank Payment`

> I have decided to clear most of my dues today, as well as make accompanying changes to stay updated regarding my upcoming dues. Start off with Meridian Gold Card. Pay the statement balance if the amount is less than 4...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 48. task_tyjimqjpvqva_n_1781613811643_jxblp7b38__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.6`
- Environment: `psi-consumer-finance`
- Findings: `RELATIVE_DATE_ANCHORS|MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|VERIFIER_ONLY_AMOUNTS|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|conditional_branch|credit_card|email_source|math_or_aggregation`
- Prompt apps: `fakelook|harbor|meridian|outlook`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `1997.32|3994.63|500|994.63`
- Verifier-only user values: `2025-10-15 || 2025-10-21`

> I want to do some bookkeeping of finances in my Harbor bank and Meridian. In Harbor, verify the only bank recipient account that isn't verified yet. Thereafter, view the transactions in my Everyday Checking account fo...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 49. task_xojc6xarjoh_n_1781646774710_2ukoc3g99__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.6`
- Environment: `psi-consumer-finance`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|VERIFIER_ONLY_AMOUNTS|VERIFIER_ONLY_USER_VALUES|LONG_PROMPT|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `bank_transactions|calendar_source|conditional_branch|credit_card|email_source|invoice_bill|math_or_aggregation|personal_profile`
- Prompt apps: `fakelook|harbor|meridian|outlook|quickbooks`
- Verifier apps: `fakelook|harbor|meridian|quickbooks`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `11800|14486.83|16800|2313.17|25|2686.83|313.17|686.83|825`
- Verifier-only user values: `2025-10-13 || 2025-10-14 || Hilton Hotels || jordan.pierce@riverapierce.example`

> I am so burned out and really need to take some time for myself. I’ve decided I’m taking a trip to NYC to see The Lost Boys on Broadway! I need some help getting my finances in order for the trip so help me out. I thi...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.

## 50. task_yrckqhw8zmb_n_1781714885872_m5paxmwgo__ayush_20260624__worktrial_taskloss_20260707

- Bucket: `C_repair_candidate`
- Risk score: `9.5`
- Environment: `psi-personal-health`
- Findings: `MANY_CROSS_SYSTEM_DEPENDENCIES|HIGH_BRANCHING|HEALTH_PRIVACY_REVIEW|FINANCE_SIDE_EFFECT_REVIEW`
- Dependencies: `calendar_source|conditional_branch|credit_card|medical_record|personal_profile|provider_search`
- Prompt apps: `fakelook|lifeline|medora`
- Verifier apps: `lifeline|medora|outlook`
- Prompt app families missing from verifier: ``
- Verifier-only amounts: `40`
- Verifier-only user values: `2025-10-16 || Dr. Xu`

> In Lifeline, check for any abnormality in the most recent fasting metabolic and lipid profile test result. If there is any abnormality, it is time to book a cardiologist appointment for myself. Update my insurance pla...

Manual check:

- [ ] Open task world or session trace.
- [ ] Verify each prompt lookup fact is present in seed data.
- [ ] Verify verifier-only constants are derivable from seed data.
- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.
