---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-11T14:30:00Z"
current_task: "Generated LinkedIn post #174 -- the homeownership / first-time-homebuyer / down-payment-assistance ministry: NOT the eviction/rent-help persona (renters in crisis, already covered as housing-eviction), but the woman in the pew who rented her whole life, was sure a house was never for someone like her, and then bought her first home in her fifties through a FREE HUD-approved housing counselor and a down-payment-assistance program nobody had told her existed -- now the one younger couples and single mothers quietly pull aside after service to ask, quiet, like it is a secret: how did you do it. A peer navigator one generation up from #173's young SNAP mother, chosen for series persona variety and because homeownership knowledge travels exactly this way in these communities: from the one person who finally got through the door. A deliberate TONAL SHIFT for the series -- after a long run of crisis/deficit lanes (food, eviction, utilities, debt, medical bills, SNAP), this is an aspirational build-something lane that lands squarely on The Plug AI voice phrase 'not for people like me,' the exact wall the post dismantles. Holds the whole homeownership maze for families certain the door is bolted shut: that you do NOT need 20% down (the myth that stops more families than any bank), loans exist for as little as 3% and some for nothing (FHA 3.5% / conventional 3% / 0%-down VA-USDA); that the state housing authority (IHDA) has real down-payment and closing-cost assistance most buyers never hear of; that a HUD-approved housing counselor is completely FREE and will prep credit, run readiness, and match you to programs; that a credit score lower than you fear can still qualify and a thin/no file can be built; that the homebuyer-education class unlocks the assistance money; that once you own, the Cook County homeowner exemption lowers the tax bill and seniors get more; that if you already own and fell behind, a HUD counselor can work your servicer BEFORE foreclosure and you should never pay an upfront fee to a rescue company; that contract-for-deed and rent-to-own can look like owning but are often a trap; that the 'we buy houses' cash-offer stripping an elder's equity is predation; and that lending/appraisal discrimination is real and CAN be challenged (reconsideration of value + fair-housing complaint); AI as the buyer's agent, loan officer, and housing counselor a resourced family already has walking beside them -- reframe sharpened: the gap is not that they got a better navigator, it is that the door was always held open for them and locked for us, and what stands in the way is usually information, not ineligibility; real free help routed to: a HUD-approved housing counseling agency (HUD Find-a-Counselor tool + 1-800-569-4287), IHDA (ihda.org) and an IHDA-participating lender, the Cook County Assessor (cookcountyassessor.com) for exemptions, a local fair-housing center + HUD fair-housing line (1-800-669-9777), and 2-1-1; opens a NEW resource-navigation lane -- homeownership / first-time-buyer / down-payment-assistance / foreclosure-prevention -- kept DISTINCT from housing-eviction (renters, #done), benevolence (#153), financial-empowerment/debt-credit-banking (#172), utility/energy (#165), tax/EITC (#166), and food/SNAP (#173); care note on four real current risks: upfront-fee foreclosure-rescue/loan-mod scams (HUD counseling is free), contract-for-deed/rent-to-own traps, 'we buy houses' equity stripping, and lending/appraisal discrimination; DELIBERATELY HEDGED IHDA program names/amounts (they change per cycle -> routed to IHDA + a lender) and DELIBERATELY did NOT name ILHAF as active (largely closed to new applications after 2023-2024 -> foreclosure help routed to a HUD counselor + the servicer); CRITICAL compliance framing stated twice in-body -- general navigation, NOT financial, mortgage, legal, or real-estate advice, and helping someone learn a program exists is NOT being their loan officer or housing counselor -- always route to a HUD-approved counselor, IHDA + a participating lender, and the Cook County Assessor for the actual programs, current rules, and the loan itself; augment-not-replace held (the whispered question after service, the trust, the hand on another renter's shoulder stay hers); ties to Community Intake; the plug is in"
runs_completed: 174
items_processed: 299
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
