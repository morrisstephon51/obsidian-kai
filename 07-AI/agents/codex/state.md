---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-04T07:40:00Z"
current_task: "Run 270: Task = review GitHub repos + fix open issues. Moved to next unverified Track item: independently VERIFIED psychic-bassoon PR #22 (date-only off-by-one) against issue #21. Cloned PR#22 head a41fc91, ran the REAL exported formatDate/formatShortDate from lib/utils.ts on BOTH main (pre-fix fe575d4) and PR head under TZ=America/Chicago, Node v25.6.1. RESULT pre-fix: all 4 date-only inputs roll back exactly one calendar day (Sep15->14, Jul4->3, Aug30->29, and Jan1 2026->Dec31 2025 = a YEAR rollback, strictly worse than reported). Post-fix: all 4 render the correct day. CRITICAL non-tautology check: full-datetime pass-through formatShortDate('2026-08-30T02:00:00Z') renders IDENTICALLY (Aug 29) on both versions -> toLocalDate regex only redirects date-only strings and still respects explicit UTC/zone. npm test on PR head = 5/5 pass (node --test lib/**/*.test.ts). TOPOLOGY CLEAN: base main = repo default branch; gh reports MERGEABLE / mergeStateStatus CLEAN -> merge advances default, no ambiguity (unlike job_scanner #19). Posted evidence+merge rec on PR #22 (issuecomment-5537279157). Did NOT merge (founder authority). PRIOR run 269: Community_intake #2/#6 verified. NEXT: founder merges Community_intake #2 then #6, then psychic-bassoon #22; job_scanner #19 still pending; Enrollment #16/#18/#20 remain unverified. 204-269 in .remember/."
runs_completed: 270
items_processed: 511
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
