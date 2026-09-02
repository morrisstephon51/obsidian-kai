---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-02T14:35:00Z"
current_task: "Generated LinkedIn post #265 -- WHOLLY NEW DOMAIN: SOCIAL SECURITY DISABILITY / SSDI / SSI / DISABILITY BENEFITS / FREE BENEFITS-LEGAL-HELP for a proud WORKING MAN of 56 in the south suburbs who spent his life in physical work (warehouse, loading docks, construction) and whose body has given out -- back that won't hold, diabetes taking his feet + eyes, a heart the doctor keeps warning about -- so he can't do the only work he's known, but was raised a man works, a man provides, a man does not 'go on disability', so he pushes through shifts + pays for it, tells everyone he's 'getting better', stays quiet at church as the strong one, and does not know: SSDI is NOT a handout but insurance he paid into every paycheck for decades + can now draw on; SSI exists for little work history/income; a first DENIAL is NORMAL + appealable (most win on appeal); it costs NOTHING to apply; a legit disability rep charges NOTHING up front -- fee set + capped by SSA, paid only from back pay IF he wins; legal aid, SOAR benefits specialists, Centers for Independent Living, Aging & Disability Resource Centers + 2-1-1 help FREE; and real disability help is FREE to start (no honest program/legal aid/SSA charges an application/processing/activation fee, promises 'guaranteed approval' for money, demands gift cards/wire/cash-app, threatens arrest, or says his SSN is 'suspended'); NO ONE real charges up front to apply or guarantees an approval for a fee. Doors (hedged): apply free at SSA (ssa.gov / 1-800-772-1213 / local office); 2-1-1 for caseworker + local disability resources; FREE help via legal aid / SOAR specialist / Center for Independent Living / Aging & Disability Resource Center; if using a disability attorney/rep, only one who charges NOTHING up front + is paid only the SSA-capped fee from back pay if he wins; verify via real SSA (ssa.gov / number on real SSA mail), official program, or legal aid. Scam spine: SSA IMPOSTER / 'SSN SUSPENDED' / 'WARRANT -- PAY NOW OR BE ARRESTED' (gift cards/wire/cash-app to 'clear it up'), DISABILITY 'APPLICATION'/'ACTIVATION' FEE + 'GUARANTEED APPROVAL', PHISHING for SSN / my Social Security login, FAKE SSA WEBSITE, OVERPAYMENT / 'REACTIVATE YOUR BENEFITS' demand. Flat rule TWICE + SEPARATE caution that SSA itself, 2-1-1, legal aid, SOAR specialists, Centers for Independent Living, and Aging & Disability Resource Centers are NOT scams. Dignity-never-deficit (a man who did hard physical work for decades + paid in every check is not a failure + not begging -- SSDI is insurance he already bought with his labor, drawing on it now his body can't work is exactly its purpose) + AI quiet-helper/augment-not-replace with compliance TWICE (explains SSDI vs SSI + who qualifies, that a first denial is normal + appealable, how to start with SSA + legal aid, what medical records/docs to gather, what the process + a hearing are like; does NOT apply for him, decide eligibility/his medical case, represent him before SSA, give legal or medical advice, promise approval, never handles SSN / my Social Security login / a payment, not a lawyer/doctor/benefits specialist/SSA; verify via real SSA, official program, or legal aid). Rotated to MAN 56 off #264 woman 49; distinct from #263 man 58, #262 woman 27, #261 man 54, #260 woman 66, #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68. WHOLLY NEW Social-Security-disability/SSDI/SSI/disability-benefits domain distinct from eviction/rental (#264), prescription-med (#263), WIC (#262), citizenship (#261), property-tax (#260), veterans-benefits (#259 VA not SSA), unemployment (#258), student loans (#257), health-insurance (#256), childcare (#255), income-tax (#252) -- about the disability insurance he paid into SSA + can now draw on because his body can't do the work, NOT the VA, not unemployment, not retirement. Serves Plug AI community + faith-community + working-family + disability + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-02-social-security-disability-ssdi-ssi-man-free-apply-ssa-legal-aid-soar-capped-rep-imposter-arrest-gift-card-suspended-ssn-activation-fee-guaranteed-approval-phishing-fake-ssa-site-scam-ministry.md. PRIOR (#264): eviction-prevention / rental-assistance / tenant-rights / free eviction legal aid / Eviction Help Illinois + 2-1-1 (proud working woman 49). PRIOR (#263): prescription-medication affordability / insulin rationing / FQHC 340B + Patient Assistance Programs + Medicare Extra Help (proud working man 58). PRIOR (#262): WIC / maternal-and-child nutrition / free formula + breastfeeding support / Illinois WIC + FQHC (young working mother woman 27). The plug is in."
runs_completed: 264
items_processed: 389
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
