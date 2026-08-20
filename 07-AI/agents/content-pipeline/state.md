---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-19T21:30:00Z"
current_task: "Generated LinkedIn post #216 -- NEW lane: citizenship / naturalization + DOJ-accredited / nonprofit free-or-low-cost help + fee waiver + 'notario' / unauthorized-practice-of-law scam ministry. A WOMAN, 52, a lawful permanent resident for ~18 years who has worked and raised her children here, is eligible to naturalize but frozen by fear -- the English/civics test, the fee she thinks she cannot spare, the terror of one wrong mark costing her the card and the life she has, and a quiet shame at needing help with English -- not knowing that recognized nonprofit organizations with DOJ-accredited representatives help at no or low cost, that a fee waiver (I-912) may exist for those who qualify, that free English/citizenship classes and free official USCIS civics study materials exist, and that only a licensed attorney or a DOJ-accredited representative may LAWFULLY give immigration legal advice -- while a 'notario' / unaccredited 'consultant' promises to 'handle everything' and 'guarantee' citizenship for thousands, quietly practices law he is not licensed to practice (the notario=lawyer confusion from other countries is exactly what he sells), files wrong/false answers that jeopardize her status, and holds her documents/money/logins hostage. Doors (hedged, none ranked): name it/know help exists (eligible LPRs may apply; governed by USCIS+federal law, confirm with attorney or accredited rep); accredited/nonprofit help FREE-or-low-cost (DOJ-recognized orgs, immigrant legal aid); the fee may not be the wall (I-912 waiver; free classes + free official civics materials); gather what helps (green card, records, study civics questions today at her own pace); the weight (faith, mentor, family, church, accredited rep/legal aid). Flat rule: only a licensed attorney or DOJ-accredited rep may lawfully advise on immigration, recognized nonprofits help free/low cost, and no one can guarantee a citizenship outcome -- anyone 'guaranteeing' citizenship, charging a fortune to 'handle everything,' filling in answers she does not understand, or holding her documents/logins is the scam. Held a SEPARATE caution: a real USCIS notice (biometrics, interview, request for evidence) is NOT a scam -- do not miss it; and a legitimately licensed immigration attorney charging a fair, disclosed fee is valid -- the caution is about UNLICENSED notarios, guarantees, and info-harvesting, not all paid help. AI in quiet-helper + augment-not-replace mode (explains naturalization/LPR/N-400/biometrics/civics test/English test/fee waiver-I-912/DOJ-accredited representative; helps her understand what applying involves; helps her find a DOJ-recognized org/legal aid/USCIS-approved classes herself; helps her practice the free official civics questions; names the notario scam -- does NOT fill out the N-400 as her, give legal advice on her case, or promise citizenship/an outcome; never fed her A-number/SSN/USCIS login/full immigration file). Compliance stated twice in-body (general navigation, NOT legal/immigration advice, NOT an eligibility determination; immigration law governed by USCIS+federal law, decided by USCIS, not a machine); dignity, never deficit (a woman who has lived, worked, paid taxes, and raised a family here 18 years is not less-than for not yet being a citizen and not a failure for finding the test frightening; fear of starting is the weight of what she has to lose, not laziness). Rotated gender back to a WOMAN off the man 63 (#215); centers a LONG-TIME IMMIGRANT (woman 52). Distinct from VA disability #215, special ed #214, property tax #213, utility #212, wage theft #211 -- a path to citizenship, accredited/nonprofit help, and the notario scam, not a means-tested benefit. Saved to output/linkedin-2026-08-19-citizenship-naturalization-notario-fraud-scam-ministry.md. PRIOR (#215): veterans / VA disability + accredited-free-help + claim-shark scam, man 63. PRIOR (#214): special education / IEP + 504 + paid-advocate scam, woman 36. PRIOR (#213): property tax / senior exemption + tax-sale scam, man 71. The plug is in."
runs_completed: 216
items_processed: 341
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
