---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-24T20:20:00Z"
current_task: "Run 375 (fleet review + cross-repo bug-class sweep). Re-verified LIVE state of all 4 agent repos: 0 merges since ~Sep 12 (JobScout last merge #24 Sep 11; Community #13 Sep 12; EFA #23 Sep 11; agent_I_content #1 Jun 6) -> owner-MERGE remains the SOLE bottleneck (unchanged since R320). Confirmed 100%% issue->PR coverage: every open issue has a covering PR (JobScout: #26->PR27, #30-59->keystone PR61, #62->63, #64->65, #66->67; Community: #14-36->keystone PR38, #39->40; EFA: #28->29, #30->31, #24=infra note; agent_I_content: #3->4, #5->6, #7->8/9). NEW WORK this run: swept the two most-recently-discovered CROSS-CUTTING bug classes across the whole fleet and certified them SIBLING-CLEAN. (1) Web-entrypoint asymmetry (web handler drops CLI terminal side-effect): only Community Intake has a web+CLI split (api/intake.js) -> already filed #39/PR#40; JobScout (vercel.json serves only static public/index.html, no function), EFA (single report->src/agent.ts CLI), agent_I_content (single generate->index.ts) STRUCTURALLY cannot host it. (2) Slash-command prompt drift: only JobScout has a pipeline slash-command (scan.md, covered by #66/#67); EFA has only the generic dd.md, Community + agent_I_content have no .claude/commands dir. => NO new tower PRs warranted; fix queue is complete. Re-confirmed the stall ROOT CAUSE with live data: 10/14 Community open PRs (#17/#19/#21/#25/#27/#29/#31/#33/#35/#37) sit on NON-DEFAULT fix/* stacked bases -> UI-merge is a silent no-op vs production AND all are superseded by keystone #38 => they must be CLOSED not merged; only #15/#23/#38/#40 target default. Both keystones already carry merge-readiness cert comments (#38 Run 364, #61 R374). Updated 2 class memories with the sibling-clean structural rule. No code changed (comment/review only)."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; 0 merges since R320; ~40 open MERGEABLE PRs across 4 repos; EVERY open issue already has a covering PR -> DO NOT ship new tower PRs, help the merge). R375 certified the two newest cross-cutting bug CLASSES sibling-clean across the fleet (web-entrypoint asymmetry: only Community api/intake #39/#40; slash-command drift: only JobScout scan.md #66/#67) -> siblings structurally cannot host them (no api/* HTTP handler / no pipeline .claude/commands). Fix queue is COMPLETE; only lever left is owner executing merges. MERGE PLANS (all MERGEABLE/CLEAN, live 2026-09-24): JobScout (default=claude/clever-cannon-IDh3G): merge keystone #61 -> CLOSE cadence issues #30/#32/#34/#36/#38/#41/#43/#45/#47/#49/#51/#53/#55/#57/#59 + tower PRs #29-#60 as superseded (merge the chain OR #61, never both) -> then merge 4 disjoint PRs #27(#26)/#63(#62)/#65(#64)/#67(#66)/#25; scorer.py fully farmed, STOP stacking. Community Intake (default=claude/quirky-galileo-UGnfz): merge keystone #38 (closes #14-#36) -> CLOSE the 10 NON-DEFAULT stacked siblings #17/#19/#21/#25/#27/#29/#31/#33/#35/#37 (UI-merging them = silent no-op vs production; superseded anyway) + #15/#23 -> merge #40 (web email parity #39). Only #15/#23/#38/#40 target default. EFA (default=claude/keen-noether-VED1j): merge #25 (Sessions comma parse; adds test/*.test.ts glob runner) FIRST, then #26/#27/#29(#28)/#31(refs#30) disjoint; issue #30 (upsertPerformance dead code) + #24 (retire stale main) = owner (need live-schema map / branch admin). agent_I_content (default=claude/eloquent-edison-aF7yG): merge #9 (glob test-runner) FIRST, then #2/#4/#6 (#8 redundant w/ #9); #4 base=fix/enforce-caption-char-limits + #8 base=fix/validate-post-platform are non-default/stacked. NEXT: nothing to build or certify -- fix queue complete, both classes swept, both keystones run-certified; pure owner-MERGE."
runs_completed: 375
items_processed: 690
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
