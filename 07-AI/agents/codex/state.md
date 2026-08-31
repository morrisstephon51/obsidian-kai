---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-30T23:59:00Z"
current_task: "Run 247: SHIPPED A FIX (net-new -- prior runs were review-only). Task = identify open issues to fix. Swept open ISSUES account-wide (prior runs fixated on PRs): only 4 exist, and just ONE is an actionable code bug -- psychic-bassoon #21 (self-filed run 234): formatDate/formatShortDate in lib/utils.ts call new Date(dateStr); date-only ISO YYYY-MM-DD parses as UTC midnight so toLocaleDateString rolls back a day for the Central Time (Chicago) audience -- a workshop dated 2026-09-15 renders Sep 14. Confirmed STILL PRESENT on main (repro TZ=America/Chicago -> Sep 14 2026). FIX: added toLocalDate() helper parsing date-only as LOCAL midnight new Date(y,m-1,d); full datetime/zoned strings still flow through new Date() unchanged. VERIFIED patched logic in America/Chicago, America/Los_Angeles, UTC: date-only 2026-09-15 -> Tuesday September 15 2026 in all three; datetime/zoned unchanged. No test runner in repo (no jest/vitest, no CI) -> manual cross-TZ verification; offline tsc unavailable (no node_modules) but change is trivially valid TS. Branched fix/date-only-utc-offbyone, committed, pushed, opened PR #24 (Closes #21). Legit outward action under Operating Rule 5 (full repo autonomy) -- founder own repo, reversible, resolves a filed issue. Merge = founder call. Other 3 open issues non-code (forming-paws #8 legal-docs status, avrg #5 Supabase-setup blocker, skills-git #1 tutorial). Prior: run 246 = jobscout #7-#16 review + is_recent-trio merge-order analysis. [runs 204-246 in .remember/ + prior state.md]."
runs_completed: 247
items_processed: 487
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
