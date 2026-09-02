---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-02T18:40:00Z"
current_task: "Generated LinkedIn post #266 -- WHOLLY NEW DOMAIN: LIHEAP / UTILITY & ENERGY-BILL ASSISTANCE / HEAT-AND-LIGHT SHUTOFF PROTECTION / PIPP for a proud WORKING WOMAN of 63 in the south suburbs who has kept a warm, decent, welcoming home her whole life, whose hours got cut this fall while the ComEd + Nicor bills climbed, so she quietly keeps the thermostat down + wears a sweater and two pairs of socks in her own front room + runs the heat only when the grandbabies visit so no one feels the cold or knows how tight it's gotten, folded the shutoff notice into a drawer, and does not know: LIHEAP (Low Income Home Energy Assistance Program) helps pay heat + light + is NOT welfare/charity; PIPP (Percentage of Income Payment Plan) can cap her bill at a share of income + chip away arrears as she keeps up; Illinois has WINTER DISCONNECTION protections so the heat is not just cut in the dead of winter without notice + options; ComEd, Nicor Gas + Peoples Gas each have their own hardship funds, payment plans + low-income discounts; one free call to CEDA (Community and Economic Development Association of Cook County, which runs LIHEAP for suburban Cook) or 2-1-1 starts real help; it costs NOTHING to apply; and real utility help is FREE to start (no honest program/CEDA/real utility charges an application/processing/reconnection fee up front, demands gift cards/prepaid card/Zelle/cash-app/crypto, threatens shutoff 'in 30 minutes unless you pay now', or sends a stranger to the door demanding cash); NO ONE real makes her pay a fee up front for an energy grant or 'guarantees' a benefit for money. Doors (hedged): apply free for LIHEAP + PIPP via CEDA or the state program; free 2-1-1 call for a caseworker + local energy resources; call the REAL ComEd/Nicor/Peoples Gas number printed on her paper bill for payment plans, hardship funds + low-income discounts; ask about Illinois winter disconnection protections before assuming the heat can be cut; verify via the real utility (number on her paper bill), CEDA, LIHEAP, or 2-1-1 before paying/trusting anyone. Scam spine: UTILITY IMPOSTER / 'POWER (or GAS) SHUT OFF IN 30 MINUTES -- PAY NOW' (gift cards/prepaid card/Zelle/cash-app/crypto to stop a disconnection), FAKE 'RECONNECTION FEE'/'DEPOSIT'/'PROCESSING FEE' up front for help/a grant that's free to start, DOOR-TO-DOOR fraud (fake 'utility worker', fake 'free energy audit', supplier 'slamming'), PHISHING for account number/SSN/payment via link or fake utility website, 'YOU'VE BEEN APPROVED FOR AN ENERGY GRANT -- JUST PAY THE FEE' advance-fee scam. Flat rule TWICE + SEPARATE caution that LIHEAP, CEDA, 2-1-1, ComEd, Nicor Gas, Peoples Gas + the utilities' own assistance programs are NOT scams. Dignity-never-deficit (a woman who worked her whole life + kept a warm decent home is not a failure + not begging -- LIHEAP + utility assistance are funded for exactly a working household squeezed by hours cut + prices up; keeping the heat + lights on for her family is providing, + asking for help she qualifies for is stewardship not shame) + AI quiet-helper/augment-not-replace with compliance TWICE (explains LIHEAP vs PIPP + who qualifies, that Illinois has winter disconnection protections, how to start with CEDA/2-1-1/the real utility, what documents to gather, what the appointment + process are like; does NOT apply for her, decide eligibility, promise a grant/amount, contact the utility for her, handle her utility login/SSN/a payment, is not the utility/CEDA/a caseworker; verify via the real utility, CEDA, LIHEAP, or 2-1-1). Rotated to WOMAN 63 off #265 man 56; distinct from #264 woman 49, #263 man 58, #262 woman 27, #261 man 54, #260 woman 66, #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33. WHOLLY NEW LIHEAP/utility-energy-bill-assistance/heat-and-light-shutoff-protection/PIPP domain distinct from SSDI/disability (#265), eviction/rental (#264 -- housing, not the utility bill), prescription-med (#263), WIC (#262), citizenship (#261), property-tax (#260), veterans-benefits (#259), unemployment (#258), student loans (#257), health-insurance (#256), childcare (#255), income-tax (#252) -- about keeping heat/gas/electricity on through LIHEAP, PIPP, utility hardship funds + Illinois winter protections, NOT rent, not a medical bill, not a tax bill. Serves Plug AI community + faith-community + working-family + senior + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-02-liheap-utility-energy-assistance-woman-heat-light-shutoff-ceda-pipp-211-comed-nicor-winter-moratorium-hardship-fund-utility-imposter-gift-card-reconnection-fee-fake-audit-phishing-scam-ministry.md. PRIOR (#265): Social Security disability / SSDI / SSI / free benefits-legal help / SSA + legal aid + SOAR (proud working man 56). PRIOR (#264): eviction-prevention / rental-assistance / tenant-rights / Eviction Help Illinois + 2-1-1 (proud working woman 49). PRIOR (#263): prescription-medication affordability / insulin rationing / FQHC 340B + Patient Assistance Programs + Medicare Extra Help (proud working man 58). The plug is in."
runs_completed: 265
items_processed: 390
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
