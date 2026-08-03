---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-02T21:11:00Z"
current_task: "Run 130: Fixed forming-paws upload redirect bug. Both /api/upload/photo and /api/upload/health-doc returned JSON on success — browser showed raw JSON instead of returning to the dog page. Changed to NextResponse.redirect back to /dogs/:id. Branch fix/upload-redirect pushed, PR #14 open against main. Issues #6/#8 still blocked on Stef (Supabase SQL + legal filing). ai-video-reel-generator #5 still blocked (Supabase setup)."
runs_completed: 130
items_processed: 340
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
