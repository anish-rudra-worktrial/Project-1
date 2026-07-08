# Project One Static QA Summary

This report is a first-pass static triage over the exported JSONL dataset. It flags review leads; it does not replace environment inspection or human judgment.

## Scope

Scope: session-backed tasks only. Per Fleet guidance, tasks with no visible sessions are dropped from this analysis for now. Included 257 tasks and dropped 263 unrun tasks from the 520-task export.

## Dataset Shape

- Tasks: 257
- Risk score min/median/mean/max: 1.35 / 7.40 / 7.52 / 14.30

| Environment | Tasks |
| --- | --- |
| psi-consumer-finance | 150 |
| psi-personal-health | 107 |

## Session Coverage

- Sessions joined to tasks: 712
- Tasks with at least one session: 257

| Session status | Sessions |
| --- | --- |
| completed | 658 |
| errored | 10 |
| cancelled | 27 |
| in_progress | 17 |

| Model | Sessions |
| --- | --- |
| claude-opus-4.8 | 336 |
| gpt-5.5 | 183 |
| qwen3.6-plus | 139 |
| qwen3.6-27b | 52 |
| claude-fable-5 | 2 |

## Corrected Dashboard Score Snapshot

Live dashboard checked on July 7, 2026:

- Dashboard task count: 257.
- Tasks scored: 220.
- Scored sessions: 658.
- Total sessions: 712.
- Overall pass rate: 7.6%.
- Overall average score: 0.08.

These aggregate score fields were visible in the dashboard chart view but not present in the observed session API export, so they are not joined into individual CSV task rows.

## Static Buckets

| Bucket | Tasks |
| --- | --- |
| C_repair_candidate | 109 |
| B_close_verify_derivability | 92 |
| D_high_risk_manual_review | 39 |
| A_likely_good_spot_check | 17 |

Bucket meanings:

- `A_likely_good_spot_check`: low static risk; still needs sample environment verification.
- `B_close_verify_derivability`: probably recoverable, but hidden dependencies or branching need checking.
- `C_repair_candidate`: worth reviewing for repair, likely needs prompt/verifier/environment reconciliation.
- `D_high_risk_manual_review`: highest-risk tasks by static signals; inspect before spending recovery time.

The generated `task_recovery_ranked.csv` turns these buckets into an ordered recovery queue with the category, recommended action, risk score, and top reason for each task.

## Most Common Findings

| Finding | Tasks |
| --- | --- |
| FINANCE_SIDE_EFFECT_REVIEW | 195 |
| MANY_CROSS_SYSTEM_DEPENDENCIES | 178 |
| VERIFIER_ONLY_AMOUNTS | 121 |
| HEALTH_PRIVACY_REVIEW | 115 |
| VERIFIER_ONLY_USER_VALUES | 97 |
| RELATIVE_DATE_ANCHORS | 93 |
| HIGH_BRANCHING | 86 |
| MANY_LOOKUPS | 31 |
| LONG_PROMPT | 23 |
| PROMPT_APP_NOT_VERIFIED | 20 |

## Dependency Signals

| Dependency | Tasks |
| --- | --- |
| email_source | 195 |
| conditional_branch | 190 |
| bank_transactions | 153 |
| calendar_source | 152 |
| credit_card | 140 |
| invoice_bill | 120 |
| medical_record | 110 |
| personal_profile | 104 |
| math_or_aggregation | 80 |
| provider_search | 75 |

## Prompt App Families Missing From Verifier Apps

| App cue | Tasks |
| --- | --- |
| ledger | 8 |
| lifeline | 6 |
| medora | 5 |
| harbor | 2 |
| meridian | 1 |

## Highest-Priority Manual Review Queue

| Risk | Bucket | Env | Task | Findings | Prompt preview |
| --- | --- | --- | --- | --- | --- |
| 14.3 | D_high_risk_manual_review | psi-personal-health | task_matgvxxwzl4t_n_1781541869363_1kostyx0x__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I want to manage the asthma follow-up preparation, medication refill coordination, appointment management, calendar updates, and outstanding billing across Lifeline, Medora, and Latch. Start in Lifeline and review the... |
| 13.7 | D_high_risk_manual_review | psi-consumer-finance | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | Hiya, it's been a hectic afternoon, and we've been asked to provide a final cash position summary today for proper corporate accounting. Let us settle our outstanding credit card liability using an optimized rewards s... |
| 13.65 | D_high_risk_manual_review | psi-personal-health | task_qmr6zgds3jyt_n_1781554267041_qznhql8vr__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW | I am overdue on a general check-up so I want to schedule that today. Also, I am so glad I have finally been added to a dental insurance plan at work so I can finally book a dental consultation for my daughter, Lena. I... |
| 13.6 | D_high_risk_manual_review | psi-consumer-finance | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I just checked my inbox and found a recent email from Canopy Analytics this week regarding an invoice. They said that the invoice is tied to a grant reporting pack and that they need a confirmation or receipt before t... |
| 13.35 | D_high_risk_manual_review | psi-consumer-finance | task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | I requested a credit line increase on our Meridian account. Before I can complete the application, I need to verify income and housing expenses. I also want to evaluate whether Meridian's current balance transfer offe... |
| 13.2 | D_high_risk_manual_review | psi-consumer-finance | task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I have some spare time and I need to look into the bank alert that was sent to me on Latch yesterday. I flagged it to look into later, but now is the perfect time! Find the email and head to the mentioned app to look ... |
| 13.15 | D_high_risk_manual_review | psi-personal-health | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I have a medical appointment coming up this week (10/17/2025), but I also have other commitments I must attend to. I need to reschedule this to 10/23/2025 for 10 AM. I also need to schedule a dermatologist appointment... |
| 13.15 | D_high_risk_manual_review | psi-personal-health | task_iuxflcdhcj1y_n_1781704569850_f35noviu1__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I would like to book an appointment with a specialist because I have had some concerning symptoms flare up. I have been experiencing heartburn and an irregular heart beat recently for the first time. I need to schedul... |
| 12.9 | D_high_risk_manual_review | psi-personal-health | task_dq9a2ad6xvfw_n_1781641058767_tkzomw5l4__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | It's approaching the weekend and I need to cover any outstanding bills I have after my last appointment. In Lifeline, check my insurance claims. I'm positive I've paid all my insurance claims, but just to be sure, che... |
| 12.85 | D_high_risk_manual_review | psi-personal-health | task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I want to pay most of the Lifeline bills, except for Jordan's. I don't think I have access to pay for those. If he has a bill, send him an email using the last email address he emailed me from. The subject is "Bill fo... |
| 12.15 | D_high_risk_manual_review | psi-consumer-finance | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | Some freelance payments came into my Harbor Everyday Checking account as remote deposits between March 1, 2025, and October 14, 2025, that I never got around to recording in Ledger, and I want the books to reflect wha... |
| 12.05 | D_high_risk_manual_review | psi-consumer-finance | task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I’m mostly up to date with my invoice reconciliation in Ledger, but there are still a couple outstanding that I need to reconcile. For any invoices that are not already paid or draft, please cross check them against m... |
| 12.05 | D_high_risk_manual_review | psi-consumer-finance | task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|MANY_LOOKUPS\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I am trying to get together updated information to request a credit line increase with Meridian. I was invited to update them on my yearly salary and monthly spending a few days ago and would like to take the opportun... |
| 12.05 | D_high_risk_manual_review | psi-personal-health | task_z4ahj9ulywql_n_1781550013842_qu78voj1r__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I’ve got a suspicion that I’m going to have to tackle my high cholesterol problem sooner rather than later. Go find the results of my most recent fasting metabolic and lipid follow-up panel. If my LDL cholesterol numb... |
| 12.0 | D_high_risk_manual_review | psi-consumer-finance | task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | Today I'm responsible for organizing some things regarding payment and the bank account and I'll need your help. To start, in Meridian, pay the open bill that's due on October 18th, using the account with the highest ... |
| 11.95 | D_high_risk_manual_review | psi-consumer-finance | task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I am planning my Saturday. I will be spending time with Nora and running some errands. I don't want to forget anything, so I need you to make a list. In Latch, add all the tasks I mention to my day for the Saturday fo... |
| 11.65 | D_high_risk_manual_review | psi-consumer-finance | task_uegzt3a3alnr_n_1781718004093_kojk830fp__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I've just been approached by a new client who wants me to design a working dashboard for them within a week. I agreed, but only if they pay half of the total price as a deposit by tomorrow before I begin. I'll also ne... |
| 11.65 | D_high_risk_manual_review | psi-consumer-finance | task_w6gnjtwmquh5_n_1781290281803_tqfgsxjic__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I finally have time to clean up our subscriptions. An old StreamBox to-do has been sitting in my Latch tasks for months, and our reminder list in Ledger no longer matches what we actually pay. Start with the recurring... |
| 11.4 | D_high_risk_manual_review | psi-consumer-finance | task_vzcjibyaetrk_n_1781615300595_i4qiu5ili__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | There is so much I need to get done today, so I need your help with a couple of vendor issues. While you're in Ledger, find the bill BILL-00072 for the Harbor vendor and create an October planning duplicate version fr... |
| 11.35 | D_high_risk_manual_review | psi-consumer-finance | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I've let my spending go a little too freely this past month. I need to go through my finances today to make sure I have everything under control. Let's start with Bank of Harbor. My goal is to contribute at least $250... |
| 11.35 | D_high_risk_manual_review | psi-consumer-finance | task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | I’m planning to switch most of my bills over to my Meridian card so that I can get more rewards. We use a lot of points for trips. I need you to look at my last 4 available statements on my Harbor reward card and get ... |
| 11.3 | D_high_risk_manual_review | psi-consumer-finance | task_im4kbgyiwrpj_n_1781447840042_frjo4ut91__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | So I should be getting a freelance payment from Canopy Analytics. Can you check if it's been received, and then if you see it, please reconcile it in Ledger. Start with checking in Latch to see if I've received any in... |
| 11.25 | D_high_risk_manual_review | psi-consumer-finance | task_gth4zs74wcai_n_1781415785576_qzz51p63n__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | Our finance dept has asked us to tie up our operational expenses for the month. We have a few crucial service invoices to log, an email update to send out, and some cash flow adjustments to handle across our accounts ... |
| 11.2 | D_high_risk_manual_review | psi-consumer-finance | task_izn1wcinqm0z_n_1781652793067_3qijsf8bc__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I need to manage my card, update Ledger to include two new bills and do some banking. I want to get this done before the weekend, so I can relax and not have to think about it. So, let's get this all done today! I nee... |
| 11.15 | D_high_risk_manual_review | psi-personal-health | task_zo1had3vycvn_n_1781706559433_y744ddaat__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | My gynecologist canceled on me, and I'm only in my first trimester, so I'd like to schedule a new appointment with a gynecologist in Medora who accepts my current medical insurance. I need an appointment for prenatal ... |

## Low-Risk Spot-Check Candidates

| Risk | Env | Task | Dependencies | Prompt preview |
| --- | --- | --- | --- | --- |
| 1.35 | psi-consumer-finance | task_cytlhsftjt4w_n_1781809824975_0f53asur8__ayush_20260624__worktrial_taskloss_20260707 | credit_card\|invoice_bill | I recently started a cafe business and need to add some expenses/send some emails related to this new business. Start by adding three new vendors to Ledger. The vendors are: Bubble Coffee and Tea, Continental Staffing... |
| 1.35 | psi-consumer-finance | task_itcgbzweb4f_n_1781578835917_xls53dne2__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | Link three different accounts to Meridian that Membership Rewards points can be transferred to. The first is American Airlines with the account number AAA0001. The next is Southwest Airlines with the account number 55... |
| 2.75 | psi-personal-health | task_slp4u3rzfopo_n_1781542500425_w15v33oco__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|email_source\|medical_record | On Lifeline, please request another month's supply of Fluticasone Nasal Spray for myself and my spouse. Send them both to CVS Pharmacy 9005. On Latch, please e-mail "extracare@cvs.example". Title it "Prescription Coll... |
| 2.8 | psi-consumer-finance | task_prsuan6qpt7i_n_1781710814650_7bp8eojpk__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|conditional_branch\|email_source | Create a new bank account in Bank of Harbor. Name it "Payroll Checking" and use Everyday Checking as a funding source. Then transfer 15,000 from Everyday Checking to Payroll Checking. After that write an email to payr... |
| 2.85 | psi-consumer-finance | task_i6zm3orie1xt_n_1781541765635_vqk7rqgds__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|email_source\|invoice_bill | I noticed an overdue StreamBox bill while sorting my bills in Ledger. Even though we don't use it that much in my household, I received an email from them mentioning my next renewal estimate. I need this overdue bill ... |
| 3.1 | psi-personal-health | task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|medical_record | I would be traveling across continents for a work trip on the last day of October, and I would like to fully prepare myself health-wise. To avoid being unable to source my needed medication at my destination, using Li... |
| 3.15 | psi-consumer-finance | task_xkn9tpsou3bs_n_1781663250293_0738anpr2__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | I am going on a trip with my friend and she told me that she has been using her Meridian card to fund her vacation using points and special rewards. I want to take advantage of my accumulated points so that I can also... |
| 3.55 | psi-personal-health | task_gzrwcsxqsuy9_n_1781711196603_8tvw9iybb__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|medical_record\|provider_search | I have been having toothaches every night after work. In Medora, I need you to add a dentist to my care team who is within a 5-mile radius of me and has a slot on October 17, 2025. Make sure you choose the doctor with... |
| 3.6 | psi-consumer-finance | task_hscavs4v3fgy_n_1781202617540_mqbfz8zmb__ayush_20260624__worktrial_taskloss_20260707 | email_source\|invoice_bill\|math_or_aggregation\|personal_profile | In Ledger, add a customer named Deen Hotel. The customer's email is deenhotelbilling@gmail.com and phone number +1 (305) 555-8123. Enter the street address as 207 Market Street, Tacoma, WA. Enter the city as Tacoma, s... |
| 3.6 | psi-personal-health | task_ru0dyrkku4o4_n_1781555298195_4ox33xy0p__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|medical_record\|provider_search | I just got dental insurance. In Medora, add Anthem Blue Cross Blue Shield Dental HMO as my dental policy. Add a new dentist to my care team. I want the dentist to speak English, be female and in-network. Schedule an i... |
| 3.6 | psi-consumer-finance | task_ts6d9ka5kz7_n_1781217047925_t4c42psvu__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card\|invoice_bill\|math_or_aggregation | Please open a new Bank of Harbor checking account. Use our existing Harbor checking account for the initial funding, and decline the option for a debit card. Once the new account is open, make a transfer of $15,000 in... |
| 3.65 | psi-personal-health | task_qy2onlerz48v_n_1781514016667_k1btarxvl__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|credit_card\|medical_record\|provider_search | Maya's asthma medications are up for renewal around her October 20 visit. She needs to route them correctly, prepare for the visit, notify her provider, contact the pharmacy, and calendar it. In the Medications sectio... |
| 3.7 | psi-consumer-finance | task_nar7e2gtnjoh_n_1781353535789_u0hj99t56__ayush_20260624__worktrial_taskloss_20260707 | email_source\|invoice_bill\|personal_profile | In Ledger, add a new active service called 'Lawful Representation'. Describe it as 'Representing a client'. Its sales price is $500.00 and the income account is 4010- Freelance Income. There's no expense account. Add ... |
| 3.7 | psi-consumer-finance | task_orujw4a5pvn_n_1781283294876_jhv3j1k8f__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|calendar_source\|credit_card\|invoice_bill | My friend told me that the best way to secure your money is with a money market account, and I’m beginning to think she’s right. Open a new money market account in Harbor funded by my checking account nicknamed “Secur... |
| 3.8 | psi-consumer-finance | task_gb00g825zcbe_n_1781522644893_lcszvr1e5__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|calendar_source\|credit_card\|email_source\|invoice_bill\|personal_profile | A new customer needs to be onboarded into Ledger. The name of the customer is Johnstone Avery. The email of the customer is js.avery@example.com, and their phone number is +1(253) 555-9876. The customer's address is 7... |
| 3.85 | psi-consumer-finance | task_xydczzczbelt_n_1781389103427_6zgjp7p7g__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | I am going on vacation soon and am putting aside a vacation fund. Please open a new checking account in Harbor funded by my everyday checking account named "Vacation Fund". Make sure "Send me a new debit card for this... |
| 4.0 | psi-consumer-finance | task_yktbgqjdiox_n_1781235421200_h1md9xdpg__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|conditional_branch\|email_source\|invoice_bill | I am trying to keep up with all the subscriptions I have taken on and have found that some are not necessary. I must make sure I have paid all my subscriptions and that all is up to date in Ledger. There appears to be... |

## How To Use This

Start with the highest-priority queue to learn failure modes, then sample each bucket and environment. Promote tasks only after checking that prompt facts, verifier expectations, and world data reconcile.
