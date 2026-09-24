---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-24T12:10:00Z"
current_task: "Run 373 (Community Intake keystone certification). Reviewed all 4 active agent repos (EFA, JobScout, Community Intake, agent_I_content): EVERY open issue already has an open PR; ~40 open PRs all MERGEABLE/CLEAN; 0 merges since R320 -> owner-MERGE confirmed as the SOLE bottleneck, not missing code. JobScout re-confirmed fully farmed (scorer cadence->#61, keyword->#63, location/title done, agency TEKsystems->#65, scan-prompt->#67; no web/api twin, only static public/index.html) -> deliberately did NOT stack a redundant 41st PR. Instead did the highest-leverage non-redundant unit: CERTIFIED keystone Community Intake PR #38 (intent-based classifier) as a proven behavioral SUPERSET of the entire #14-#36 tower by actually RUNNING it in a fresh /tmp clone (Node v25): npm run test:unit 94/94 PASS (exit 0), incl. the explicit #14-#36 tower-supersession block running each issue own example against BOTH classify() copies (intake.js + api/intake.js) + genuine partner/volunteer precision cases; smoke learner/partner/volunteer all exit 0. DISCOVERED a previously-unflagged structural trap likely explaining 0 merges: 10 of the 14 Community classify PRs have NON-DEFAULT base branches (stacked on each other) -- only #15/#23/#38/#40 target default; clicking Merge on #17/#19/#21/#35 (partner chain) or #25/#27/#29/#31/#33/#37 (volunteer chain) lands on an intermediate feature branch, NOT default. Posted a merge-readiness certification comment on PR #38 (issuecomment-5813505547): merge #38 -> close #15/#17/#19/#21/#23/#25/#27/#29/#31/#33/#35/#37 as superseded -> merge #40; collapses 14 PRs -> 2 merges. Comment-only, no code changed."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; 0 merges since R320; ~40 open MERGEABLE PRs across 4 repos; every open issue already has a PR -> STOP shipping new tower PRs, help the merge instead). R373: CERTIFIED Community Intake keystone #38 by running it -- 94/94 unit PASS + tower-supersession block green vs BOTH classify copies + smoke green; posted merge-readiness cert on PR #38. NEW TRAP: 10/14 Community classify PRs have NON-DEFAULT (stacked) bases -- merging via UI does NOT reach default; only #15/#23/#38/#40 target default. MERGE PLANS (all MERGEABLE/CLEAN 2026-09-24): Community Intake: merge #38 (keystone, closes #14-#36) -> CLOSE #15/#17/#19/#21/#23/#25/#27/#29/#31/#33/#35/#37 as superseded -> merge #40 (web email parity #39). JobScout: merge #61 (salary-cadence regex superset of #29-#60) + #63 (keyword whole-word #62) + #65 (TEKsystems #64) + #67 (scan-prompt parity #66) + #27 (recency years-ago #26) + #25 (salary range placeholder); scorer.py fully farmed, STOP stacking. NEXT: certify #61 by running tests/ before recommending the #29-#60 issue closes. EFA: merge #25 (Sessions comma parse + adds test/*.test.ts glob runner) FIRST, then #26/#27/#29/#31 (all MERGEABLE, disjoint). Issue #30 (upsertPerformance dead code) = owner territory (needs live-schema postId->content_item_id mapping). agent_I_content: merge #9 (glob test-runner) FIRST, then #2/#4/#6 (#8 redundant w/ #9); #4 base=#2 branch + #8 base=#6 branch (non-default, stacked)."
runs_completed: 373
items_processed: 688
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
