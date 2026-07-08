# Project One Static QA Summary

This report is a first-pass static triage over the exported JSONL dataset. It flags review leads; it does not replace environment inspection or human judgment.

## Dataset Shape

- Tasks: 520
- Risk score min/median/mean/max: 1.35 / 7.25 / 7.35 / 14.85

| Environment | Tasks |
| --- | --- |
| psi-consumer-finance | 313 |
| psi-personal-health | 207 |

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

## Static Buckets

| Bucket | Tasks |
| --- | --- |
| C_repair_candidate | 214 |
| B_close_verify_derivability | 201 |
| D_high_risk_manual_review | 66 |
| A_likely_good_spot_check | 39 |

Bucket meanings:

- `A_likely_good_spot_check`: low static risk; still needs sample environment verification.
- `B_close_verify_derivability`: probably recoverable, but hidden dependencies or branching need checking.
- `C_repair_candidate`: worth reviewing for repair, likely needs prompt/verifier/environment reconciliation.
- `D_high_risk_manual_review`: highest-risk tasks by static signals; inspect before spending recovery time.

## Most Common Findings

| Finding | Tasks |
| --- | --- |
| FINANCE_SIDE_EFFECT_REVIEW | 408 |
| MANY_CROSS_SYSTEM_DEPENDENCIES | 337 |
| VERIFIER_ONLY_AMOUNTS | 247 |
| HEALTH_PRIVACY_REVIEW | 220 |
| VERIFIER_ONLY_USER_VALUES | 193 |
| RELATIVE_DATE_ANCHORS | 190 |
| HIGH_BRANCHING | 152 |
| MANY_LOOKUPS | 77 |
| LONG_PROMPT | 40 |
| PROMPT_APP_NOT_VERIFIED | 34 |

## Dependency Signals

| Dependency | Tasks |
| --- | --- |
| conditional_branch | 366 |
| email_source | 362 |
| bank_transactions | 325 |
| calendar_source | 306 |
| credit_card | 291 |
| invoice_bill | 247 |
| medical_record | 213 |
| personal_profile | 197 |
| math_or_aggregation | 176 |
| provider_search | 136 |

## Prompt App Families Missing From Verifier Apps

| App cue | Tasks |
| --- | --- |
| ledger | 16 |
| lifeline | 11 |
| medora | 6 |
| harbor | 3 |
| meridian | 1 |

## Highest-Priority Manual Review Queue

| Risk | Bucket | Env | Task | Findings | Prompt preview |
| --- | --- | --- | --- | --- | --- |
| 14.85 | D_high_risk_manual_review | psi-personal-health | task_uafdddxsii5f_n_1781580009873_ye68x4ssy__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I need to get my payments sorted for my health stuff as I have been getting calls, texts, etc., asking for payments. However, I have no idea why I still have money due. I thought I had paid it all off last month. Coul... |
| 14.55 | D_high_risk_manual_review | psi-consumer-finance | task_vgekb6ez2mk_n_1781691388858_cx87x0003__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I want to proactively follow up on customers with outstanding balances while ensuring that expected incoming payments are properly tracked and reserved. In Ledger, identify the two customers with the highest open bala... |
| 14.3 | D_high_risk_manual_review | psi-personal-health | task_matgvxxwzl4t_n_1781541869363_1kostyx0x__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I want to manage the asthma follow-up preparation, medication refill coordination, appointment management, calendar updates, and outstanding billing across Lifeline, Medora, and Latch. Start in Lifeline and review the... |
| 13.75 | D_high_risk_manual_review | psi-consumer-finance | task_g9jcqlioeg_n_1781363550879_h4ee24f4t__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I'm getting a draft invoice ready for one of my customers and, as part of a promotion, I'd also like to send them a small reward while I finalize everything. In Ledger, find the customer "Elevate Embedded LLC" and upd... |
| 13.7 | D_high_risk_manual_review | psi-consumer-finance | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | Hiya, it's been a hectic afternoon, and we've been asked to provide a final cash position summary today for proper corporate accounting. Let us settle our outstanding credit card liability using an optimized rewards s... |
| 13.65 | D_high_risk_manual_review | psi-personal-health | task_qmr6zgds3jyt_n_1781554267041_qznhql8vr__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW | I am overdue on a general check-up so I want to schedule that today. Also, I am so glad I have finally been added to a dental insurance plan at work so I can finally book a dental consultation for my daughter, Lena. I... |
| 13.6 | D_high_risk_manual_review | psi-consumer-finance | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I need your help with a subscription billing audit. First, review the relevant subscription activity in Harbor and Ledger: - Compare the StreamBox bill payment in scheduled transfers in Harbor (Pay & Transfer) with th... |
| 13.6 | D_high_risk_manual_review | psi-consumer-finance | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I just checked my inbox and found a recent email from Canopy Analytics this week regarding an invoice. They said that the invoice is tied to a grant reporting pack and that they need a confirmation or receipt before t... |
| 13.35 | D_high_risk_manual_review | psi-consumer-finance | task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | I requested a credit line increase on our Meridian account. Before I can complete the application, I need to verify income and housing expenses. I also want to evaluate whether Meridian's current balance transfer offe... |
| 13.2 | D_high_risk_manual_review | psi-consumer-finance | task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I have some spare time and I need to look into the bank alert that was sent to me on Latch yesterday. I flagged it to look into later, but now is the perfect time! Find the email and head to the mentioned app to look ... |
| 13.15 | D_high_risk_manual_review | psi-personal-health | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I have a medical appointment coming up this week (10/17/2025), but I also have other commitments I must attend to. I need to reschedule this to 10/23/2025 for 10 AM. I also need to schedule a dermatologist appointment... |
| 13.15 | D_high_risk_manual_review | psi-personal-health | task_iuxflcdhcj1y_n_1781704569850_f35noviu1__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I would like to book an appointment with a specialist because I have had some concerning symptoms flare up. I have been experiencing heartburn and an irregular heart beat recently for the first time. I need to schedul... |
| 12.9 | D_high_risk_manual_review | psi-personal-health | task_dq9a2ad6xvfw_n_1781641058767_tkzomw5l4__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | It's approaching the weekend and I need to cover any outstanding bills I have after my last appointment. In Lifeline, check my insurance claims. I'm positive I've paid all my insurance claims, but just to be sure, che... |
| 12.85 | D_high_risk_manual_review | psi-personal-health | task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I want to pay most of the Lifeline bills, except for Jordan's. I don't think I have access to pay for those. If he has a bill, send him an email using the last email address he emailed me from. The subject is "Bill fo... |
| 12.6 | D_high_risk_manual_review | psi-consumer-finance | task_g7z1w88tzgi_n_1781373040055_28w1j82eb__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | A few client invoices in Ledger need attention before the next payment batch closes. Pull up the Sales Invoices view and check the status filter for Overdue, then separately check for Sent, combining both result sets.... |
| 12.15 | D_high_risk_manual_review | psi-consumer-finance | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | Some freelance payments came into my Harbor Everyday Checking account as remote deposits between March 1, 2025, and October 14, 2025, that I never got around to recording in Ledger, and I want the books to reflect wha... |
| 12.05 | D_high_risk_manual_review | psi-consumer-finance | task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|FINANCE_SIDE_EFFECT_REVIEW | I’m mostly up to date with my invoice reconciliation in Ledger, but there are still a couple outstanding that I need to reconcile. For any invoices that are not already paid or draft, please cross check them against m... |
| 12.05 | D_high_risk_manual_review | psi-consumer-finance | task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|MANY_LOOKUPS\|PROMPT_APP_NOT_VERIFIED\|VERIFIER_ONLY_AMOUNTS\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I am trying to get together updated information to request a credit line increase with Meridian. I was invited to update them on my yearly salary and monthly spending a few days ago and would like to take the opportun... |
| 12.05 | D_high_risk_manual_review | psi-personal-health | task_z4ahj9ulywql_n_1781550013842_qu78voj1r__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I’ve got a suspicion that I’m going to have to tackle my high cholesterol problem sooner rather than later. Go find the results of my most recent fasting metabolic and lipid follow-up panel. If my LDL cholesterol numb... |
| 12.0 | D_high_risk_manual_review | psi-consumer-finance | task_asvghzavjtzg_n_1781585241181_ywf3rxzj3__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|MANY_LOOKUPS\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I was on a trip with my friend from October 5 to October 10 and paid for some of the expenses that we had together to simplify things. We agreed that we would split up these expenses later. Now, after the trip, I want... |
| 12.0 | D_high_risk_manual_review | psi-personal-health | task_iegiud4ie8sa_n_1781547489845_yey638yu1__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|VERIFIER_ONLY_USER_VALUES\|HEALTH_PRIVACY_REVIEW\|FINANCE_SIDE_EFFECT_REVIEW | I broke my tooth and I need to schedule an urgent visit to a dentist ASAP. Please schedule an appointment in Medora with a dentist that has availability for an urgent visit at the earliest time, on 10/15. I can't spea... |
| 12.0 | D_high_risk_manual_review | psi-consumer-finance | task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|FINANCE_SIDE_EFFECT_REVIEW | Today I'm responsible for organizing some things regarding payment and the bank account and I'll need your help. To start, in Meridian, pay the open bill that's due on October 18th, using the account with the highest ... |
| 11.95 | D_high_risk_manual_review | psi-consumer-finance | task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707 | MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_USER_VALUES\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | I am planning my Saturday. I will be spending time with Nora and running some errands. I don't want to forget anything, so I need you to make a list. In Latch, add all the tasks I mention to my day for the Saturday fo... |
| 11.85 | D_high_risk_manual_review | psi-consumer-finance | task_edbhacdtf15c_n_1781591126430_n3nla40f5__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | My tasks for today are to pay outstanding bills for this month, to update bills in Ledger, if necessary, and to check if I have enough money on my Harbor account for upcoming expenses and bills. I also do not want to ... |
| 11.85 | D_high_risk_manual_review | psi-consumer-finance | task_h5krxt4vgizt_n_1781612831028_di2o7s7lk__ayush_20260624__worktrial_taskloss_20260707 | RELATIVE_DATE_ANCHORS\|MANY_CROSS_SYSTEM_DEPENDENCIES\|HIGH_BRANCHING\|VERIFIER_ONLY_AMOUNTS\|LONG_PROMPT\|FINANCE_SIDE_EFFECT_REVIEW | Hi, a bunch of payments are about to hit my Harbor checking over the next day or two, and my Meridian card payment is coming out of the same account, so I want to make sure my checking does not drop below my safety fl... |

## Low-Risk Spot-Check Candidates

| Risk | Env | Task | Dependencies | Prompt preview |
| --- | --- | --- | --- | --- |
| 1.35 | psi-consumer-finance | task_cytlhsftjt4w_n_1781809824975_0f53asur8__ayush_20260624__worktrial_taskloss_20260707 | credit_card\|invoice_bill | I recently started a cafe business and need to add some expenses/send some emails related to this new business. Start by adding three new vendors to Ledger. The vendors are: Bubble Coffee and Tea, Continental Staffing... |
| 1.35 | psi-consumer-finance | task_itcgbzweb4f_n_1781578835917_xls53dne2__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | Link three different accounts to Meridian that Membership Rewards points can be transferred to. The first is American Airlines with the account number AAA0001. The next is Southwest Airlines with the account number 55... |
| 1.35 | psi-consumer-finance | task_nfbkdbttwpyt_n_1781280049363_92hkehhrr__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | Open a Money Market account using my Everyday Checking account as the funding source. I do not need a debit card for this account. Transfer $815 from the Emergency Savings Account to the newly opened account. Then add... |
| 2.15 | psi-personal-health | task_dqmnq5uggp5m_n_1781591780653_gyd1dmse0__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|email_source\|personal_profile | I was speaking to Jordan who told me that there is some issue with his account and he is unable to access it. He needs to add an emergency contact, grant access to his father and also pay off the outstanding balance t... |
| 2.35 | psi-personal-health | task_iorgyu3zfk0f_n_1781566916086_eciynpbma__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|email_source\|medical_record | I'm currently on vacation and have developed a painful toothache, so I need help finding a dentist in the city who accepts my new insurance plan. First, I need to add the new insurance plan I just signed up for. In my... |
| 2.4 | psi-consumer-finance | task_ai5uwt54g6am_n_1781330777477_3d8ro6ize__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|invoice_bill\|personal_profile | Please help manage my recurring payment on Harbor and Ledger. First, please do verification for the existing external recipient account that belongs to BridgePay Advance Repayment by detecting the two micro-deposit am... |
| 2.4 | psi-consumer-finance | task_w1fsdm7n5mg0_n_1781264064205_yfeqg90ci__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|invoice_bill\|personal_profile | I recently purchased a pair of limited-edition Air Jordan sneakers and need to complete payment and properly record the transaction. In Harbor, create a new domestic transfer recipient using the following information:... |
| 2.5 | psi-personal-health | task_kz5rdcamz9mz_n_1781737787987_kwddrzl5t__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|email_source\|medical_record | I would like to give my family proxy access to my Lifeline account. These people are my husband, mother, and father-in-law, who can all be found in my account. Lena's email is "lena.rivera@riverapierce.example", Jorda... |
| 2.6 | psi-consumer-finance | task_kfncskd6asj_n_1781554649693_dbnrhy12u__ayush_20260624__worktrial_taskloss_20260707 | email_source\|invoice_bill\|personal_profile | Add three companies as vendors to Ledge using only the Vendor Name, Email, and Display Name fields. The first vendor is Super Online Streaming with the email address superstreamonline+1@vendor.example and phone number... |
| 2.75 | psi-personal-health | task_slp4u3rzfopo_n_1781542500425_w15v33oco__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|email_source\|medical_record | On Lifeline, please request another month's supply of Fluticasone Nasal Spray for myself and my spouse. Send them both to CVS Pharmacy 9005. On Latch, please e-mail "extracare@cvs.example". Title it "Prescription Coll... |
| 2.8 | psi-consumer-finance | task_prsuan6qpt7i_n_1781710814650_7bp8eojpk__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|conditional_branch\|email_source | Create a new bank account in Bank of Harbor. Name it "Payroll Checking" and use Everyday Checking as a funding source. Then transfer 15,000 from Everyday Checking to Payroll Checking. After that write an email to payr... |
| 2.85 | psi-consumer-finance | task_i6zm3orie1xt_n_1781541765635_vqk7rqgds__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|email_source\|invoice_bill | I noticed an overdue StreamBox bill while sorting my bills in Ledger. Even though we don't use it that much in my household, I received an email from them mentioning my next renewal estimate. I need this overdue bill ... |
| 3.05 | psi-personal-health | task_xutdxqezilz_n_1781588126425_ra36a8nsf__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|medical_record | My asthma has been acting up and I need some help moving up an appointment and refilling my prescription to avoid it getting any worse. In Medora, reschedule my October 17, 2025 appointment with Dr. James Wu. Book the... |
| 3.1 | psi-personal-health | task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|medical_record | I would be traveling across continents for a work trip on the last day of October, and I would like to fully prepare myself health-wise. To avoid being unable to source my needed medication at my destination, using Li... |
| 3.15 | psi-consumer-finance | task_xkn9tpsou3bs_n_1781663250293_0738anpr2__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|credit_card | I am going on a trip with my friend and she told me that she has been using her Meridian card to fund her vacation using points and special rewards. I want to take advantage of my accumulated points so that I can also... |
| 3.2 | psi-personal-health | task_xicjtv23zf_n_1781545679960_g37go0huq__ayush_20260624__worktrial_taskloss_20260707 | email_source\|medical_record | Complete the unfinished task in Medora by uploading ID 1. Include "Checkup" as the reason for the visit Request a 1-month refill supply of the spray medication in Epic. Send a message with subject: "Refill", to Primar... |
| 3.3 | psi-personal-health | task_bk0qredhb4zf_n_1781547819546_jekxhw28t__ayush_20260624__worktrial_taskloss_20260707 | calendar_source\|email_source\|medical_record\|provider_search | In Lifeline, make annual physical appointments in the pediatrics specialty for Lena Rivera and Omar Pierce. I want both appointments to be on October 20th, 2025. Make Lena's at 9am and Omar's one hour and 30 minutes a... |
| 3.4 | psi-consumer-finance | task_gbahkllstav_n_1781645232549_fp3ung43v__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|email_source\|invoice_bill\|personal_profile | A friend of mine needs money to go to a convention for the weekend, and needs to borrow some money, with him promising to pay me back at the end of the month. As I use my Ledger account for all of my finances, busines... |
| 3.4 | psi-consumer-finance | task_glazmldynpfb_n_1781461743108_cw7eqgzmi__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|invoice_bill\|personal_profile | I'm just back from signing a new contract with Zambezi Fisheries, and they gave me the first check for $2000, so we can go ahead and add them as a new customer in Ledger. Their details are accounts@zambezi.example, (6... |
| 3.45 | psi-consumer-finance | task_itzujkm0rppy_n_1781545486264_n5nvcjhj8__ayush_20260624__worktrial_taskloss_20260707 | bank_transactions\|conditional_branch\|credit_card\|invoice_bill | I need some help reorganising my bank accounts, updating the details across systems and recategorizing some transactions. In Harbor, please open a new checking account called 'Prime Checking', using the everyday check... |

## How To Use This

Start with the highest-priority queue to learn failure modes, then sample each bucket and environment. Promote tasks only after checking that prompt facts, verifier expectations, and world data reconcile.
