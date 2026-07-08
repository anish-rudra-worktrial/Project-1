# Constant Derivability Worklist

This is a second QA layer on top of the static triage. It extracts verifier constants that are not obviously present in the prompt and turns them into a review queue.

A row here is not automatically a bug. It is a concrete question for a human reviewer: can this verifier value be uniquely derived from the prompt and seed world?

## Shape

- Tasks scanned: 520
- Constants requiring review: 3729
- Tasks represented: 513

| Priority | Rows |
| --- | --- |
| high | 3646 |
| medium | 83 |

| Constant type | Rows |
| --- | --- |
| money | 1462 |
| date | 1425 |
| name_or_label | 606 |
| email | 222 |
| phone | 14 |

| Likely source app | Rows |
| --- | --- |
| meridian | 1079 |
| medora | 1061 |
| harbor | 647 |
| ledger | 505 |
| lifeline | 254 |
| communications | 183 |

| Task bucket | Rows |
| --- | --- |
| C_repair_candidate | 1737 |
| B_close_verify_derivability | 1199 |
| D_high_risk_manual_review | 677 |
| A_likely_good_spot_check | 116 |

## Tasks With The Most Constants To Prove

| Constants | Bucket | Task |
| --- | --- | --- |
| 36 | D_high_risk_manual_review | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 |
| 23 | D_high_risk_manual_review | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 |
| 23 | C_repair_candidate | task_alheo0s3pevg_n_1781556624781_77zesa09d__ayush_20260624__worktrial_taskloss_20260707 |
| 22 | C_repair_candidate | task_vcq4qlugudy_n_1781514280178_w72jdy7k4__ayush_20260624__worktrial_taskloss_20260707 |
| 21 | B_close_verify_derivability | task_smdfxsbrq2u_n_1781371133671_chhxfi6y6__ayush_20260624__worktrial_taskloss_20260707 |
| 20 | C_repair_candidate | task_gxijjqyryyx6_n_1781515450316_jiheubjn6__ayush_20260624__worktrial_taskloss_20260707 |
| 20 | C_repair_candidate | task_zzt4es93lpsi_n_1781989274882_qxwcxipxr__ayush_20260624__worktrial_taskloss_20260707 |
| 19 | D_high_risk_manual_review | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 |
| 19 | C_repair_candidate | task_ykudav7z9ttu_n_1781653385805_diq9r462p__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | D_high_risk_manual_review | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | B_close_verify_derivability | task_fjogxadsqh4_n_1781652563501_dqlt8wk01__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | B_close_verify_derivability | task_pmklilrpcia_n_1781549190432_1vim7mfdd__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | D_high_risk_manual_review | task_pukb1eshzc1k_n_1781701090123_uwa276ndg__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | D_high_risk_manual_review | task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_m7tc4brunifj_n_1781636191630_fg6qpd5ch__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_uxma8v1ewo_n_1781555246021_3cfngm8ce__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_onilbqfwupd9_n_1781684537330_c9kd9bc2h__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_bshwzmkvvma2_n_1781628770617_53s1xjj5t__ayush_20260624__worktrial_taskloss_20260707 |
| 16 | D_high_risk_manual_review | task_ato4elb7m1bc_n_1781282633340_d77bfypkg__ayush_20260624__worktrial_taskloss_20260707 |
| 16 | D_high_risk_manual_review | task_sfjed1tt1gst_n_1781652381399_3vhhv330i__ayush_20260624__worktrial_taskloss_20260707 |

## Highest-Priority Rows

| Priority | Bucket | Type | Source app | Constant | Task | Question |
| --- | --- | --- | --- | --- | --- | --- |
| high | D_high_risk_manual_review | money | ledger | 1642.5 | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 480 | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 709.78 | task_abnoxqu8myxh_n_1781539233132_asy21q4wt__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | ledger | 875 | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | ledger | 18.63 | task_qraur0syjg66_n_1781196573639_he8xokeyy__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 514.82 | task_edbhacdtf15c_n_1781591126430_n3nla40f5__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | harbor | 482.78 | task_ato4elb7m1bc_n_1781282633340_d77bfypkg__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | ledger | 2400 | task_bldwgko1jup_n_1781355522269_qwmhwh80q__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 9271.42 | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 20 | task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_pukb1eshzc1k_n_1781701090123_uwa276ndg__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | ledger | 18.63 | task_w6gnjtwmquh5_n_1781290281803_tqfgsxjic__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 4735.41 | task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_zgp4orqdpb0_n_1781512927273_bw57xtk3a__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_glvi0nyc1p6y_n_1781782792093_gihqex5xi__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_uafdddxsii5f_n_1781580009873_ye68x4ssy__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | harbor | 2400 | task_g9jcqlioeg_n_1781363550879_h4ee24f4t__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | meridian | 17.66 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 37.49 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 78.06 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_ituuqltofn1_n_1781551596197_coj6bor1d__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_uie3badamyzk_n_1781520506149_84x4sunuf__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 18.63 | task_edbhacdtf15c_n_1781591126430_n3nla40f5__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | harbor | 18.63 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | harbor | 187.5 | task_yqupdaywlvqb_n_1781306014106_ejs854ja4__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_snomzyg0aaz_n_1781541336492_kon2jr7io__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | communications | 1264.59 | task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | communications | 6000 | task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | ledger | 1517 | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 9247.42 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | communications | 123.8 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | harbor | 21.96 | task_icch7e5wbqm_n_1781757558776_dbq3igpwl__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_iegiud4ie8sa_n_1781547489845_yey638yu1__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | communications | 1470.86 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_im4kbgyiwrpj_n_1781447840042_frjo4ut91__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | ledger | 18.63 | task_irxxgeka5ymu_n_1781636326568_4dohzda2x__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |

## How To Use This

1. Open `derivability_worklist.csv` and filter to `review_priority=high`.
2. For each row, inspect the prompt, verifier context, and seed/session evidence.
3. Mark the constant as explicitly prompted, uniquely derivable, ambiguous, or not derivable.
4. Promote the task only when every verifier constant used for success is grounded.

## Limits

- This is still static analysis; it does not open seed databases or recordings.
- The likely source app is heuristic, especially for cross-app tasks.
- Some constants are valid no-change guards or implementation details despite looking user-visible.
- The best next step is to connect these rows to seed-data probes for the highest-volume apps.
