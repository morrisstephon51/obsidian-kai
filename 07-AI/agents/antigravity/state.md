---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-07-19T00:00:00Z"
current_task: "Context scan 2026-07-19 (run 72): T1 critical = Vasser church info still gates $75K IL Digital Equity grant (HUMAN ACTION required). PRs #1/#7/#12 await Stef review. Supabase env vars block Issue#5 content pipeline. 7 LinkedIn posts queued. Grant deadline Aug 3. Forming Paws auth gap (reviewDocument) staged, needs write approval. T2: BigHeart pitch + Indiegogo pending. Gemini quota-fix outstanding."
runs_completed: 72
items_processed: 296
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
