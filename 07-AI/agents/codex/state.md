---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-24T04:00:00Z"
current_task: "Run 371 (Enrollment_Funnel_Agent). Found + shipped a genuinely NEW, distinct-class bug OUTSIDE the farmed csv-normalizer/reporter/classify towers: the weekly engagement formula (likes*1+comments*3+shares*5+saves*2) was hardcoded in TWO executable sites -- scorer.ts computeEngagementScore (per-post scores + current-week total in agent.ts) and supabase.ts fetchRollingEngagement (the 4-week drop-detection BASELINE). checkEngagementDrop compares current-vs-baseline to raise the ONLY human-facing alert ('ENGAGEMENT ALERT: review content strategy immediately'); the two copies agree only by coincidence, so any weight change silently makes the comparison apples-to-oranges (false/missed alert) with zero test coverage. Filed issue #28; shipped PR #29 (closes #28): unify on computeEngagementScore via a new EngagementCounts type (NormalizedRow AND performance_data rows both satisfy it); baseline now aggregates THROUGH the shared fn -> one source of truth, cannot drift. Added test/engagement-parity.test.ts (pins 1/3/5/2 weights, views excluded, baseline==current-week). VERIFIED: npx tsc --noEmit clean (exit 0); parity test green; e2e smoke run on sample CSVs still builds reports/bigheart-weekly-*.md. PR #29 MERGEABLE/CLEAN, base=default (claude/keen-noether-VED1j), touches ONLY scorer.ts+supabase.ts+test/ -> DISJOINT from EF #25/#26/#27 (merge any order); deliberately did NOT touch package.json to dodge #25 test-script add/add conflict. Memory paid off: my first candidate (topUtmSources comma bug in claude-client.ts) was ALREADY fixed by OPEN PR #25 (shared parseSessionCount) -> did NOT duplicate. Noted for owner (NOT fixed, mutates live schema): upsertPerformance() is dead code -> CSV perf never persisted -> rolling baseline may stay empty in a CSV-only workflow, so the drop alert may never fire. Owner-MERGE remains the sole bottleneck (0 merges since R320; ~30 open MERGEABLE PRs across repos)."
carryover: "CARRYOVER (owner-MERGE still the sole bottleneck; 0 merges since R320; ~30 open MERGEABLE PRs). NEW R371: Enrollment_Funnel_Agent issue #28 + PR #29 -- unify weekly engagement weights (scorer.ts computeEngagementScore is now the single source of truth; supabase.ts fetchRollingEngagement baseline aggregates through it). PR #29 MERGEABLE, base=default, touches ONLY scorer.ts+supabase.ts+test/ -> disjoint from EF #25/#26/#27, merge in any order. EF merge plan: #25 (Sessions comma parse, shared parseSessionCount, +test/ glob runner) FIRST, then #26 (csv trim parity) + #27 (Meta whole-token) + NEW #29 (engagement-weight unify) -- all MERGEABLE + mutually disjoint. EF follow-up for owner: upsertPerformance() dead code (CSV perf never persisted -> empty rolling baseline). JobScout: PR #61 (salary-cadence regex superset) + #63 (keyword whole-word #62) + #65 (TEKsystems #64) + #67 (scan-prompt parity #66) + #25/#27 -- all MERGEABLE, mutually disjoint; scorer.py is fully farmed+superseded, stop stacking. Community Intake: keystone PR #38 (intent classify, supersedes #14-#36) then PR #40 (web /api/intake email parity #39). agent_I_content: PR #9 (glob test-runner, merge FIRST) + #2/#4/#6/#8 + issues #3/#5/#7."
runs_completed: 371
items_processed: 686
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
