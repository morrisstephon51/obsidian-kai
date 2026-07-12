---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-07-12T09:00:00Z"
current_task: "Scanned 25 repos — 2 open issues found. PR#4 in ai-video-reel-generator was already MERGED (Vercel SUCCESS). Merged PR#2 in skills-introduction-to-git (clearPattern bug fix, clean). Commented on issue #5 noting PR#4 merged; Supabase env vars remain the only blocker."Resource not accessible by integration" because Pages was never enabled. Enabled via gh API (build_type=workflow), re-triggered deploy — site now live at https://morrisstephon51.github.io/forming-paws/ (deployed in 15s). Scanned all active repos; ai-video-reel-generator PR#4 remains DRAFT awaiting Stef review."
runs_completed: 55
items_processed: 173
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
