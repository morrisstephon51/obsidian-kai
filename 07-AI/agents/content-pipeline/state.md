---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-06T22:05:00Z"
current_task: "Generated LinkedIn post #149 -- the intercessory prayer ministry coordinator: the woman who knows who is sick before the pastor does, keeps the prayer list from slips/texts/hallway whispers, works the phone tree, tracks the Tuesday surgery and the grieving family, and lives with the fear that a name falls through when one person tries to hold a whole church of pain by hand; AI as the member-care system a big-budget church runs on care staff and tracking software (turn a pile of handwritten cards into one clean typed list, remind her which surgery was when and who needs a call by Friday, convert scattered midnight texts into the weekly prayer sheet, catch the request before it gets lost by morning); augments her, the knowing stays hers, gives back the hours and takes the fear that someone slipped through; the gap is resourcing/access, not faith or care; member-care-coordination frame with a name-that-falls-through emotional anchor, distinct from visitor-followup assimilation, the caregiver family medical load, church-mother elder presence, and media-ministry broadcast ops; the plug is in"
runs_completed: 149
items_processed: 274
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
