---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-07T22:26:00Z"
current_task: "Generated LinkedIn post #155 -- the prison / reentry ministry: the deacon or lay saint who never stopped writing letters to men inside, stands at the gate at six a.m. on release day, then tries single-handedly to walk a returning citizen back into a life the paperwork keeps locking him out of (an ID expired inside with no birth certificate to replace it, benefits terminated the month he went in, the felony box on every application, parole dates that do not forgive a missed bus, an expungement maze nobody explains); something slips not from his carelessness but because one man with a day job and a family cannot hold a whole reentry's documents, deadlines, and denial letters alone -- a stalled ID chain, an unfiled benefit, an expungement never filed so the box gets checked for another ten years; AI as the reentry navigator a funded diversion program's case manager + staff attorney + career counselor already provide (a sequenced order-of-operations for document recovery, translating a benefits-termination letter into next-action language, mapping the expungement path from what a record actually qualifies for, holding every parole date and agency window so none passes); augments him, the showing up stays his, frees him to do the part only he can do, which is believe; the gap is resourcing/access, not our sons deserving fewer second chances or him being less capable; opens a NEW resource-navigation lane -- reentry logistics -- and bridges the faith-community AND community-resource-navigation missions (ties to Community Intake and JobScout's second-chance-employer lane); distinct from treasurer, secretary, food-pantry, prayer, visitor-followup, media, kitchen, transportation, music, sunday-school, church-mother, scholarship, health/nurse, benevolence, and bereavement personas; the plug is in"
runs_completed: 155
items_processed: 280
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
