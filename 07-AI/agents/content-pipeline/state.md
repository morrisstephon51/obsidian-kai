---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-18T13:05:00Z"
current_task: "Generated LinkedIn post #208 -- NEW lane: the food-assistance / SNAP + EBT benefit-theft ministry. A WOMAN, 64, a grandmother raising two grandchildren on a part-time paycheck and a thin fixed income, who skips her own meals so the kids eat full plates -- never applied for food help because a lifetime taught her 'food stamps' meant failure and shame -- not knowing that SNAP is a benefit a working caregiver raising grandchildren may well qualify for, that applying is free through the state, that food banks and benefits navigators will help her apply at no cost, and that there are other food doors right now (pantries, WIC, free school and summer meals for the grandkids, senior food programs) with no fee and no shame -- while EBT card-skimming thieves, 'verify your card and PIN' phishing texts, and upfront 'SNAP application fee / benefits enrollment' con artists hunt a proud older woman who thinks the whole system was built to look down on her. Doors (hedged, none ranked): apply (a benefit she may qualify for, free to apply, confirm with state SNAP office / navigator, don't rule yourself out); protect the card (skimming/phishing real, guard the PIN, never share the full card number, check the balance, report theft fast, some states can replace stolen SNAP -- confirm state rule); free help applying (food banks, community action agencies, navigators, 211, no upfront fee); other food doors (pantries, WIC, school + summer meals, senior programs, no fee no shame); the shame + pride (faith, friend, 211, 988). Flat rule: applying is free, real help to apply is free, and no one honest charges a fee to enroll you or texts demanding your EBT card number and PIN -- anyone charging to file, guaranteeing approval, or asking for your card + PIN to 'reactivate' is the thief, not the help. Held a SEPARATE caution: a real SNAP notice (recertification deadline, scheduled interview, document request) is NOT a phishing text -- don't ignore genuine paperwork with a real clock. AI in quiet-helper mode (explains the words, finds the state SNAP office / food bank / community action agency / 211 to reach herself, helps her understand a recertification deadline + what documents to gather, reads a confusing notice, names the scam -- does NOT decide/guarantee eligibility, submit her application as her caseworker, or act as a benefits office; never fed full SSN / EBT card number / PIN / bank login). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a WOMAN off the #207 man 51; centers an OLDER KINSHIP CAREGIVER GOING HUNGRY SO THE GRANDKIDS EAT (64). Deliberately distinct from health coverage (#206 = Medicaid/ACA), SSDI (#203 = the body that can't work), and debt (#205/#196 = a bill already owed) -- this is FOOD ON THE TABLE THIS WEEK and the nutrition benefit meant to cover it. Saved to output/linkedin-2026-08-18-snap-food-assistance-ebt-theft-scam-ministry.md. PRIOR (#207): workers' compensation / workplace injury -- mid-life manual laborer hurt on the job and afraid to report, man 51. PRIOR (#206): health coverage / Medicaid / ACA-marketplace enrollment -- working mother uninsured after a job loss, woman 39. PRIOR (#205): debt collection / collector harassment / know-your-rights -- older near-retirement man 63. The plug is in."
runs_completed: 208
items_processed: 333
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
