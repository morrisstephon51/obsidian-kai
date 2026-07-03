---
agent: enrollment-funnel
display_name: "Enrollment Funnel"
emoji: "🏥"
role: "BigHeart Enrollment · Health Agent"
status: archived
last_run: "2026-06-21T16:27:00Z"
current_task: null
runs_completed: 19
items_processed: 83
last_error: null
color: "#FF6B6B"
house: "clinic"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent enrollment-funnel`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from enrollment-funnel --topic bigheart --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent enrollment-funnel`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Manages BigHeart Health "My Health My Power" initiative enrollment.
- Tracks church partner outreach and program signups.

## Archived (2026-07-03)
Correction: real code exists at github.com/morrisstephon51/Enrollment_Funnel_Agent (TS + Anthropic client) — an earlier version of this note wrongly said "zero implementation" because that repo was never cloned locally. The repo is real but dormant (no commits since 2026-06-05) and never wired into this persona's actual loop (run-agents.sh never invokes it). This is Track 2 (BigHeart) — lower priority than Track 1, which is why it's staying archived rather than being wired up now.
