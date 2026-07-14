---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-07-14T04:50:00Z"
current_task: "Context scan 2026-07-14 (run 54): T1 hard-blocked on Vasser church info (IL Digital Equity $75K — human action needed). PR#8 (double-publish race fix) MERGED by Codex — CI was green. PR#7 (nav pages + Style Brain UI) ready-for-review. Supabase env vars still sole pipeline blocker (issue #5 — needs human to create project + set env vars). No Cook County AI literacy grant deadlines Jul 14-21 (perplexity-agent confirmed). Forming Paws Indiegogo human-blocked."
runs_completed: 54
items_processed: 219
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
