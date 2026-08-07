---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-07T14:22:00Z"
current_task: "Generated LinkedIn post #153 -- the benevolence / emergency-assistance ministry: the deacon-board volunteer people call when the lights are about to go off, who works the maze of emergency rent help, LIHEAP-style utility assistance, and one-time aid applications by hand, from memory, on a phone; every so often a family falls through not from his carelessness but because one man cannot hold every program, deadline, document, and quietly-emptied fund for a whole congregation in crisis at once; AI as the benefits-navigation / case-management software funded social-service agencies already run on (eligibility matching from a plain-language household description, translating denial letters into next-action language, auto-filling the repetitive parts of applications before the window shuts, holding every family's deadline so none slips); augments him, the trust stays his, frees him to answer the phone at night and mean it; the gap is resourcing/access, not our families being less worthy or him being less capable; deliberately bridges the faith-community AND community-resource-navigation missions (ties to Community Intake); distinct from treasurer, secretary, food pantry, prayer, visitor-followup, media, kitchen, transportation, music, sunday-school, church-mother, scholarship, and health/nurse personas; the plug is in"
runs_completed: 153
items_processed: 278
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
