---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-15T00:10:00Z"
current_task: "Context scan 2026-07-15 (run 58): 3 human blockers unchanged — (1) Vasser church info blocks IL Digital Equity $75K grant, (2) Supabase env vars block content pipeline (Issue #5), (3) PR#7 awaits Stef review. 3 PRs open across repos (PR#1 XSS fix, PR#6 execFileSync hardening, PR#9 analytics schema) — all awaiting merge. LinkedIn post queued (skills-gap=jobs-gap) needs manual publish. No grant deadlines Jul 13-19."
runs_completed: 58
items_processed: 237
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
