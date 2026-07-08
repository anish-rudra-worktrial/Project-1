# Project One Workflow Walkthrough

This note is a short walkthrough of the Project One workflow and how the scripts fit together. The goal was not just to review tasks one by one, but to build a repeatable way to decide which tasks are worth recovering and what kind of work each task needs.

The dataset contains consumer finance and health tasks that did not make it into delivery. A failed or undelivered task can have several different causes. The prompt might be unclear. The verifier might check a value that is not visible to the agent. The model might complete part of the task but miss one side effect. The environment might also get in the way. Treating all of those as the same kind of failure would make the review slower and less useful.

The workflow separates those cases into three passes.

## 1. Static Task Triage

The first script is `triage_dataset.py`.

This pass looks at the task and verifier before looking at any model trace. It checks for things that usually make a task harder to deliver cleanly:

- too many apps or systems involved;
- relative dates that can be interpreted more than one way;
- finance or health actions with high side-effect risk;
- prompt steps that are not clearly covered by the verifier;
- verifier values that appear only in the verifier, not in the prompt;
- missing or thin session coverage.

The output is a ranked recovery queue, not a final judgment. The most useful file from this pass is `reports/task_recovery_ranked.csv`.

That queue puts each task into one of four buckets:

| Bucket | Meaning |
| --- | --- |
| `A_likely_good_spot_check` | Low static risk. These are the best first candidates for promotion after a human spot check. |
| `B_close_verify_derivability` | Probably recoverable, but the verifier needs proof that its constants are visible or derivable from the seed world. |
| `C_repair_candidate` | Worth saving, but needs prompt, verifier, or seed data repair first. |
| `D_high_risk_manual_review` | Too risky to promote from static signals alone. These need deeper manual review before repair time is spent. |

This gives the reviewer a practical starting order instead of a flat list of tasks.

## 2. Verifier Constant Review

The second script is `constant_derivability_worklist.py`.

This pass focuses on a common verifier problem: hidden constants. A verifier may check for an exact dollar amount, date, phone number, email, name, invoice number, or status value. That can be correct if the agent can find the same value in the environment. It becomes a problem when the value only exists inside the verifier.

The script pulls those constants into a worklist so a reviewer can prove them against the seed world. The key output is `reports/derivability_worklist.csv`.

This review is intentionally conservative. A constant appearing in the worklist does not mean the task is bad. It means the task needs proof. The question is:

Can the agent uniquely derive this value from the prompt and the environment?

If the answer is yes, the task may still be deliverable. If the answer is no, the verifier or seed data needs repair.

## 3. Completed-Run Trace Review

The third script is `post_run_verifier.py`.

This pass happens after model runs already exist. It does not create Fleet runs or submit model responses. It reads completed-run evidence, either from `trace_evidence.md` or from downloaded session transcripts, and classifies what happened in the run.

The trace review is important because static risk is only one side of the story. Some tasks look risky but pass cleanly. Some tasks look simple but fail because the model misses a side effect or the environment blocks a required action.

The post-run layer separates completed sessions into categories like:

- `PASS_CLEAN`
- `PASS_BUT_STATIC_RISK`
- `NARROW_VERIFIER_FAILURE`
- `PARTIAL_COMPLETION`
- `ENVIRONMENT_OR_NAVIGATION_FAILURE`
- `TASK_OR_SEED_AMBIGUITY`
- `BROAD_SIDE_EFFECT_FAILURE`

For this handoff, the trace sample includes 20 completed sessions, with 5 traces from each static bucket. That gives concrete examples for why each bucket exists and helps calibrate the static review against real behavior.

## How The Pieces Fit Together

The three scripts answer three different questions:

| Script | Question |
| --- | --- |
| `triage_dataset.py` | Where should review time go first? |
| `constant_derivability_worklist.py` | Which verifier facts need proof from the seed world? |
| `post_run_verifier.py` | What actually happened when a model attempted the task? |

Together, they turn the dataset into an auditable recovery process. The static layer creates the queue. The constant layer shows what needs seed-world proof. The trace layer checks whether real runs support the static assessment or reveal a different failure mode.

## What This Helps With

This workflow is meant to make task QA faster without hiding the decision-making.

Operators can start with the most recoverable tasks instead of reading the full dataset in arbitrary order. Engineers can see whether failures are coming from verifier design, environment behavior, or model execution. Task writers can focus repairs on specific issues instead of rewriting tasks from scratch.

The main idea is simple: recover good tasks, repair close tasks, and avoid spending time on tasks where the failure is too broad or too ambiguous.

## Limits

The scripts do not replace human review. They organize it.

The first two passes are static, so they cannot prove the seed world by themselves. The third pass depends on completed traces being available. The strongest next improvement would be to connect the verifier-constant worklist directly to seed data checks, so each verifier-only constant can be labeled as derivable, ambiguous, or not derivable.
