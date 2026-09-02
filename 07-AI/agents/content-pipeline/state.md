---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-09-02T10:30:00Z"
current_task: "Generated LinkedIn post #264 -- WHOLLY NEW DOMAIN: HOUSING / EVICTION PREVENTION / EMERGENCY RENTAL ASSISTANCE / TENANT RIGHTS / FREE EVICTION LEGAL AID for a proud WORKING WOMAN of 49 in the south suburbs who fell behind on rent after her hours were cut + a medical bill hit, now has a notice taped to her door + a court date she does not understand, and has told no one at church because she was raised you keep your own roof + don't air your troubles -- so she quietly packs boxes 'just in case', loses sleep, calls it handling it, and does not know: a notice/court date is NOT being put out; emergency rental assistance can catch up past-due rent; in Cook County a tenant has real rights + FREE eviction legal help via Eviction Help Illinois + legal aid; court rental-assistance/early-resolution/mediation programs exist; her landlord may take a written payment plan; 2-1-1 + community-action agencies (CEDA) + township general assistance + Catholic Charities point to rent help + a caseworker; and real rental/eviction help is FREE (no honest program/legal aid/court/housing authority charges an application/processing/activation fee, promises 'guaranteed approval' for money, demands gift cards/wire/cash-app, or calls/texts out of the blue for SSN/bank login/a deposit to 'hold' a unit or 'release' assistance); NO ONE real charges to apply or guarantees a rental for a fee. Doors (hedged): 2-1-1 for emergency rental assistance + caseworker; free apply via CEDA / township GA / Catholic Charities / faith funds; FREE eviction legal help via Eviction Help Illinois + legal aid + court rental-assistance/early-resolution/mediation; ask landlord in writing re payment plan; verify via the real court (clerk / number on her actual court papers), official program number, or housing authority. Scam spine: PHANTOM RENTAL LISTING (deposit/first-month by gift card/wire/cash-app to 'hold' a unit sight-unseen), RENTAL-ASSISTANCE 'APPLICATION' FEE + 'GUARANTEED APPROVAL', IMPOSTER 'LANDLORD' / 'PAY OR YOU'RE OUT TODAY' (gift cards/wire, fake sheriff/court fee), FORECLOSURE/EVICTION 'RESCUE' taking a fee or the deed/lease, PHISHING text/call to 'verify/release/keep' assistance or her case via SSN/bank login/payment. Flat rule TWICE + SEPARATE caution that 2-1-1, CEDA, township GA, Catholic Charities, Eviction Help Illinois, legal aid, and the real court are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains options + who qualifies, notice-vs-court-date, how to start with 2-1-1 + legal aid, docs to gather, what a first call/court date is like; does NOT apply for her, decide eligibility, represent her in court, give legal advice, promise approval/rent money, never handles SSN/bank login/a payment, not a lawyer/caseworker/the court; verify via real court, official program, or housing authority). Rotated to WOMAN 49 off #263 man 58; distinct from #262 woman 27, #261 man 54, #260 woman 66, #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68. WHOLLY NEW housing/eviction-prevention/rental-assistance/tenant-rights/eviction-legal-aid domain distinct from utility-shutoff/LIHEAP, property-tax relief (#260 homeowner), prescription-med (#263), WIC (#262), health-insurance (#256), SNAP, childcare (#255), income-tax (#252) -- about keeping the ROOF (rent arrears, eviction notice + court date, tenant rights, free eviction legal help), not utilities and not homeownership. Serves Plug AI community + faith-community + working-family + housing + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-02-eviction-prevention-rental-assistance-tenant-rights-free-legal-aid-eviction-help-illinois-court-211-phantom-listing-application-fee-imposter-landlord-gift-card-foreclosure-rescue-phishing-scam-ministry.md. PRIOR (#263): prescription-medication affordability / insulin rationing / FQHC 340B + Patient Assistance Programs + Medicare Extra Help (proud working man 58). PRIOR (#262): WIC / maternal-and-child nutrition / free formula + breastfeeding support / Illinois WIC + FQHC (young working mother woman 27). PRIOR (#261): U.S. citizenship / naturalization / N-400 + I-912 fee waiver / free accredited-rep legal help (lawful permanent resident man 54). The plug is in."
runs_completed: 263
items_processed: 388
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
