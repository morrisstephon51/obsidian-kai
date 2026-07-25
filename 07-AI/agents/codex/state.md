---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-07-25T12:30:00Z"
current_task: "Synced local fix/live-dogs-from-supabase branch (was 2 commits behind origin). Pulled migration 003 (RLS public-read on dogs) + openChat null-guard fix. PR #7 confirmed complete: 3 SQL migrations + Supabase fetch in app.js, all ready to apply. Stef blocker: run migrations 001-003 in Supabase SQL editor for project wyzcnkdonbdykidmcxvx then merge PR #7 to close issue #6. No new issues on other repos."
runs_completed: 109
items_processed: 286
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
