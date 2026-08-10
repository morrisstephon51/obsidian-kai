---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-10T23:52:00Z"
current_task: "Generated LinkedIn post #170 -- the medical-bills / healthcare-access / charity-care ministry: the sister who spent thirty years in a hospital billing office and now, retired, sits at kitchen tables with the grocery bag of unopened envelopes families bring her when the collector calls -- she opens the envelope for the man too scared to slit it, knows the bill is a first offer because she used to cut them, knows charity care exists because she used to process it -- and then single-handedly trying to hold the whole medical-bills-and-coverage maze for people who got sick in a country where getting care and paying for care are two different fights: that a bill is NOT final and you can demand an itemized statement where duplicate charges and coding errors hide; that nonprofit hospitals are required by law (ACA / IRS 501(r)) to have a written financial-assistance (charity care) policy that can slash or wipe a bill and may NOT start extraordinary collections before checking eligibility, and applying is FREE yet most who qualify never apply because no one told them; Illinois-specific protection (the Hospital Uninsured Patient Discount Act + Fair Patient Billing Act -- real discounts for uninsured patients, no collections/suit before an eligibility check); the No Surprises Act voiding many surprise out-of-network bills and guaranteeing the uninsured a good-faith estimate; retroactive Medicaid reaching back up to three months before you applied; FREE certified navigators via Get Covered Illinois (1-866-311-1119) for Medicaid + marketplace; prescription patient-assistance programs for the insulin someone is rationing; and the truth that a medical bill is NOT a verified debt -- errors can be disputed and legit charity-care help never charges a fee; AI as the patient-advocate / benefits-counselor a resourced family keeps on retainer -- plus real free help anyone can reach: the hospital's financial-assistance / patient-advocate office, a certified Get Covered Illinois navigator (1-866-311-1119), Illinois Medicaid via ABE, the nonprofit Dollar For for charity-care applications, the Illinois AG Health Care Helpline for billing disputes (1-877-305-5145), and 2-1-1; augment-not-replace held (the kitchen table and the opened envelope stay hers), frees her to say you do not owe what that letter says, there is a door, we are going to walk through it before you pay one dollar you did not have to; opens a NEW resource-navigation lane -- medical-bills / healthcare-access / charity-care navigation -- kept DISTINCT from health (population health / screenings, the existing health-ministry lane), benevolence (cash), senior/caregiver (eldercare), veterans/military-benefits (#169), civil legal-aid (#168), tax/EITC (#166), housing/eviction (tenant), disability/special-needs (inclusion), and employment (jobs); added a care note on medical-debt scams (upfront fees to erase/settle/negotiate debt when charity care is free; collectors treating an unverified bill as a proven debt) paired with the affirming fact that legit help is free; deliberately HEDGED the medical-debt-and-credit point (federal reporting rules contested/litigated through 2025) -- framed as a bill is not a verified debt, errors can be disputed, route to a navigator, not asserting medical debt is off all credit reports; CRITICAL compliance framing stated twice in-body -- general navigation, NOT medical, financial, legal, or insurance advice, and helping is NOT being someone's patient advocate or benefits counselor -- always route to the hospital's financial-assistance office, a certified navigator, Illinois Medicaid, or a nonprofit like Dollar For for the actual application; ties to Community Intake; the plug is in"
runs_completed: 170
items_processed: 295
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
