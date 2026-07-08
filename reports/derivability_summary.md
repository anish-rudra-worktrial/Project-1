# Constant Derivability Worklist

This is a second QA layer on top of the static triage. It extracts verifier constants that are not obviously present in the prompt and turns them into a review queue.

A row here is not automatically a bug. It is a concrete question for a human reviewer: can this verifier value be uniquely derived from the prompt and seed world?

## Scope

Scope: tasks present in the supplied triage CSV. With the current session-backed Project One triage, this scans 257 tasks and drops 263 tasks outside that triage scope.

## Shape

- Tasks scanned: 257
- Constants requiring review: 1843
- Tasks represented: 254

| Priority | Rows |
| --- | --- |
| high | 1801 |
| medium | 42 |

| Constant type | Rows |
| --- | --- |
| date | 710 |
| money | 689 |
| name_or_label | 315 |
| email | 120 |
| phone | 9 |

| Likely source app | Rows |
| --- | --- |
| medora | 561 |
| meridian | 490 |
| harbor | 299 |
| ledger | 275 |
| lifeline | 126 |
| communications | 92 |

| Task bucket | Rows |
| --- | --- |
| C_repair_candidate | 849 |
| B_close_verify_derivability | 537 |
| D_high_risk_manual_review | 395 |
| A_likely_good_spot_check | 62 |

## Tasks With The Most Constants To Prove

| Constants | Bucket | Task |
| --- | --- | --- |
| 23 | D_high_risk_manual_review | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 |
| 23 | C_repair_candidate | task_alheo0s3pevg_n_1781556624781_77zesa09d__ayush_20260624__worktrial_taskloss_20260707 |
| 19 | D_high_risk_manual_review | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | D_high_risk_manual_review | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | B_close_verify_derivability | task_fjogxadsqh4_n_1781652563501_dqlt8wk01__ayush_20260624__worktrial_taskloss_20260707 |
| 18 | B_close_verify_derivability | task_pmklilrpcia_n_1781549190432_1vim7mfdd__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | D_high_risk_manual_review | task_z5zra8ojflf_n_1781340792001_t94q3vmad__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_m7tc4brunifj_n_1781636191630_fg6qpd5ch__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_uxma8v1ewo_n_1781555246021_3cfngm8ce__ayush_20260624__worktrial_taskloss_20260707 |
| 17 | C_repair_candidate | task_bshwzmkvvma2_n_1781628770617_53s1xjj5t__ayush_20260624__worktrial_taskloss_20260707 |
| 16 | C_repair_candidate | task_f1bvegtdpsxb_n_1781534688885_cn7qn7oml__ayush_20260624__worktrial_taskloss_20260707 |
| 16 | C_repair_candidate | task_lpiswvg5prl7_n_1781655481539_5ia9eui9p__ayush_20260624__worktrial_taskloss_20260707 |
| 15 | C_repair_candidate | task_dlmkv6otfy07_n_1781138793510_cvrqys0hh__ayush_20260624__worktrial_taskloss_20260707 |
| 15 | C_repair_candidate | task_lhywptsxf6rj_n_1781648186758_kafn22w68__ayush_20260624__worktrial_taskloss_20260707 |
| 15 | C_repair_candidate | task_itxp4ethttx_n_1781631113910_suu69rryw__ayush_20260624__worktrial_taskloss_20260707 |
| 15 | C_repair_candidate | task_va1awtrgcirv_n_1781386064473_w5we5z8oi__ayush_20260624__worktrial_taskloss_20260707 |
| 14 | D_high_risk_manual_review | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 |
| 14 | D_high_risk_manual_review | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 |
| 14 | D_high_risk_manual_review | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 |
| 14 | C_repair_candidate | task_xojc6xarjoh_n_1781646774710_2ukoc3g99__ayush_20260624__worktrial_taskloss_20260707 |

## Highest-Priority Rows

| Priority | Bucket | Type | Source app | Constant | Task | Question |
| --- | --- | --- | --- | --- | --- | --- |
| high | D_high_risk_manual_review | money | ledger | 1642.5 | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 480 | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | ledger | 875 | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | ledger | 2400 | task_bldwgko1jup_n_1781355522269_qwmhwh80q__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 9271.42 | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 20 | task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 18.63 | task_w6gnjtwmquh5_n_1781290281803_tqfgsxjic__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 4735.41 | task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_glvi0nyc1p6y_n_1781782792093_gihqex5xi__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 14486.83 | task_qzuenxoozak_n_1781195720034_vv4ic4hmb__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | harbor | 187.5 | task_yqupdaywlvqb_n_1781306014106_ejs854ja4__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_snomzyg0aaz_n_1781541336492_kon2jr7io__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | communications | 1264.59 | task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | communications | 6000 | task_udwrcq8akbx8_n_1781633202566_j8zdw3grb__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | ledger | 1517 | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 9247.42 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | communications | 1470.86 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this amount be uniquely derived from seed data rather than being verifier-only ground truth? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_im4kbgyiwrpj_n_1781447840042_frjo4ut91__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 17 | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | lifeline | 30 | task_ivnptdiryl3z_n_1781663573660_22n9ikfo2__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_matgvxxwzl4t_n_1781541869363_1kostyx0x__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 1500 | task_gth4zs74wcai_n_1781415785576_qzz51p63n__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | lifeline | 20 | task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | lifeline | 62.47 | task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | ledger | 517 | task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 504 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | lifeline | 30 | task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707 | Can this health billing amount be uniquely derived from Lifeline records? |
| high | D_high_risk_manual_review | money | harbor | 354.92 | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | meridian | 134925 | task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | meridian | 200 | task_uegzt3a3alnr_n_1781718004093_kojk830fp__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |
| high | D_high_risk_manual_review | money | ledger | 1875 | task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | harbor | 2517.5 | task_bjqxsskmpxeq_n_1781476993426_gmm015kra__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | harbor | 125 | task_hu7u8hnudhu_n_1781411729307_bvabegg9q__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | harbor | 159.68 | task_i8xzvmzsxsql_n_1781700231775_h6zh3s0cg__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | harbor | 271.42 | task_nvpb0yuy1mj0_n_1781615257807_i11yigal7__ayush_20260624__worktrial_taskloss_20260707 | Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules? |
| high | D_high_risk_manual_review | money | ledger | 18.63 | task_itxsazhocgr_n_1781289458817_snuiks36m__ayush_20260624__worktrial_taskloss_20260707 | Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records? |
| high | D_high_risk_manual_review | money | meridian | 8575.46 | task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707 | Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters? |

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
