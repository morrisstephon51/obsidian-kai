---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-18T18:05:00Z"
current_task: "Generated LinkedIn post #210 -- NEW lane: the childcare-assistance / child-care-subsidy ministry. A WOMAN, 29, a single mother of two little ones working full time, watching nearly her whole check disappear into daycare and quietly doing the midnight math on whether quitting would leave her with more -- not knowing that child care assistance helps working parents pay on a sliding scale, that Head Start / Early Head Start and state pre-K exist at no cost, that a child care resource and referral agency and 211 will check her eligibility and help her apply for free, and that she may not have to choose between the job and the kids -- while 'guaranteed childcare grant for a fee' scams, application-fee cons that charge to fill out a free form, phishing that harvests her SSN and her children's Social Security numbers, and fake unlicensed 'cheap daycare' that takes a deposit and vanishes hunt a mother stretched to the last dollar. Doors (hedged, none ranked): check if you qualify for help paying (subsidy on a sliding scale, get eligibility checked, confirm with a referral agency or 211, don't assume too much/too little); free early-childhood programs (Head Start / Early Head Start / state pre-K at no cost); free help to apply (referral agencies, community orgs, 211, no upfront fee); the work side (may not have to choose job vs kids, some employers help); the weight (faith, mentor, family, church, 211, 988). Flat rule: applying is free and runs through the state/county program, no honest party charges an upfront fee to guarantee a childcare grant, and no legitimate program needs her full SSN + her kids' Social Security numbers handed to a stranger to 'check eligibility' -- anyone charging upfront to lock in a grant, guaranteeing it, or harvesting family info is the scam, not the help. Held a SEPARATE caution: a real request for documents (pay stubs, proof of income/work, a redetermination notice) from the actual childcare-assistance office is NOT a scam -- don't ignore genuine paperwork with a real deadline; a missed redetermination can drop the help. AI in quiet-helper mode (explains the words, finds the referral agency / Head Start program / 211 to reach herself, helps her understand documents + what a notice asks, names the scam -- does NOT decide whether she qualifies, act as the caseworker, or promise a subsidy; never fed full SSN / DOB / children's Social Security numbers / private case details). Compliance stated twice in-body; dignity, never deficit (a mother working full time for two kids is the opposite of irresponsible). Rotated gender back to a WOMAN off the #209 man 34; centers a YOUNG WORKING SINGLE MOTHER (29). Deliberately distinct from SNAP/food (#208), health-coverage enrollment (#206), and the job loss (#201 -- she still HAS the job, which is the whole tension) -- this is the COST OF CARE between a mother and the job that pays for her kids and the free help to lower it. Saved to output/linkedin-2026-08-18-childcare-assistance-subsidy-ccap-scam-ministry.md. PRIOR (#209): reentry / criminal-record expungement + sealing -- a father rebuilding after incarceration, kept behind an old record, man 34. PRIOR (#208): food assistance / SNAP + EBT benefit-theft -- grandmother skipping meals so her grandkids eat, woman 64. PRIOR (#207): workers' compensation / workplace injury -- mid-life manual laborer hurt on the job and afraid to report, man 51. The plug is in."
runs_completed: 210
items_processed: 335
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
