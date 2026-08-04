---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-08-04T00:53:00Z"
current_task: "Context scan 2026-08-04 (run 120): 5 active priorities. TRACK 1 — OpenClaw Phase 1 LIVE thru Aug 17 (Kairo on Phase 2 Week 1: AGENTS.md + MESSAGE-BUS-SCHEMA live); Plug AI execution deferred to 2026-10-13 (IL Digital Equity $75K lapsing by choice — stop flagging). TRACK 2 — Forming Paws now has TWO Codex PRs open awaiting review: #13 (XSS + value fix) and #14 (upload redirect to 302 /dogs/:id); issues #6/#8 blocked on Stef (Supabase + legal filing); ai-video-reel-generator #5 blocked on Supabase. BigHeart LinkedIn post ready (faith-community angle). GRANTS — Cook County Digital Equity IMPACT Small Grants open; Justice Advisory Council due today Aug 3."
runs_completed: 120
items_processed: 540
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
