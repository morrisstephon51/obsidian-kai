---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-27T03:35:00Z"
current_task: "Run 388 (agent_I_content — the LAST un-executed queue — run in a fresh clone with a real npm install; found TWO distinct failures, one in the runbook and one in the guards). FINDING 1, THE RUNBOOK DID NOT MERGE AS WRITTEN: order #2->#4->#6 is clean but #9 then hits CONFLICT (content) in package.json. Default has NO \"test\" key and #2/#4/#8/#9 each ADD it with a DIVERGENT value, so the SET conflicts while every PR still reads MERGEABLE against its own base (#4 absorbs #2's line only because it is stacked on #2's branch). This is the BROKEN twin of EFA #25/#27, which add byte-identical lines and merge silently. THE CASCADE WAS THE REAL HAZARD: merge_ready would have SKIPPED a conflicting #9, but the next line closed #8 unconditionally -> #9 skipped -> package.json keeps #4's enumerated line -> #8 closed as \"superseded\" -> platform-validation.test.ts lands on default WITH NO RUNNER AT ALL and the suite stays green on the two files it still knows about. The exact bug class the section exists to fix, caused by the runbook. Patched merge-fleet.sh: new resolve_test_line_conflict (merges base into the PR branch, keeps the glob line, pushes, flips #9 back to MERGEABLE; aborts unless package.json is the ONLY conflict; asserts the resolved value before committing) + #8's closure now GATED on #9 reaching MERGED, else [HOLD]. Resolver gotcha worth keeping: merging the base INTO the PR branch INVERTS which side is \"ours\" vs the obvious local test — my first cut silently kept the enumerated line and only the post-resolve assert caught it. FINDING 2, NEW GUARD CLASS — THE UNWIRED HELPER (PR #10 shipped): mutation-tested all three existing guards per the R387 rule and all three are REAL (each goes red on bug re-injection AND red against default; each imports the real module — no tautology). But all three test the exported helper IN ISOLATION. Replacing the three call sites with arity/type-identical no-ops — helpers left defined, exported, byte-identical — gives a CLEAN tsc --noEmit and caption-limit 7/7 green, hashtag-filter 9/9 green, platform-validation 8/8 green, while every user-visible symptom returns (over-limit captions persisted, #fyp/#viral in text_outputs, durationInFrames dropped from video_outputs). Not hypothetical: issue #3 WAS itself a wiring bug (topicWords computed in generateContent, never used) — the fix rebuilt the helper and reproduced the same blind spot in its coverage. Shipped PR #10 (agents/content-pipeline/pipeline-wiring.test.ts, 6 tests) off DEFAULT: drives the REAL entrypoints through injected fakes (stub Anthropic client; monkeypatched createClient — module is commonjs so mutating the cached export binds the fake) and asserts on OUTPUT, so it stays agnostic about which helper does the work. One test reproduces #5's exact mechanism rather than a proxy: JSON.parse(JSON.stringify(payload)) then assert durationInFrames is still a number. Triple-verified: PASSES on the merged tree (4/4 files, 30/30 assertions), FAILS 6/6 on default with genuine assertion failures (not import errors), FAILS 6/6 on the unhooked tree the other three call green. No package.json change -> no add/add conflict, #9's glob auto-wires it. Also shipped: execution-audit comment on #9, R388 addendum in MERGE-RUNBOOK-2026-09-24.md, merge-fleet.sh patched (bash -n clean; dry-run re-verified 23 merges / 14 PR-closes / 1 retarget / 27 issue-closes / 4 draft-skips — +1 merge vs R387 for #10, ALL other counts unchanged). Merge order now 2 -> 4 -> 6 -> [resolve] -> 9 -> close 8 -> 10 LAST. ALL FIVE agent queues are now execution-proven. Full 23-repo sweep: zero drift vs R387 beyond the two PRs R387/R388 themselves added."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; ~15 days, 0 merges since Sep 11-12). NEW RULE from R388 — MUTATION-TESTING THE HELPER IS NECESSARY BUT NOT SUFFICIENT. R387 taught: run a guard against DEFAULT (must fail) and re-inject the bug (must go red). R388 adds a THIRD mutation the first two miss entirely: UNHOOK THE CALL SITE. Leave the helper defined, exported and byte-identical, replace its call with an arity/type-identical no-op, confirm tsc is clean, then run the suite. If it stays green the fix is only as durable as the next refactor — all 3 agent_I_content guards were individually real and ALL THREE were blind to this. Prefer a guard that drives the real entrypoint through an injected fake and asserts on OUTPUT over one that imports a helper and asserts on its return. SECOND R388 RULE — A SKIPPED MERGE CAN BE WORSE THAN A FAILED ONE. merge-fleet.sh's per-PR safety check turns a conflict into a silent [skip], and any UNCONDITIONAL follow-up action (close the superseded PR, close the issue) then executes against a state that never happened. Every 'X supersedes Y' step must be GATED on X actually reaching MERGED. Audit the script for other unconditional close_pr calls that assume a prior merge landed. STATUS: all 5 agent queues execution-proven — JobScout keystone #61 (R357/R385), Community keystone #38 (R386), EFA + hardened PR #32 (R387), agent_I_content + hardened PR #10 (R388). Never merge Community #23 (nor #25/#27/#29/#31/#33/#37 stacked on it): they drop genuine volunteers. DO NOT ship new tower PRs — every open issue fleetwide has a covering MERGEABLE PR. Runbook is BOTH prose (MERGE-RUNBOOK-2026-09-24.md) AND executable (merge-fleet.sh): Stef runs `./merge-fleet.sh` (dry-run, safe) then `./merge-fleet.sh --execute`. Net effect now 23 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. The 4 draft PRs (psychic #25, Link-inbio #5, kai-vault #2+#3) stay OWNER-ONLY until Stef clicks Mark ready for review; the script skips them by design. EFA order #25->#26->#27->#32->#29->#31. Owner-only remainders: EFA #30 schema-persist/#24 retire main, avrg #5 Supabase, forming-paws #8 (IL-SOS filing), + the 4 Section-6 drafts. NON-actionable (do NOT re-flag): skills-introduction-to-git #1 (course bot), ----Workspace-notes PR #1 (owner draft)."
runs_completed: 388
items_processed: 754
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
