---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-02T00:00:00Z"
current_task: "Generated LinkedIn post #263 -- WHOLLY NEW DOMAIN: PRESCRIPTION-MEDICATION AFFORDABILITY / MEDICATION ASSISTANCE (his diabetes + high-blood-pressure meds almost certainly cost far less through free, legitimate doors -- FQHC community health center on a sliding scale + deeply discounted 340B pharmacy pricing; drug-maker Patient Assistance Programs (PAPs) giving brand meds + insulin free/near-free; manufacturer insulin savings programs + monthly insulin caps; Medicare 'Extra Help' / Part D Low-Income Subsidy via Social Security + free Illinois SHIP counselors; generics, $4 generic lists, 90-day supplies via his own pharmacist/doctor; free price tools GoodRx/NeedyMeds/RxAssist) for a proud WORKING MAN of 58 in the south suburbs who quietly rations his pills + stretches his insulin (skips doses, cuts tablets in half, saves the vial to month's end) because the copays + cash price scare him more than the diagnosis, and has never asked for help because he was raised a man handles it himself and doesn't complain -- so he goes without and calls it managing, and does not know: real medication help is FREE (real discount cards are free; no honest pharmacy/health center/manufacturer program/Medicare office charges an enrollment/activation/membership fee, demands gift cards or a wire, or calls/texts out of the blue for his Medicare number, SSN, or bank login to 'verify/reactivate/keep' coverage or 'send a new card'); and NO ONE real charges to sign him up or promises 'guaranteed approval' for a fee. Doors (hedged): FQHC sliding-scale + 340B pricing; ask his pharmacist/doctor re generics, $4 list, 90-day supply, free manufacturer savings/assistance; apply free to the manufacturer PAP for his specific brand drug/insulin (find via NeedyMeds/RxAssist); if on Medicare, Extra Help / Part D LIS via Social Security + free Illinois SHIP; free price tools (GoodRx) to compare cash price; 2-1-1 for local health center + free/charitable clinic; verify via real pharmacy, clinic's real number, Medicare.gov, or official manufacturer program. Scam spine: FAKE ONLINE 'PHARMACY' (counterfeit/dangerous/no meds), PRESCRIPTION 'DISCOUNT CARD' / ASSISTANCE ENROLLMENT FEE (membership/activation fee for free help, or 'guaranteed approval' for money), MEDICARE/PART D IMPOSTER 'NEW CARD / VERIFY OR LOSE YOUR COVERAGE' (fishing Medicare number/SSN/bank or a fee), COUNTERFEIT/UNSAFE MEDICATION sold cheap, PHISHING TEXT/CALL to 'confirm/reactivate/protect' pharmacy account or coverage via Medicare number/SSN/card/bank login. Flat rule TWICE + SEPARATE caution that FQHCs, his own doctor + pharmacist, licensed pharmacies, real manufacturer PAPs, Medicare/Social Security/Illinois SHIP, and 2-1-1 are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains options + who generally qualifies, how to start with an FQHC + his pharmacist, docs to gather, how to find a real manufacturer program + what an appointment is like; does NOT enroll him, decide eligibility, prescribe/change meds, promise approval/price, never handles Medicare number/SSN/card/bank login, not a doctor/pharmacist/substitute for his clinic; verify via real pharmacy, clinic, Medicare.gov, official manufacturer program). Rotated to MAN 58 off #262 woman 27; distinct from #261 man 54, #260 woman 66, #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68, #253 man 29. WHOLLY NEW prescription-med-affordability domain distinct from health-insurance (#256), medical debt/charity care, WIC nutrition (#262), SNAP, disability/SSDI-SSI (#251), income-tax (#252); adjacent to but distinct from health-insurance + medical-debt posts (focused on the cost of the drugs themselves: generics, 340B, PAPs, insulin caps, Extra Help). Serves Plug AI community + faith-community + working-family + seniors/older-adults + health + chronic-illness + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-02-prescription-medication-assistance-man-insulin-rationing-fqhc-340b-patient-assistance-program-medicare-extra-help-generics-fake-pharmacy-discount-card-fee-imposter-counterfeit-scam-ministry.md. PRIOR (#262): WIC / maternal-and-child nutrition / free formula + breastfeeding support / Illinois WIC + FQHC (young working mother woman 27). PRIOR (#261): U.S. citizenship / naturalization / N-400 + I-912 fee waiver / free accredited-rep legal help (lawful permanent resident man 54). PRIOR (#260): property-tax relief / homeowner-senior exemptions + Senior Freeze / free appeal / Cook County Assessor (widowed homeowner woman 66). The plug is in."
runs_completed: 262
items_processed: 387
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
