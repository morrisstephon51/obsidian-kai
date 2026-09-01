---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-01T00:00:00Z"
current_task: "Generated LinkedIn post #258 -- WHOLLY NEW DOMAIN: UNEMPLOYMENT INSURANCE / IDES BENEFITS after a layoff, for a working WOMAN of 44 in the south suburbs who gave years to one job and was laid off through no fault of her own, was raised to believe unemployment is a handout so she has NOT filed, is burning through savings in silence, and does not know the truths that change everything: unemployment insurance is NOT welfare but a benefit her own work already paid into (filed FREE through IDES at ides.illinois.gov or by phone, built for exactly a no-fault layoff, and a denial can be appealed FREE), free help to file + to find the next job is real (American Job Center / Illinois workNet / IllinoisJobLink, plus free legal aid for a denied claim/appeal), IDES NEVER demands a fee/gift cards to release benefits and never texts out of the blue for her SSN or password, and NO ONE real charges to file, 'speed up' benefits, or fix an 'overpayment' with gift cards. Doors (hedged, none ranked): file FREE direct with IDES (ides.illinois.gov/phone); free help via American Job Center / Illinois workNet / IllinoisJobLink; FREE appeal (legal aid); 2-1-1; verify via ides.illinois.gov + official number, guard SSN + password. Scam spine: FAKE FILE-YOUR-CLAIM/GET-BENEFITS-FASTER ADVANCE-FEE SERVICE, UNEMPLOYMENT IDENTITY-THEFT / FAKE-IDES TEXT-OR-EMAIL PHISHING, IMPOSTER IDES GIFT-CARD/REACTIVATE-YOUR-ACCOUNT SCAM, FAKE UNEMPLOYMENT WEBSITE, and FAKE OVERPAYMENT PAY-BACK-NOW-WITH-GIFT-CARDS SCAM. Flat rule stated TWICE + SEPARATE caution that IDES/ides.illinois.gov, American Job Center/Illinois workNet, legal aid, and 2-1-1 are NOT scams. Dignity-never-deficit (a no-fault layoff is not failure; UI is a benefit her own work paid into, not a handout) + AI quiet-helper/augment-not-replace with compliance TWICE (explains what UI is + who qualifies, how to start a claim at ides.illinois.gov, what docs to gather, how to find nearest American Job Center + hours, what an appeal is; does NOT file the claim, decide eligibility, or promise a benefit amount/approval, never handles SSN/password, not a substitute for IDES; verify with ides.illinois.gov). Rotated to a WOMAN age 44 off #257 man 41; distinct from #256 woman 52, #255 man 33, #254 woman 68, #253 man 29, #252 woman 39, #251 man 46, #250 woman 34. WHOLLY NEW unemployment-insurance domain (benefits after a layoff) distinct from job search (#250, finding the next job), student loans (#257), health insurance enrollment (#256), child care (#255), SNAP/food (#254), expungement (#253), tax (#252), disability (#251), utility (#249), medical debt (#248), citizenship (#247), eviction (#245). Serves Plug AI community + faith-community + working-family + first-gen + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-unemployment-insurance-benefits-ides-free-claim-file-appeal-american-job-center-fake-claim-filing-fee-identity-theft-phishing-imposter-ides-gift-card-fake-unemployment-site-overpayment-gift-card-scam-ministry.md. PRIOR (#257): student loan repayment / IDR / PSLF / studentaid.gov (first-gen man 41). PRIOR (#256): health insurance enrollment / Medicaid / Get Covered Illinois / ACA (uninsured woman 52). PRIOR (#255): child care / CCAP / Head Start / free preschool (single father 33). The plug is in."
runs_completed: 257
items_processed: 382
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
