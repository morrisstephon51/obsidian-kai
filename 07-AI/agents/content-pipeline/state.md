---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-07T02:06:00Z"
current_task: "Generated LinkedIn post #150 -- the church secretary / administrative clerk: the woman who is the reason anything runs on time, types the bulletin every Saturday night, keeps the calendar so rehearsals/meetings/repasts don't collide, answers every call, writes the sympathy and welcome letters, and updates the roll -- all by hand on a desktop from 2009, always a little behind not because she's slow but because she retypes from scratch what she already typed last week; AI as the administrative-operations software a big-budget church runs the front office on (regenerate the bulletin from last week's in minutes, draft letters in her own words, turn scribbled announcements into a clean insert, de-conflict the calendar); augments her, the judgment/knowing stays hers, takes the retyping off her desk; the gap is resourcing/access, not competence or care; administrative-operations frame with a Saturday-night-retyping emotional anchor, distinct from treasurer financial stewardship, prayer-ministry member care, visitor-followup CRM, media-ministry broadcast ops, and kitchen/transportation single-event logistics; the plug is in"
runs_completed: 150
items_processed: 275
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
