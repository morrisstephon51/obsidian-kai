---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-07-14T12:30:00Z"
current_task: "Context scan 2026-07-14 (run 55): Three human blockers gate all forward motion — (1) Vasser church legal name/address/pastor/workshop date blocks IL Digital Equity $75K grant, (2) Supabase env vars block content pipeline (issue #5), (3) PR#7 nav+StyleBrain UI awaits Stef review. PR#8 MERGED (CI green). 2 LinkedIn posts queued for manual publish. No Cook County AI literacy grant deadlines Jul 14-21 confirmed. Forming Paws Indiegogo still pending."
runs_completed: 55
items_processed: 224
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
