---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-06T17:10:00Z"
current_task: "Generated LinkedIn post #147 -- the new-members / visitor follow-up ministry: the greeter who catches every first-time guest, gets the card, calls Tuesday, remembers the name the next Sunday, and keeps people from drifting away, with no assimilation team, no follow-up database, no system; AI as the assimilation operation a big-budget church pays a department for (turn a stack of cards into one follow-up list, draft a warm first text in her own words, track who has been reached vs missed so no double-calls and no cracks, set day-3 and week-2 nudges when people decide whether they belong, note what each guest said so it lives outside her memory); augments her, the noticing stays hers, gives back the Tuesday nights and makes sure the guest who came once still hears from somebody the week she is worn out; the gap is resourcing, not faith or skill; retention/belonging emotional anchor, distinct from transportation-ministry continuity and kitchen-ministry repast care; bridges Track 1 faith AI literacy with an assimilation/CRM frame; the plug is in"
runs_completed: 147
items_processed: 272
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
