---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-07T10:20:00Z"
current_task: "Generated LinkedIn post #152 -- the health ministry / nurse's ministry: the retired RN who runs the after-service blood-pressure table, holds the whole congregation's diagnoses, medications, appointments, and sick-and-shut-in list in her head, and notices the slow decline before the clinic does; one slips through not from her missing it but because one woman cannot hold sixty people's numbers, refills, follow-ups, and rides from memory on a Sunday; AI as the population-health / care-coordination software funded clinics already run on (plain-language discharge translation, holding the sick-and-shut-in list with appointment + refill dates, ride/referral coordination, pattern-spotting the slow decline across weeks); augments her, the trust stays hers, frees her to lay a hand on somebody and mean it; the gap is resourcing/access, not our people being sicker or her being any less of a nurse; deliberately bridges the faith-community AND community-health-worker missions (also ties to BigHeart My Health My Power); distinct from treasurer, secretary, food pantry, prayer, visitor-followup, media, kitchen, transportation, music, sunday-school, church-mother, and scholarship personas; the plug is in"
runs_completed: 152
items_processed: 277
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
