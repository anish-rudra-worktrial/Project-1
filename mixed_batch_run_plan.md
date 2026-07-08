# Mixed Batch Run Plan

Selected 48 tasks: 6 from each environment x bucket stratum.

## Run Created

- Job name: `codex-mixed-batch-48-stratified`
- Job ID: `704a285a-b5d1-437b-8322-c1be58b3e422`
- Dashboard URL: `https://fleetai.com/dashboard/jobs/704a285a-b5d1-437b-8322-c1be58b3e422`
- Model: `anthropic/claude-fable-5`
- Pass@K: 1
- Max steps: 999
- Tasks selected: 48
- Sessions created: 48
- Observed status after launch: `In Progress`
- Notes: The job initially showed `0 tasks / No sessions found` immediately after submit, then populated after refresh with 48 task groups and one session each.

## Later Dashboard Recheck

The dataset dashboard moved from 713 total sessions after the one-task spot check to 761 total sessions after this batch, which matches the 48 sessions created here.

- Scored sessions visible at recheck: 7.
- Tasks scored at recheck: 6.
- Overall pass rate on scored sessions: 28.6%.
- Overall average score on scored sessions: 0.29.
- `anthropic/claude-fable-5` totals: 51 total sessions, 7 scored sessions, 6 scored tasks.

I would not treat those 7 scored sessions as representative of the full dataset. They are useful as a smoke test showing that the batch run registered and some grading completed, while the Project One handoff should continue to lean on the full static triage, derivability worklist, and human verification sample.

| Environment | Bucket | Available | Selected | Selected with prior sessions |
| --- | --- | ---: | ---: | ---: |
| `psi-consumer-finance` | `A_likely_good_spot_check` | 23 | 6 | 6 |
| `psi-consumer-finance` | `B_close_verify_derivability` | 128 | 6 | 6 |
| `psi-consumer-finance` | `C_repair_candidate` | 119 | 6 | 6 |
| `psi-consumer-finance` | `D_high_risk_manual_review` | 43 | 6 | 6 |
| `psi-personal-health` | `A_likely_good_spot_check` | 16 | 6 | 5 |
| `psi-personal-health` | `B_close_verify_derivability` | 73 | 6 | 6 |
| `psi-personal-health` | `C_repair_candidate` | 95 | 6 | 6 |
| `psi-personal-health` | `D_high_risk_manual_review` | 23 | 6 | 6 |

## Task Keys

- `task_i6zm3orie1xt_n_1781541765635_vqk7rqgds__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `2.85`, sessions `3`
- `task_hscavs4v3fgy_n_1781202617540_mqbfz8zmb__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `3.6`, sessions `3`
- `task_orujw4a5pvn_n_1781283294876_jhv3j1k8f__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `3.7`, sessions `3`
- `task_gb00g825zcbe_n_1781522644893_lcszvr1e5__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `3.8`, sessions `3`
- `task_xydczzczbelt_n_1781389103427_6zgjp7p7g__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `3.85`, sessions `3`
- `task_yktbgqjdiox_n_1781235421200_h1md9xdpg__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `A_likely_good_spot_check`, risk `4.0`, sessions `3`
- `task_tqwet5cnm_n_1781199538326_4qjwqnf3e__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `5.35`, sessions `4`
- `task_xyxx2vpkrek_n_1781607774982_827vogeju__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `5.7`, sessions `4`
- `task_zidagf17yxuq_n_1781294888177_lqtg1ka30__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `4.05`, sessions `3`
- `task_ih05dzesrzu_n_1781644552459_q0vpp6pu5__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `4.35`, sessions `3`
- `task_owbpcay232q0_n_1781582669170_33r41ih05__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `4.5`, sessions `3`
- `task_mdikk1gtyd2_n_1781983231400_jtfmhmm1q__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `B_close_verify_derivability`, risk `4.7`, sessions `3`
- `task_iw2kthdsrf9_n_1781270306790_qeqmn5y2r__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `8.4`, sessions `4`
- `task_ogrtkp7dmz7_n_1781684912333_uubhq8apt__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `8.4`, sessions `4`
- `task_uxma8v1ewo_n_1781555246021_3cfngm8ce__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `8.2`, sessions `4`
- `task_i9oc3bualpdt_n_1781194988200_9cibwav0i__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `9.95`, sessions `3`
- `task_hlt1v2oseidr_n_1781499374015_4d1avgc01__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `9.75`, sessions `3`
- `task_lhywptsxf6rj_n_1781648186758_kafn22w68__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `C_repair_candidate`, risk `9.6`, sessions `3`
- `task_qehlqyjkuoqy_n_1781640416463_7t94nlq5c__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `10.8`, sessions `4`
- `task_uflzxpdl2ii_n_1781214710280_xc3w85bsi__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `13.6`, sessions `3`
- `task_leq16uslqvlv_n_1781275844925_0cgwctlkf__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `13.35`, sessions `3`
- `task_mkkgy4cmj0dr_n_1781644551453_p2xclptoe__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `13.2`, sessions `3`
- `task_agnnvwbuhxbb_n_1781684922865_jlcx55wg5__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `12.05`, sessions `3`
- `task_k7ngh0g7q71x_n_1781992664263_8h2gytbji__ayush_20260624__worktrial_taskloss_20260707` - `psi-consumer-finance`, `D_high_risk_manual_review`, risk `12.05`, sessions `3`
- `task_a3usg9top92_n_1781728721593_j33115ch8__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `3.1`, sessions `5`
- `task_slp4u3rzfopo_n_1781542500425_w15v33oco__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `2.75`, sessions `3`
- `task_ru0dyrkku4o4_n_1781555298195_4ox33xy0p__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `3.6`, sessions `3`
- `task_qy2onlerz48v_n_1781514016667_k1btarxvl__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `3.65`, sessions `3`
- `task_gzrwcsxqsuy9_n_1781711196603_8tvw9iybb__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `3.55`, sessions `2`
- `task_dqmnq5uggp5m_n_1781591780653_gyd1dmse0__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `A_likely_good_spot_check`, risk `2.15`, sessions `0`
- `task_qyprvzopetcx_n_1781700439060_1pl2xi39e__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `4.1`, sessions `4`
- `task_pmhe0agibuk_n_1781683133219_1h255c71z__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `4.55`, sessions `4`
- `task_qtptxtroymwx_n_1781686270105_09vbd8rnn__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `5.65`, sessions `4`
- `task_tyvkozyuhrbd_n_1781588423223_ywidg30t8__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `6.35`, sessions `4`
- `task_hwru6v23mgqk_n_1781583553803_tvree3bhw__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `6.45`, sessions `4`
- `task_igpndla7ffq_n_1781736164354_kdb59x0wl__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `B_close_verify_derivability`, risk `6.55`, sessions `4`
- `task_wam3eaul71u_n_1781709090122_r7ys8u6oh__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `8.45`, sessions `5`
- `task_acgafactdeh8_n_1781660991705_bq93l51xf__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `8.1`, sessions `5`
- `task_nxpu1iujoqak_n_1781561397798_affnmblok__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `8.9`, sessions `4`
- `task_qzgssm54zwj_n_1781732180252_9d3yq8nyw__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `8.0`, sessions `4`
- `task_xu9xi0nqpgsg_n_1781533907519_ci205f769__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `7.55`, sessions `4`
- `task_igsyzitzfj9j_n_1781541775018_1m7a3i694__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `C_repair_candidate`, risk `7.1`, sessions `4`
- `task_bgsq2ryse7je_n_1781558918928_e04niybuz__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `13.15`, sessions `4`
- `task_ilyr5jkkljrf_n_1781571007260_wxumiflc4__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `10.8`, sessions `4`
- `task_olqncx5cxrq4_n_1781574270429_uhfhk55t2__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `10.8`, sessions `4`
- `task_iuxflcdhcj1y_n_1781704569850_f35noviu1__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `13.15`, sessions `3`
- `task_dq9a2ad6xvfw_n_1781641058767_tkzomw5l4__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `12.9`, sessions `3`
- `task_i3ktag4wf0_n_1781571533334_gmarzvzrj__ayush_20260624__worktrial_taskloss_20260707` - `psi-personal-health`, `D_high_risk_manual_review`, risk `12.85`, sessions `3`
