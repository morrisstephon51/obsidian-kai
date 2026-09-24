---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-24T07:45:00Z"
current_task: "Run 372 (Enrollment_Funnel_Agent). Shipped a distinct-class, high-severity bug OUTSIDE the farmed csv-normalizer/reporter/classify towers AND distinct from my own #29: the engagement-drop alert (the agent's ONLY human-facing alert) silently gives a FALSE all-clear whenever there is no 4-week baseline. checkEngagementDrop collapsed two realities into the same {dropped:false}: (a) engagement genuinely stable and (b) NO baseline to compare against. (b) is the NORMAL case for the documented manual CSV workflow because upsertPerformance() is DEAD CODE -> CSV metrics never persist to performance_data -> fetchRollingEngagement returns [0,0,0,0] -> alert can NEVER fire, and reporter.ts rendered nothing (client reads as 'engagement is fine'). Shipped PR #31 (refs #30, base=default): checkEngagementDrop now returns hasBaseline; reporter.ts renders 3 states (drop->ALERT banner / stable->quiet / no-baseline->explicit 'Drop detection inactive' note); agent.ts logs the blind spot; test/baseline-visibility.test.ts pins it. SAFE slice: NO schema/data writes. Filed issue #30 for the root-cause persistence gap -- wiring upsertPerformance needs live-schema verification of the CSV postId->content_item_id mapping + onConflict target (CSV postId is a platform post id, NOT a content_items UUID; naive upsert would FK-violate or orphan rows the baseline query never reads) -> owner territory, deliberately not fixed. VERIFIED: npx tsc --noEmit clean (exit 0); new test green; reporter 3-state matrix correct (drop->alert only, stable->quiet, no-baseline->note only, null/no-DB->quiet); e2e CSV smoke still builds reports/bigheart-weekly-2026-06-02.md. PR #31 MERGEABLE, touches ONLY scorer.ts+reporter.ts+agent.ts+test/ -> set-merge-tested vs #29 in BOTH orders (0 conflicts; scorer.ts AUTO-merges since #29 edits computeEngagementScore at top, #31 edits checkEngagementDrop below; combined tsc clean + BOTH tests green). Disjoint from #25/#26/#27. Did NOT touch package.json (dodges #25 test-script add/add); new test runs under #25's test/*.test.ts glob runner. Owner-MERGE remains the SOLE bottleneck (0 merges since R320; now ~31 open MERGEABLE PRs across repos)."
carryover: "CARRYOVER (owner-MERGE still the sole bottleneck; 0 merges since R320; ~31 open MERGEABLE PRs). NEW R372: Enrollment_Funnel_Agent PR #31 (refs #30) -- surface empty engagement baseline instead of false all-clear (checkEngagementDrop returns hasBaseline; reporter 3-state note; agent.ts log; test/baseline-visibility.test.ts). MERGEABLE, base=default, SAFE (no schema/data writes), disjoint from #25/#26/#27/#29, set-merge-clean with #29 both orders. Issue #30 = root-cause: upsertPerformance() dead code -> CSV perf never persists -> empty rolling baseline -> owner must wire CSV postId->content_item_id mapping (live-schema). EF MERGE PLAN: #25 (Sessions comma parse + adds the test/*.test.ts glob runner) FIRST to activate all tests, then #26 (csv trim) + #27 (Meta whole-token) + #29 (engagement-weight unify) + #31 (baseline visibility) -- all MERGEABLE + mutually disjoint, any order. JobScout: PR #61 (salary-cadence regex superset) + #63 (keyword whole-word #62) + #65 (TEKsystems #64) + #67 (scan-prompt parity #66) + #25/#27 -- all MERGEABLE, mutually disjoint; scorer.py fully farmed+superseded, STOP stacking. Community Intake: keystone PR #38 (intent classify, supersedes #14-#36) then PR #40 (web /api/intake email parity #39). agent_I_content: PR #9 (glob test-runner, merge FIRST) + #2/#4/#6/#8 + issues #3/#5/#7."
runs_completed: 372
items_processed: 687
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
