---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-13T16:15:00Z"
current_task: "Generated LinkedIn post #183 -- the reentry / criminal-record sealing & expungement ministry, a NEW lane opened as an UPSTREAM door BENEATH the workforce/Get-Skilled lane (#178) and the housing lanes, the way #182 (health coverage) sat beneath medical-bills (#08-10). One of the most classic and biblical church ministries -- the returning citizen, the second chance, refusing to define a person by their worst day -- never touched before. Barrier: a decades-old record the person assumes is a permanent life sentence with no bars, because nobody ever told them Illinois lets a great many records be SEALED or EXPUNGED, that there is FREE legal help, and that the door they think is welded shut may open. NEW persona rotated off the recent run (SNAP mother #173 ... barber 58 #182): a WOMAN IN HER EARLY FORTIES (41), the most dependable person in her church (runs the Sunday kitchen and hospitality, first car in the lot, last one out), home and clean and steady at one job 10+ years, who caught a nonviolent case in a hard much-younger season (early 20s) and spent 20 years becoming a completely different person -- but the record from who she was at 21 keeps surfacing on background checks and quietly blocks the promotion, the better job, the apartment, even clearance to volunteer with her own church youth group. Dignity, never a deficit (PULSE guard against she should have thought about that before): she already did everything the system asked, then 15 more years of being one of the best people in any room, and she carries a mark the woman across town who did the same reckless things young never got because that woman got a warning and a ride home instead of a case number. Doors, durable/hedged/routed, none ranked: (1) FREE legal aid -- Illinois Legal Aid Online + free expungement/sealing help desks/clinics; (2) a records/reentry org, Cabrini Green Legal Aid and Safer Foundation named as EXAMPLES only, hedged; (3) the real court process (Circuit Court Clerk + state), routed to the court and a legal-aid lawyer; (4) eligibility myth-buster -- MANY IL records are eligible and people never check, hedged HARD (only a lawyer/court can say); (5) request your own record first; (6) 211/211.org; (7) scam warning -- outfits charging big up-front fees promising to erase your record overnight or guarantee it gone, cold-callers wanting a fee + SSN; FTC-aligned truth that real records help is often FREE/low-cost, no one can guarantee a court outcome, the real process runs through the court and a real lawyer. AI held in quiet-helper + augment-not-replace: explains expungement/sealing/eligible/petition in plain words, ballparks what MIGHT be worth asking a lawyer, finds the nearest free help desk, drafts the questions, helps her request her own record -- but does NOT give legal advice, does NOT say what is eligible (a lawyer/court does), does NOT file, does NOT replace the attorney, and must NEVER be fed her full record, case numbers, or SSN. Core reframe: the woman across town did the same reckless things and got a warning + a clean screen ever since; one got a case number that follows her onto every application, the other got a second chance handed to her so quietly she does not know she got one -- not less changed, differently policed and resourced. Compliance TWICE in-body -- general navigation, NOT an endorsement of any org/attorney/program, NOT legal advice; AI can be confidently wrong so verify every eligibility rule/form/deadline/outcome with a real legal-aid attorney or the court; never feed a full record, case numbers, or SSN to a public AI tool; big up-front fees or guaranteed clearances are red flags. DELIBERATELY did NOT rank any org/attorney/program or promise a record can be cleared or any outcome. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intake routing, sits UPSTREAM of the jobs/Get-Skilled lane (#178) and housing. PRIOR (#182): health-coverage/insurance-enrollment -- the self-employed barber 58 never insured. PRIOR (#181): adult-education/GED -- facilities-lead man late-30s. PRIOR (#180): transportation -- home-health-aide woman. The plug is in."
runs_completed: 183
items_processed: 308
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
