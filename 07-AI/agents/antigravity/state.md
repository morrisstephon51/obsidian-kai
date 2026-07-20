---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-19T22:00:00Z"
current_task: "Context scan 2026-07-19 (run 74): T1 CRITICAL = Vasser church info (legal name, address, pastor confirm, workshop date) still gates $75K IL Digital Equity grant. HUMAN ACTION required. Deadline Aug 3. PRs #1/#7/#12 await Stef review. Faith-community LinkedIn post generated. No Cook County grant deadlines this week. Forming Paws auth gap CLOSED by Codex (commit 566e5d3). T2: Supabase env vars block Issue#5 content pipeline. BigHeart pitch + Indiegogo pending. Gemini quota-fix outstanding."
runs_completed: 74
items_processed: 308
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
