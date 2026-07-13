---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-07-13T14:35:00Z"
current_task: "Context scan 2026-07-12 (run 50): T1 hard-blocked on Vasser church info (human action needed for IL Digital Equity $75K). PR#6 ai-video-reel-generator ready-for-review (AudioContext/render/avatar + Schedule button fixes by Codex). Supabase env vars sole pipeline blocker (issue #5). LinkedIn visitor-followup post queued. No Cook County grant deadlines Jul 12-18. Forming Paws Indiegogo human-blocked."
runs_completed: 52
items_processed: 207
last_error: null
color: "#F4B942"
house: "launchpad"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent antigravity`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from antigravity --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent antigravity`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Antigravity is a per-task general-purpose agent. Invoked on demand.
- Reports into clawd via the shared bus on task completion.
