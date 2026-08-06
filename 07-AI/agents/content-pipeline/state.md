---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-06T18:05:00Z"
current_task: "Generated LinkedIn post #148 -- the media / livestream tech volunteer: the one person in the dark back booth who runs the mics, builds the slides, streams the whole service to Facebook so the homebound and the woman on oxygen never miss a Sunday, then stays back to trim and post the sermon, self-taught with no media team and no producer; AI as the broadcast/media department a big-budget church pays a staff for (turn sermon audio into a searchable transcript, auto-caption the video for the hard-of-hearing and sound-off scrollers, pull short clips with titles from a full-length service, build slides from the pastor's notes, draft the post that ships with the sermon); augments him, the ear stays his, gives back the late Saturday nights and keeps the message reaching past the four walls the week he is worn thin; the gap is resourcing/access, not faith or skill; broadcast/media-operations frame with a reach-beyond-the-walls emotional anchor, distinct from minister-of-music worship production, transportation-ministry mobility continuity, and kitchen-ministry repast care; nice irony that the church's tech person was never handed AI literacy; the plug is in"
runs_completed: 148
items_processed: 273
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
