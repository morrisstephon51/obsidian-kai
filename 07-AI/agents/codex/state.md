---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-26T18:55:00Z"
current_task: "Run 386 (keystone superset PROVEN BY EXECUTION). R385 upgraded JobScout from count-parity to code-inspection parity; this run did the largest un-inspected queue (Community Intake 13i/14pr) and went further than inspection: checked out ALL 12 superseded sibling branches' own test files and RAN them against keystone #38's intake.js + api/intake.js in a fresh clone -- because Section 2 of the runbook CLOSES 12 PRs, which is lossy if #38 is not really a superset. RESULT: #15 48/48, #17 56/56, #19 62/62, #21 70/70, #35 78/78 clean; #25/#27/#29/#31/#33/#37 pass but for one inherited case; #23 = 50/52. THE ONE DIVERGENCE IS THE KEYSTONE BEING CORRECT: the failing line is the ALREADY-MERGED #3 assertion (default branch test/classify.test.mjs:28-29, 'I want to teach and mentor students' -> volunteer) which PR #23 INVERTED in place to 'learner' and relabeled an intentional #22 false-negative, because its token-deletion fix could not satisfy it. Measured: #23 sends 'I want to mentor first-gen students on AI tools' to learner@0.5 -- it silently DROPS genuine volunteers who offer to teach/mentor, the exact population The Plug AI wants in the volunteer inbox; #38 gets every row right via seek-vs-offer direction logic. So merging #23 (or the 6 PRs stacked on it) would be HARMFUL, and the runbook's 'close 12 + merge #38' plan is confirmed correct and now execution-proven. #38's own suite 94/94 unit + 3/3 smoke; CLI intake.js and serverless api/intake.js agreed on every probe -> no twin drift. Shipped: evidence comment on PR #38 + a 'do not merge' evidence comment on PR #23, R386 precision note + section in MERGE-RUNBOOK-2026-09-24.md, and a self-documenting comment block in merge-fleet.sh's community close loop (bash -n clean, plan byte-identical). Also wrote a fleetwide closing-keyword coverage audit (every open issue x every open PR BODY -- titles do NOT auto-close): JobScout 4 auto/15 keyword-less, Community 4 auto/9, EFA 1 auto, avrg 3 auto, content 3 auto/0 -> merge-fleet.sh's Community hand-close set correctly includes 14/16/18 (their PRs #15/#17/#19 get CLOSED not merged, so those keywords never fire). avrg's '#27+#31 auto-close' claim re-verified TRUE (#27 body carries Fixes #26 AND an appended 'Also closes #28', and its diff really does drop the ADMIN_SECRET guard from persona DELETE -> #28 is a covered duplicate, not an orphan). Full 23-repo sweep: ZERO drift vs R385. merge-fleet.sh dry-run still 21 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. No new PR manufactured -- queue fully covered."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; ~15 days, 0 merges since Sep 11-12 across all 5 agent repos + Section-6). R386 raised the bar again: keystone supersession is now EXECUTION-proven for BOTH towers (JobScout #61 via the chain's own tests in R357; Community #38 via all 12 sibling suites in R386). CRITICAL NEW FACT: a tower sibling can INVERT an already-merged assertion to fit its blunt fix, so running the tower's own tests against a keystone can report a FALSE keystone regression -- Community #38 reads 50/52 vs #23 and that is #38 WINNING. Never merge Community #23 (nor #25/#27/#29/#31/#33/#37 stacked on it): they drop genuine volunteers. Diff every failing assertion against the DEFAULT branch before calling regression. DO NOT ship new tower PRs -- every open issue fleetwide has a covering MERGEABLE PR (verified by code inspection for JobScout R385 and by execution for Community R386); only orphans left are genuinely owner-only. The runbook is BOTH prose (MERGE-RUNBOOK-2026-09-24.md) AND a one-command executable (merge-fleet.sh, same codex dir): Stef runs `./merge-fleet.sh` (dry-run, safe) then `./merge-fleet.sh --execute` to clear the ENTIRE fleet queue in one shot -- self-verifies (auto-skips drafts + non-mergeables), keystone hand-closes, retargets content #4. Verified net effect: 21 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. The 4 draft PRs (psychic #25, Link-inbio #5, kai-vault #2+#3) stay OWNER-ONLY until Stef clicks Mark ready for review; the script skips them by design. Merge order unchanged (JobScout #61 keystone->#63/#25/#27/#65/#67 + hand-close 15 tower issues 30-59; Community #38 keystone->CLOSE 12 siblings->hand-close issues 14-36->merge #40; EFA #25 first->#26/#27/#29/#31; content #2->retarget+merge #4->#6->#9->close #8; avrg #27+#31 auto-close incl. the #28 duplicate). Owner-only remainders: EFA #30 schema-persist/#24 retire main, avrg #5 Supabase, forming-paws #8 (IL-SOS filing), + the 4 Section-6 drafts. NON-actionable (do NOT re-flag): skills-introduction-to-git #1 (course bot), ----Workspace-notes PR #1 (owner draft). NEXT: nothing to build -- each loop re-run the per-repo sweep of ALL non-archived repos + merge-fleet.sh dry-run; the remaining un-execution-verified queues are EFA (3i/5pr, #25 test-glob runner is the load-bearing one) and agent_I_content (3i/5pr, #4/#8 stacked on non-default bases) -- run their tests in a fresh clone next."
runs_completed: 386
items_processed: 744
last_error: null
color: "#00FF88"
house: "dev-lab"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent codex`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from codex --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent codex`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Codex is a per-task coding agent. Runs, does work, and exits.
- Reports into clawd via the shared bus on task completion.
