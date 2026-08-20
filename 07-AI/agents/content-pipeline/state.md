---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-19T21:00:00Z"
current_task: "Generated LinkedIn post #215 -- NEW lane: the veterans / VA disability claim + 'claim shark' scam ministry. A MAN, 63, a veteran whose old service injury (wrecked back, bad knees, hearing that never came all the way back) has WORSENED with age, gets by in pain and calls it toughness, is certain the VA closed the door on him years ago (an old 'no' or an unfinished stack of forms), and is too proud to ask for what he wrongly reads as a HANDOUT -- not knowing that a service-connected condition, including one that got worse or was denied before, may let him FILE or REOPEN a claim, that accredited Veterans Service Officers (VFW, American Legion, DAV, PVA, free county/state veteran service officers) help at NO COST, that VA.gov lists accredited reps, that the claim itself is FREE to file, and that it is AGAINST FEDERAL LAW for an unaccredited outfit to charge a fee to prepare or present an INITIAL claim -- while 'claim shark' companies advertising on late-night TV / social promise to 'maximize your rating' or 'get you to 100%' for a big upfront fee or a cut of his back pay, coach exaggeration (fraud that exposes the veteran), impersonate the VA demanding a fee/gift cards, and harvest his info. Doors (hedged, none ranked): name it and know an old 'no' may not be the end (file/reopen; confirm with an accredited rep or the VA -- governed by VA + federal law); get accredited help FREE (VSOs, county/state veteran service offices, VA.gov); the claim is FREE to file and charging for an initial claim is unlawful; gather what helps (service records, medical records showing worsening, his own account -- a step today); the weight (faith, mentor, family, church, accredited VSO, Veterans Crisis Line 988 then press 1). Flat rule: filing is free, accredited VSOs help at no cost, and it is illegal for an unaccredited outfit to charge to prepare/present an initial claim -- anyone charging a big upfront fee or a cut of back pay, coaching exaggeration, or fishing for his login is the scam, not the help. Held a SEPARATE caution: a real C&P exam notice, a real VA decision letter, and real record requests are NOT scams -- do not miss the exam or ignore the mail; showing up is exactly right; and a VA-accredited attorney/claims agent charging a VA-regulated fee on an APPEAL (after an initial decision) can be lawful and valid -- the caution is about upfront fees on INITIAL claims, guarantees, exaggeration coaching, and info-harvesting, not all accredited/paid help. AI in quiet-helper + augment-not-replace mode (explains 'service connection,' 'disability rating,' 'C&P exam,' 'back pay,' 'supplemental claim,' 'appeal,' 'accredited representative,' 'VSO'; helps him understand what filing/reopening involves; helps him find an accredited VSO / county veteran service office / VA.gov himself; names the scam -- does NOT file as him, speak to the VA as him, or promise a rating/percentage/dollar amount; never fed his SSN / VA.gov login / bank login / full medical records). Compliance stated twice in-body (general navigation, NOT legal/medical/VA-claims advice, NOT a rating or eligibility determination; accreditation/ratings/claims governed by the VA + federal law, decided by the VA, not a machine); dignity, never deficit (a veteran claiming compensation for an injury carried home from service is not milking anything and is not asking for charity -- it is earned; too proud to ask is a door held shut by shame, not strength; not knowing an old denial can be reopened or that free accredited help exists is help nobody walked him through). Rotated gender back to a MAN off the woman 36 (#214); centers an OLDER VETERAN (man 63). Deliberately distinct from every benefit/bill/wage/tax/school-right lane in the recent run (special ed #214, property tax #213, utility #212, wage theft #211, childcare #210) -- earned disability compensation, free accredited help, and the claim-shark scam, not a means-tested benefit. Saved to output/linkedin-2026-08-19-veterans-va-disability-claim-shark-scam-ministry.md. PRIOR (#214): special education / IEP + Section 504 parent rights + paid-advocate / diagnosis-mill scam -- a working mother reading every note home as a verdict on her struggling child and herself, woman 36. PRIOR (#213): property tax / senior-homeowner exemption + tax-sale rescue scam -- a man bracing to lose his paid-off home over a delinquent tax bill, man 71. PRIOR (#212): utility shutoff / energy assistance (LIHEAP) -- a woman on a fixed income rationing to keep the power on in the August heat, woman 58. The plug is in."
runs_completed: 215
items_processed: 340
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
