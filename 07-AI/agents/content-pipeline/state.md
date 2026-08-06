---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-06T09:50:00Z"
current_task: "Generated LinkedIn post #145 -- the kitchen / culinary ministry: the woman who feeds the whole church out of a small kitchen (repast, revival, anniversary, Sunday fellowship), scaling by feel and coordinating who-brings-what with no staff and no budget; AI as the catering-and-event help a big-budget church pays a team for (scale her own recipe to a large count with grocery list and rough cost, build a who-is-bringing-what sheet, generate a cooking/serving timeline so food is hot at once, draft the sympathy-and-coordination text to a grieving family in her voice, one message to the whole crew); augments her, the recipes and hands and love stay hers, gives back the hours and makes sure the grieving family gets fed without her carrying every number alone at midnight; the gap is resourcing, not care or skill; funeral-repast emotional anchor, distinct from church-mother prayer-list care; bridges Track 1 faith AI literacy with a hospitality/culinary-ministry frame; the plug is in"
runs_completed: 145
items_processed: 270
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
