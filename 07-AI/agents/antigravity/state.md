---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-07-12T11:00:00Z"
current_task: "Context scan 2026-07-12 (run 48): T1 hard-blocked — Stef must contact Vasser (church legal name/address/pastor/date) for IL Digital Equity $75K. PR#4 MERGED (Vercel SUCCESS); Supabase env vars sole blocker (issue #5). LinkedIn faith-community post ready. No Cook County AI grant deadlines Jul 12-18. Forming Paws Indiegogo human-blocked."
runs_completed: 48
items_processed: 189
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
