---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-07T18:22:00Z"
current_task: "Generated LinkedIn post #154 -- the bereavement / homegoing ministry: the deaconess or church mother who shows up when a family loses somebody and carries them through the homegoing, the repast, the obituary, and the after-death paperwork avalanche grief makes impossible (death certificates -- never just one, Social Security, pension/insurance claims, account closures, the mail nobody has the heart to open); something slips not from her carelessness but because one woman cannot hold a whole estate's notifications, deadlines, and denied-benefit letters for a grieving family alone; AI as the patient after-death navigator a funded family's estate attorney + advisor + funeral concierge already provide (plain-language notification checklist of who to tell and what each needs, translating benefit/insurance letters into next-action language, drafting the obituary from spoken memories, holding every estate deadline so none passes during the grief window); augments her, the presence stays hers, frees her to sit in the silence and stay; the gap is resourcing/access, not our families deserving less care or her being less capable; opens a NEW resource-navigation lane -- grief logistics / death admin -- and bridges the faith-community AND community-resource-navigation missions (ties to Community Intake); distinct from treasurer, secretary, food-pantry, prayer, visitor-followup, media, kitchen, transportation, music, sunday-school, church-mother, scholarship, health/nurse, and benevolence personas; the plug is in"
runs_completed: 154
items_processed: 279
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
