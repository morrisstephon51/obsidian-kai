---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-12T19:09:00Z"
current_task: "Generated LinkedIn post #178 -- the free-workforce-training / apprenticeship / credential ministry, deliberately the SECOND word of The Plug AI tagline ('Get Skilled'), picking up exactly where #177 (digital access, the FIRST word 'Get Connected') left off -> the next movement of the tagline arc 'Get Connected. Get Skilled. Get into AI.' Distinct from the earlier employment/jobs lane (that was landing A job now); this is the free ON-RAMP before the better job -- the credential/apprenticeship/skilled trade that changes what a family earns for life, and that our people are quietly certain is 'not for people like us.' NEW persona for series variety: a MAN in his mid-forties, a warehouse/logistics worker in the south-suburban freight corridor whose body is telling him the clock is running out on work that only pays while he can lift -- rotated hard off the recent adult-woman/youth run (SNAP mother #173, homeownership woman #174, college father #175, caterer/entrepreneur #176, teenage boy #177) back to a grown working man. Framed with full dignity as capability meeting a missing on-ramp, never a deficit (PULSE guard against 'he should have gone to school'): one of the most skilled, disciplined people in the building, told at 17 that college was for other kids and who believed it, never handed the map to a free credential that would double his pay without a dollar of debt. Same core Plug AI wall: 'training and school are for people with money and time we don't have.' Doors named, fact-checked current/durable as of 2026, every one HEDGED + ROUTED, none guaranteed: (1) WIOA -- federal, ongoing, funds adult job training via American Job Centers; (2) American Job Centers / CareerOneStop (careeronestop.org, 1-877-US-2JOBS); (3) Registered Apprenticeships (apprenticeship.gov) -- 'earn while you learn,' they PAY you to train, the answer to 'I can't afford to stop working'; (4) community-college workforce certificates (CDL/HVAC/welding/CNA-LPN/phlebotomy/IT) routed to 'your local community college' with real south-suburban anchors as examples (Prairie State College, Chicago Heights; South Suburban College, South Holland), no school ranked over another; (5) Pell/federal aid for training -- mentioned GENERALLY, hedged HARD, care-note that short-term-workforce rules are changing so check what's current, routed via FAFSA/financial-aid office, NO dollar figure or eligibility promise; (6) Illinois workNet (illinoisworknet.com); (7) 211/211.org; (8) scam warnings -- 'pay up front for a guaranteed government job / certified in a weekend / fast diploma' mills, framed with the 'the one working hardest is the one being hunted' motif and the FTC-aligned truth that real WIOA training doesn't charge you and an apprenticeship PAYS you. AI framed as the patient 'person who knows how all this works' a resourced family always had -- finds which free programs he might qualify for, the nearest center, compares apprenticeship vs certificate, makes sense of WIOA intake, never makes a grown man feel slow for going back to a classroom at 45. Augment-not-replace held HARD ('Not to take the class for him. Not to do the trade... The skill is his. The hands are his... It only finds him the door'). Core reframe: the gap is not that our man is less capable -- one worker was handed a counselor, a map, and a family who knew which credential to get; the other a strong back, a time clock, and a soft lie that the classroom closed on him at 17. Compliance stated TWICE in-body -- general navigation, NOT a guarantee of eligibility, NOT an endorsement of any school/program, NOT legal/financial advice. DELIBERATELY did NOT tell anyone they qualify or rank one school/trade/union over another. Routed to: American Job Center via CareerOneStop; apprenticeship.gov; local community college (Prairie State / South Suburban as examples); Illinois workNet; FAFSA/financial-aid office; 211. Ties directly to the tagline's second word and to Community Intake's routing. The plug is in. --- PRIOR (#177): the digital-access / home-internet / homework-gap ministry -- the honor-roll teenager doing homework on a taped-up phone in the church parking lot, the tagline's FIRST word 'Get Connected.' PRIOR (#176): the small-business / entrepreneurship-formalization ministry -- the church caterer who just needed the free EIN and free advisers."
runs_completed: 178
items_processed: 303
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
