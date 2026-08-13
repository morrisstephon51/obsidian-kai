---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-12T23:40:00Z"
current_task: "Generated LinkedIn post #180 -- the transportation-access / transit-desert ministry, a NEW lane opened deliberately right after the tagline arc closed (#177 Get Connected / digital access, #178 Get Skilled / workforce training, #179 Get into AI / AI literacy itself). Transportation is the quiet barrier beneath nearly every other one the series has named: you cannot reach the job, the clinic, the class, the pantry, or the church if you cannot get there, and south suburban Cook County is a genuine transit desert (little/no rail, thin bus coverage, jobs and hospitals scattered across towns). Returns to the series' QUIET-HELPER mode after the three-post AI-literacy-itself arc -- AI is the patient someone who helps a capable person navigate a maze, not the subject. NEW persona to rotate off the recent run (SNAP mother #173, homeownership woman #174, college father #175, caterer woman #176, teen boy #177, warehouse man #178, elder church mother #179): a WOMAN IN HER FIFTIES, a home health aide / CNA who has spent her whole life being the church's unofficial driver (elders to service, a sister to dialysis, the young mother whose stroller won't fold for the bus). Her car dies -- a transmission she can't afford -- and overnight the woman who moved the whole congregation around can't move herself: missed shifts, cut hours, a mother she can't get to dialysis, a life built on mobility collapsing over one unseen thing. Framed with full dignity, never a deficit (PULSE guard against 'poor people just need to figure out a ride'): one of the most reliable, hardest-working people in that building, dropped onto a map drawn for people with a car that never breaks. Doors, fact-checked current/durable 2026, every one HEDGED + ROUTED, none oversold: (1) Pace Suburban Bus -- Dial-a-Ride/Call-n-Ride + ADA paratransit reaching where the fixed route doesn't, hedged on eligibility/geography; (2) the RTA -- Travel Information Center trip planning + Reduced Fare / Ride Free (Benefit Access) for seniors and people with disabilities, hedged; (3) Medicaid non-emergency medical transportation (NEMT) -- the real, largely-unknown benefit for rides to covered medical appointments, often free, arranged in advance, hedged HARD and routed to 'the number on your Medicaid card / your managed-care plan'; (4) local township dial-a-ride vans, routed to 'your township office' with Rich/Bloom/Thornton Townships as examples only, none ranked; (5) 211/211.org for transportation help, bus passes, car-repair programs; (6) scam warnings weighted for this barrier -- 'pay a processing fee, get a free car' and fake 'government transportation grant' schemes wanting bank info, with the FTC-aligned truth that a real benefit/public program never charges an upfront enrollment fee. AI held in quiet-helper + augment-not-replace mode: reads the paratransit application line by line, explains NEMT in plain words, helps puzzle out the Pace/bus route to her Tuesday client, drafts the township questions -- but does NOT drive, does NOT replace the human, does NOT show up for her clients or hold her mother's hand at dialysis. Core reframe intact: the gap is not that she is less capable -- one family has two cars, a licensed teenager, a train station four blocks away, and someone who handles the forms; the other has a twice-an-hour bus, no rail, and a job that assumed everyone drives. Compliance stated TWICE in-body -- general navigation, NOT an endorsement of any transit agency/program/company, NOT legal/financial/medical advice; AI can be wrong so verify every route, schedule, and eligibility rule with the actual agency; never feed private info (SSN, Medicaid ID, bank) to a public AI tool; 'free car / transportation grant' upfront-fee schemes are scams hunting the people trying hardest. DELIBERATELY did NOT rank one agency/township/program over another or promise anyone a ride or outcome. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland ('the towns the trains forgot'). Ties to Community Intake's routing. The plug is in. --- PRIOR (#179): the AI-literacy-itself ministry, the tagline's THIRD word 'Get into AI' -- the elder church mother in her 60s/70s who believed the future was a room she wasn't invited into; closed the #177-179 arc. PRIOR (#178): the free-workforce-training / apprenticeship ministry, the SECOND word 'Get Skilled' -- the warehouse man whose body was quitting. PRIOR (#177): the digital-access / homework-gap ministry, the FIRST word 'Get Connected' -- the honor-roll teen on a taped-up phone in the church parking lot."
runs_completed: 180
items_processed: 305
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
