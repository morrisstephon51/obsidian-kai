---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-07T06:11:00Z"
current_task: "Generated LinkedIn post #151 -- the scholarship / education-committee volunteer: the retired schoolteacher who every spring gets the congregation's graduating seniors through FAFSA, scholarship applications, college essays, and recommendation letters by hand, out of a shoebox of deadlines and on the only screen she has, her phone; every year one kid slips, not from carelessness but because one person cannot hold twenty kids and forty deadlines and a shifting FAFSA at once; AI as the college-access system funded high schools and $2K private consultants already run on (scholarship matching from a kid's story, first-pass essay feedback so she coaches substance not commas, a plain-language FAFSA walkthrough for nervous parents, deadline tracking so none slips); augments her, the knowing stays hers, frees her to believe in them out loud; the gap is resourcing/access, not the kids' readiness or her competence; deliberately bridges BOTH in-scope missions -- faith community AND first-gen students; distinct from treasurer, church secretary, food pantry, prayer, visitor-followup, media, and kitchen personas; the plug is in"
runs_completed: 151
items_processed: 276
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
