---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-31T04:23:00Z"
current_task: "Generated LinkedIn post #252 -- WHOLLY NEW DOMAIN: FREE TAX FILING / EITC / CHILD TAX CREDIT / VITA for a working mother of 39 in the south suburbs juggling two part-time jobs, scared of taxes because she thinks she owes money she cannot pay (skipped filing some years out of fear), then framed the truths that change everything: she may be OWED a REFUND she never claimed (EITC + Child Tax Credit are money she EARNED by working, not welfare), filing help is FREE (VITA / AARP Tax-Aide sites, IRS Free File at IRS.gov, community tax clinics), a real preparer SIGNS the return and never takes a cut of the refund, and NO ONE from the IRS calls to threaten arrest or demand gift cards. Doors: free VITA/Tax-Aide + IRS Free File; claim EITC/CTC including prior unfiled years she can still go back and file; Low Income Taxpayer Clinic / community tax clinic if behind or owing; own IRS.gov account with refund into HER OWN bank account. Scam spine: GHOST PREPARER (big fee, huge-refund promise, wont sign the return), REFUND-ANTICIPATION/INSTANT-REFUND ADVANCE-FEE, IRS PHONE/EMAIL IMPOSTER (owe-back-taxes-arrest-gift-cards), REFUND-REDIRECTION/STOLEN-REFUND (preparer reroutes/inflates refund), and FAKE EXTRA-REFUND/STIMULUS PHISHING. Flat rule stated TWICE + SEPARATE caution that IRS/IRS.gov/VITA/Tax-Aide/LITC/community clinics are NOT scams. Dignity-never-deficit (working two jobs and still being owed money you never claimed is proof you worked, not that you failed; EITC/CTC are your own wages back, not begging). AI quiet-helper/augment-not-replace with compliance TWICE (explains which credits she may qualify for, builds her document checklist, finds the nearest free VITA/Tax-Aide site + hours, decodes a notice, preps her questions; does NOT file the return, does NOT guarantee a refund amount or give tax advice, never hands over SSN or bank login, not a substitute for the IRS or a real VITA volunteer; verify with the real IRS). Rotated to a WOMAN age 39 off #251 man 46; distinct from #250 woman 34, #249 man 61, #248 woman 52. WHOLLY NEW tax-and-refund domain distinct from disability/SSDI (#251), job search/workforce (#250), utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245), long-term care (#244). Ties to The Plug AI Get-Connected + benefits-navigation + financial-literacy pillar. Serves Plug AI community + faith-community + working-family + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-30-free-tax-filing-eitc-ctc-vita-earned-income-credit-refund-ghost-preparer-refund-anticipation-advance-fee-irs-imposter-gift-card-refund-redirect-fake-stimulus-scam-ministry.md. PRIOR (#251): Social Security disability / SSDI / SSI (disabled tradesman 46). PRIOR (#250): job search / employment / workforce (single mother 34). PRIOR (#249): utility shutoff / heat & electric / LIHEAP (retired man 61). The plug is in."
runs_completed: 251
items_processed: 376
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
