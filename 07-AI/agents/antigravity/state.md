---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-16T16:41:00Z"
current_task: "Context scan 2026-07-16 (run 61): 3 human blockers persist — (1) Vasser church info blocks IL Digital Equity $75K grant (T1 critical path), (2) Supabase env vars block content pipeline Issue#5 (human setup required), (3) PR#7 awaits Stef review. PRs #8 and #9 now CONFIRMED merged by Codex. PR#1 (psychic-bassoon) has merge conflicts — needs rebase. LinkedIn post (deacon persona) generated and saved, pending human publish. No grant deadlines this week; next relevant Aug 3."
runs_completed: 61
items_processed: 254
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
