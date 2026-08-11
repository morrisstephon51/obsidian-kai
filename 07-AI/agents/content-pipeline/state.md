---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-11T12:12:00Z"
current_task: "Generated LinkedIn post #173 -- the food-benefits / SNAP-navigation ministry: NOT the food pantry coordinator handing out boxes (distribution logistics, already done), but the young mother in the third pew who cracked the SNAP maze for her own kids the hard way -- sat in the public-aid office, filled the application out wrong the first time, got cut off at a recertification she never knew was coming -- and is now the one other mothers quietly slide a phone across the fellowship-hall table to and say denied me, I don't understand this letter. A young peer navigator, not a retired expert, chosen for deliberate series variety and because food-benefit knowledge really does travel mother-to-mother in these communities. And then single-handedly trying to hold the whole food-benefits maze for working families who assume they earn too much, who got scared off by the changed work rules, who let the benefit lapse at recert without knowing why: that SNAP goes through the same ABE portal as Medicaid and the income cutoff is higher than people think, that a car and a little savings don't knock you out; that expedited SNAP can put food on the card in 7 days when the kitchen is empty tonight; that the number-one reason benefits vanish is a missed recertification, not ineligibility; that the SNAP work rules changed and scared people off but the exemptions are wide, so don't assume you're disqualified; that WIC covers pregnant and postpartum moms and kids under five and you can have WIC and SNAP both; that Summer EBT / SUN Bucks loads real grocery money for every school-lunch kid when summer hits; that Double Up Food Bucks doubles SNAP dollars on produce at the market; that college students and lawfully-present immigrant families qualify far more than they believe and SNAP for the citizen children is not a public-charge trap; and that being on SNAP is not charity and not a moral failure -- it is nutrition assistance a working family is owed; AI as the benefits counselor a resourced family never even needs because they never navigate hunger at all -- the reframe sharpened from prior posts: the gap is not that they got a better navigator, it's that they were never made to become an expert in staying fed; plus real free help anyone can reach: the ABE portal (abe.illinois.gov), the local DHS Family Community Resource Center, the Illinois DHS Helpline (1-800-843-6154), a certified SNAP-outreach navigator through the Greater Chicago Food Depository, the Illinois Hunger Coalition Hunger Hotline (1-800-359-2163), WIC, and 2-1-1; opens a NEW resource-navigation lane -- food-benefits / SNAP / WIC / nutrition-benefits navigation -- kept DISTINCT from the food pantry coordinator (distribution logistics), benevolence (one-time emergency cash, #153), childcare/early-childhood, medical-bills/healthcare-access (#170), utility/energy (#165), tax/EITC (#166), and financial-empowerment/debt (#172); added a care note on food-benefit scams (anyone charging a fee to 'get you food stamps' when applying is free) and Link/EBT card skimming (protect the PIN, freeze the card, report theft immediately -- hedged on reimbursement since federal replacement of stolen SNAP lapsed end of 2024 and stays contested); DELIBERATELY hedged the SNAP work-rule point too, since the ABAWD ages/exemptions changed under both the 2023 and 2025 federal laws -- framed as 'the rules changed, the exemptions are wide, check' and routed to a caseworker for current rules; CRITICAL compliance framing stated twice in-body -- general navigation, NOT legal, benefits-eligibility, or nutrition advice, and helping read a letter is NOT being someone's caseworker -- always route to DHS/ABE, a certified SNAP-outreach navigator, WIC, or 2-1-1 for the actual application and current rules; augment-not-replace held (the phone slid across the table, the plate quietly sent home, the trust stay hers); ties to Community Intake; the plug is in"
runs_completed: 173
items_processed: 298
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
