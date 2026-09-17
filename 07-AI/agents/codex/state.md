---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-17T16:30:00Z"
current_task: "Run 336 (review GitHub repos / fix open issues). Found next same-class sibling in -Community_intake_Routing: motivational phrase `support the community` misroutes faith leaders, social workers, educators who describe their learning goal/role (same class as `help out` #26, `give back` #28). Filed issue #30, created fix/volunteer-support-community-context (base=fix/volunteer-give-back-context, stacked on PR#29), opened PR #31. 86/86 tests pass."
runs_completed: 336
items_processed: 615
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
