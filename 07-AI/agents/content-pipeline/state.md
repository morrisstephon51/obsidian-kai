---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-06T13:55:00Z"
current_task: "Generated LinkedIn post #146 -- the transportation ministry / church van driver: the volunteer who gets the elderly and carless to church every Sunday, running the whole pickup route from memory with no dispatcher, no logistics software, no team; AI as the fleet-and-logistics help a big-budget church pays a department for (turn a name-and-address list into an efficient pickup order, one night-before text to all riders instead of fourteen calls, log rider needs like front-seat/walker/no-porch-rail so they live outside his memory, plan the second run while finishing the first, leave a driveable route for the Sunday he is sick); augments him, the knowing stays his, gives back the early mornings and makes sure Sister Ruthie still gets picked up the day he cannot drive; the gap is resourcing, not faith or skill; continuity/resilience emotional anchor, distinct from kitchen-ministry repast care; bridges Track 1 faith AI literacy with a logistics/mobility-access frame; the plug is in"
runs_completed: 146
items_processed: 271
last_error: null
color: "#9B59B6"
house: "studio"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent content-pipeline`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from content-pipeline --topic content --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent content-pipeline`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Handles video, flyers, social content, training materials for The Plug AI and BigHeart.
- Stack: Next.js, Supabase, Remotion, FAL, Pexels, Vercel, Composio.
- Live at: content-machine-wine.vercel.app
