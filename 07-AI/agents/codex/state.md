---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-07-20T05:37:00Z"
current_task: "Audited forming-paws GitHub repo for open issues. Found redirect bug in upload routes: /api/upload/photo and /api/upload/health-doc return JSON on success but the dog detail page submits via native HTML form POST, causing browser to display raw JSON instead of navigating back. Fix: change success response to NextResponse.redirect to /dogs/${dogId}."
runs_completed: 84
items_processed: 220
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
