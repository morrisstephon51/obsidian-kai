---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-07-10T21:30:00Z"
current_task: "Scanned context.md + world.md + bus (6 msgs) — T1 hard-blocked: Vasser church info still missing (legal name, address, pastor confirm, workshop date) for IL Digital Equity $75K grant; mundi-agent-dashboard 3 lint fixes pending (codex re-authorized to commit+push); LinkedIn faith-community post ready to review/publish; no Cook County AI literacy grant deadlines July 10-16; Forming Paws Indiegogo not yet launched; Gemini quota fix needs human action"
runs_completed: 40
items_processed: 154
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
