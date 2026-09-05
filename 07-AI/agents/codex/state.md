---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-04T20:05:00Z"
current_task: "Run 274: Task = review GitHub repos + fix open issues. Independently VERIFIED Enrollment_Funnel_Agent PR #20 (issue #19, half-open week windows — stop boundary-Monday double-count). Cloned fix/week-window-boundary-double-count; imported the REAL date logic (agent.ts: weekStart=new Date(week+'T00:00:00'); weekEnd=addDays(weekStart,7) via setDate) + REAL weekBoundaries construction (supabase.ts:109-118). NON-TAUTOLOGY runtime differential across a DST spring-forward pair: proved weekEnd(N).ISO===weekStart(N+1).ISO (2025-03-10T05:00Z) — setDate advanced 7 CALENDAR days across the 23h Sunday, so the shared Monday-00:00-local boundary the fix relies on is exact. Impact1 (fetchWeekContent): boundary post OLD .lte in BOTH week N & N+1 (double-count) -> NEW .lt in N+1 ONLY. Impact2 (fetchRollingEngagement): confirmed rangeEnd===weekStart; current-week boundary post OLD .lte passesRange=true binnedIdx=0 (INFLATES 4wk baseline, can suppress a real engagement-drop alert) -> NEW .lt excluded (idx-1). NOTED findIndex short-circuits so internal-boundary double-bin cannot happen; the material leak the fix closes is the current-week post entering baseline via .lte(rangeEnd). Diff isolated to src/lib/supabase.ts ONLY (3 predicates .lte->.lt / <=-> < + comments), NO scope-creep. npm ci && npx tsc --noEmit CLEAN. gh MERGEABLE/CLEAN. Posted evidence on PR #20 (issuecomment-5547872437). Did NOT merge (founder authority). PRIOR: run 273 Enrollment #18(verified); run 272 job_scanner #19 (+flagged 4 .claude scope-creep); run 271 Enrollment #16; run 270 psychic-bassoon #22; run 269 Community_intake #2/#6. STILL OPEN needing founder merge: Community_intake #2 then #6 (+new issue #3, no PR yet); psychic-bassoon #22; Enrollment #16, #18(verified), #20(verified); job_scanner #19 (optionally drop .claude). UNVERIFIED: Enrollment #14 (csv substring); job_scanner #14/#15/#16; Community_intake #3. 204-273 in .remember/."
runs_completed: 274
items_processed: 515
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
