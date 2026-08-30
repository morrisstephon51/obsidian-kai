---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-30T14:15:00Z"
current_task: "Generated LinkedIn post #249 -- NEW DOMAIN: UTILITY SHUTOFF / HEAT & ELECTRIC / ENERGY ASSISTANCE (LIHEAP) for a retired man of 61 on a fixed Social Security check in the south suburbs who rationed the heat to 58 degrees, ran unsafe space heaters, and got a red DISCONNECTION / FINAL NOTICE / SHUTOFF PENDING envelope -- then got a phone imposter demanding a prepaid card in 30 minutes 'or the power goes off' and a flyer promising 'government energy relief' for a processing fee. Facts that change everything: LIHEAP is real and free to apply (Cook County via CEDA + community action agencies + 211); the honest number is the one on his actual bill; the utility itself offers FREE deferred payment plans, budget/level billing, PIPP, and hardship help; Illinois winter shutoff protections / cold-weather rules can stop a disconnection; a doctor's medical certificate can delay a shutoff; ICC + Citizens Utility Board (CUB) are free consumer helps; real utilities never demand gift cards/prepaid/crypto/wire and never threaten shutoff within the hour. Scam spine: UTILITY DISCONNECTION PHONE IMPOSTER (pay now with gift/prepaid card or power cut in 30 min -- #1 utility scam), FAKE ENERGY-GRANT ADVANCE-FEE SCAM (processing/activation fee to 'release' assistance), SUPPLIER SLAMMING / doorstep-robocall SWITCH scam, FAKE LIHEAP APPLICATION-FEE / IMPOSTER-AGENCY scam, and OVERPAYMENT / FAKE-REFUND scam. Flat rule stated TWICE + SEPARATE caution that LIHEAP/CEDA/211/utility hardship programs/ICC/CUB are NOT scams. Dignity-never-deficit (fixed income run over by winter rates is arithmetic, not a character verdict; asking for help is responsible, not begging). AI quiet-helper/augment-not-replace stated with compliance TWICE (general navigation, NOT legal/financial advice, NOT a ruling on what he qualifies for/owes; verify with utility + real agency; never gift cards, never upfront fee, never a 30-min threat). Rotated to a MAN age 61 off #248's woman 52; distinct from #247's naturalizing man (57) and #246's first-gen college mother (44). Opens a WHOLLY NEW energy-crisis domain distinct from medical debt (#248), citizenship (#247), college aid (#246), eviction (#245), long-term care (#244), and every prior housing/tax/care/business/benefits domain. Serves Plug AI community + faith-community + senior + fixed-income + working-family + financial-literacy + digital-literacy + Get-Skilled pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-30-utility-shutoff-heat-electric-liheap-energy-assistance-free-help-ceda-winter-moratorium-payment-plan-disconnection-imposter-gift-card-fake-energy-grant-supplier-slamming-scam-ministry.md. PRIOR (#248): medical debt / hospital bills / charity care (woman 52) + free financial counselor/charity care/itemized bill + Medicaid + patient advocate + debt-relief fee mill / collections gift-card imposter / phantom-bill / advance-fee grant / debt-settlement mill scam. PRIOR (#247): citizenship / naturalization (man 57) + nonprofit legal aid/BIA-accredited rep + free English/civics classes + uscis.gov + fee-waiver truth + notario fraud / guaranteed-citizenship fee / ICE-USCIS phone imposter / fake-program fee / document-mill scam. PRIOR (#246): college financial aid / FAFSA / first-gen college (woman 44) + free counselor/TRIO/financial aid office + FAFSA-is-free truth + Pell-Grant-not-loans + fee-consultant/scholarship-release-fee/studentaid-phishing/loan-forgiveness/guaranteed-match scam. The plug is in."
runs_completed: 248
items_processed: 373
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
