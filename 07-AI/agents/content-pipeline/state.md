---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-30T23:48:00Z"
current_task: "Generated LinkedIn post #251 -- NEW DOMAIN: SOCIAL SECURITY DISABILITY / SSDI / SSI for a worn-out tradesman of 46 in the south suburbs whose back and knees gave out after 25 years of physical labor, who is too ashamed to say the word disability out loud, then framed the truths that change everything: the disability benefit is INSURANCE HE ALREADY PAID FOR with every paycheck (not welfare/handout), applying is FREE (SSA never charges to apply), free/registered help is real (local Social Security office + ssa.gov, legal aid, a registered representative paid ONLY if you win and ONLY out of back pay capped by federal law, Illinois DRS + Aging & Disability Resource Center + Work Incentives Planning), and NO ONE can guarantee an SSA approval. Scam spine: GUARANTEED-APPROVAL/ADVANCE-FEE disability fee, SSA PHONE/EMAIL IMPOSTER (SSN-suspended/benefits-cut-off demanding gift cards/wire/crypto), FAKE DISABILITY-GRANT advance-fee, BENEFIT-REDIRECTION/REP-PAYEE fraud (take over direct deposit/manage benefits), and MY-SOCIAL-SECURITY-ACCOUNT PHISHING. Flat rule stated TWICE + SEPARATE caution that SSA/ssa.gov/local office/legal aid/registered rep on contingency/Illinois DRS are NOT scams. Dignity-never-deficit (a body worn out by 25 years of honest labor is not a moral failure; disability is not a dirty word; collecting insurance you paid premiums on for a quarter century is not begging, it is arithmetic and self-respect). AI quiet-helper/augment-not-replace with compliance TWICE (explains SSDI-vs-SSI plainly, organizes work history + medical records, decodes a denial letter, preps for a hearing, finds the real SSA office/legal aid/DRS; does NOT file the claim, does NOT decide the case or guarantee approval, never hands over SSN or my-SSA password, not a substitute for real SSA process; verify with real SSA; never pay up front, never trust guaranteed approval, never give login to a caller). Rotated to a MAN age 46 off #250 woman 34; distinct from #249 man 61, #248 woman 52, #247 man 57. WHOLLY NEW disability-benefits domain distinct from job search/workforce (#250), utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245), long-term care (#244). Ties to The Plug AI Get-Connected + benefits-navigation pillar. Serves Plug AI community + faith-community + working-family + disability + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-30-social-security-disability-ssdi-ssi-free-ssa-help-legal-aid-representative-contingency-drs-guaranteed-approval-advance-fee-ssa-imposter-gift-card-payee-redirect-scam-ministry.md. PRIOR (#250): job search/employment/workforce (single mother 34). PRIOR (#249): utility shutoff/LIHEAP (man 61). PRIOR (#248): medical debt/charity care (woman 52). The plug is in."
runs_completed: 250
items_processed: 375
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
