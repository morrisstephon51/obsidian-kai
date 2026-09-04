---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-04T19:56:00Z"
current_task: "Run 273: Task = review GitHub repos + fix open issues. Independently VERIFIED Enrollment_Funnel_Agent PR #18 (issue #17, weekly date range off-by-one: display rendered exclusive weekEnd instead of inclusive Sunday, so consecutive weekly reports overlapped by a day). Cloned repo; base main=987f910, pr18 head. NON-TAUTOLOGY runtime differential: imported the REAL buildReport from both main and pr18 via tsx and rendered dateRange for 3 weeks. Confirmed weekStart/weekEnd are LOCAL-midnight (new Date(week+'T00:00:00') / lastMonday()->setHours(0,0,0,0); addDays preserves time-of-day), so fix's weekEnd.getTime()-86400000 is sound. RESULTS: normal wk Mon Jun 2 OLD 'Jun 2 - Jun 9'(overlap bug)->NEW 'Jun 2 - Jun 8' FLIPPED; spring-forward wk (23h Sun Mar 8) OLD Mar 16->NEW Mar 15 correct Sunday; fall-back wk (25h Sun Nov 1) OLD Nov 9->NEW Nov 8 correct Sunday -- proved epoch-ms subtraction is DST-SAFE (my key concern vs the issue's setDate suggestion). Diff isolated to src/lib/reporter.ts +5/-1, NO scope-creep, weekEnd query bound (.lte in supabase.ts) untouched, orthogonal to PR #16/#20. gh MERGEABLE/CLEAN. Posted evidence table on PR #18 (issuecomment-5545777171). Did NOT merge (founder authority). PRIOR: run 272 job_scanner #19 (+flagged 4 .claude scope-creep files); run 271 Enrollment #16; run 270 psychic-bassoon #22; run 269 Community_intake #2/#6. STILL OPEN needing founder merge: Community_intake #2 then #6; psychic-bassoon #22; Enrollment #16, #18(verified), #20; job_scanner #19 (optionally drop .claude). UNVERIFIED: Enrollment #20 (week-window boundary double-count), #14 (csv substring); job_scanner #14/#15/#16. 204-272 in .remember/."
runs_completed: 273
items_processed: 514
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
