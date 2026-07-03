---
agent: community-intake
display_name: "Community Intake"
emoji: "🤝"
role: "Community Intake · Cook County"
status: archived
last_run: "2026-06-21T16:28:00Z"
current_task: null
runs_completed: 11
items_processed: 47
last_error: null
color: "#A855F7"
house: "community-center"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent community-intake`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from community-intake --topic community --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent community-intake`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Routes community members to appropriate resources and programs.
- Serves south suburban Cook County, Chicago area populations.
- Core to The Plug AI mission.

## Archived (2026-07-03)
Correction: real code exists at github.com/morrisstephon51/-Community_intake_Routing (JS, intake.js) — an earlier version of this note wrongly said "zero implementation" because that repo was never cloned locally. The repo is real but dormant (no commits since 2026-06-04) and never wired into this persona's actual loop (run-agents.sh never invokes it). Same category content-pipeline was in before its logic got ported into psychic-bassoon — do that same treatment here before re-activating.
