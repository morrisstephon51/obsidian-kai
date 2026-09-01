---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-09-01T12:00:00Z"
current_task: "Generated LinkedIn post #259 -- WHOLLY NEW DOMAIN: VETERANS (VA) BENEFITS after service, for a proud VETERAN MAN of 61 in the south suburbs who served, came home long ago, and never filed for the disability compensation/benefits he earned because he was raised to believe taking anything is a handout and 'others had it worse,' so he has carried a service-connected condition and a shrinking budget in silence, and does not know the truths that change everything: VA benefits are NOT welfare but earned by his own service (filed FREE with an accredited Veterans Service Officer at va.gov or by phone, built for exactly a veteran with a service-connected condition, and a denial can be appealed FREE), free help to file + appeal is real (accredited VSOs at VFW / American Legion / DAV / Cook County Veterans Assistance Commission, plus free legal aid), the VA NEVER demands a fee/gift cards to release benefits and never texts out of the blue for his SSN, VA login, or direct-deposit info, and NO ONE real charges a percentage or upfront fee to file, 'maximize' a rating, or fix an 'overpayment' with gift cards. Doors (hedged, none ranked): file FREE with an accredited VSO (VFW/American Legion/DAV/Cook County VAC); file/manage direct at va.gov or by phone; FREE appeal (accredited rep or legal aid); 2-1-1 or the VA line; verify via va.gov + official number, guard SSN + VA login + direct deposit. Scam spine: FEE-CHARGING CLAIM-SHARK / UNACCREDITED CLAIM CONSULTANT, IMPOSTER-VA PHISHING (fake VA text/email/call harvesting SSN + VA.gov login), IMPOSTER VA/UPDATE-YOUR-DIRECT-DEPOSIT GIFT-CARD/REACTIVATE-ACCOUNT SCAM, FAKE VA WEBSITE, and FAKE OVERPAYMENT/PENSION-REVIEW PAY-BACK-NOW-WITH-GIFT-CARDS SCAM. Flat rule stated TWICE + SEPARATE caution that the VA/va.gov, accredited VSOs, legal aid, and 2-1-1 are NOT scams. Dignity-never-deficit (a veteran carrying a service-connected condition is not a burden; VA benefits are earned by his service, not a handout) + AI quiet-helper/augment-not-replace with compliance TWICE (explains what VA benefits are + who generally qualifies, how to start at va.gov, what service records/docs to gather, how to find the nearest accredited VSO + hours, what an appeal is; does NOT file the claim, decide the rating/eligibility, or promise a benefit amount/approval, never handles SSN/VA login, not a substitute for the VA or a VSO; verify with va.gov). Rotated to a MAN age 61 off #258 woman 44; distinct from #257 man 41, #256 woman 52, #255 man 33, #254 woman 68, #253 man 29, #252 woman 39, #251 man 46. WHOLLY NEW veterans-benefits domain distinct from civilian disability/SSDI-SSI (#251), unemployment (#258), student loans (#257), health insurance (#256), child care (#255), SNAP/food (#254), expungement (#253), tax (#252), job search (#250), utility (#249), medical debt (#248), citizenship (#247), eviction (#245). Serves Plug AI community + faith-community + working-family + veterans + first-gen + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-veterans-benefits-va-disability-compensation-pension-accredited-vso-free-claim-appeal-claim-shark-fee-imposter-va-phishing-gift-card-direct-deposit-fake-va-site-overpayment-scam-ministry.md. PRIOR (#258): unemployment insurance / IDES / free claim + appeal / American Job Center (laid-off woman 44). PRIOR (#257): student loan repayment / IDR / PSLF / studentaid.gov (first-gen man 41). PRIOR (#256): health insurance enrollment / Medicaid / Get Covered Illinois / ACA (uninsured woman 52). The plug is in."
runs_completed: 258
items_processed: 383
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
