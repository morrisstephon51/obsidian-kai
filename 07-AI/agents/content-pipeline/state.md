---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-31T21:40:00Z"
current_task: "Generated LinkedIn post #256 -- WHOLLY NEW DOMAIN: HEALTH INSURANCE ENROLLMENT / MEDICAID / GET COVERED ILLINOIS / ACA MARKETPLACE for an uninsured working woman of 52 in the south suburbs who stitches together part-time jobs with no insurance, skipping the doctor and rationing a prescription because she is sure coverage is out of reach. Truths that change everything: free/low-cost coverage is real and built for exactly this (Medicaid via IL HFS/IDHS through ABE, plus Get Covered Illinois -- the state official ACA Marketplace -- where premium tax credits can bring a plan to little/nothing), enrolling is FREE (state + certified Navigators/assisters + community health center/FQHC that also sees her on a sliding scale now), the state/Marketplace NEVER text/call demanding a fee or gift cards to keep coverage and never text for her SSN, and NO ONE real charges money/gift cards/enrollment/verification fees to sign her up. Doors: free Medicaid via HFS/IDHS/ABE; free enrollment via Get Covered Illinois with premium tax credits; free Navigator/counselor/CHW help; FQHC sliding-scale care + enrollment help now; 2-1-1; verify via Get Covered Illinois/HealthCare.gov/HFS. Scam spine: FAKE HEALTH PLAN/JUNK INSURANCE/DISCOUNT CARD, ADVANCE-FEE/ENROLLMENT-FEE, IMPOSTER VERIFY-YOUR-COVERAGE/PAY-TO-KEEP-MEDICAID GIFT-CARD CALL/TEXT, FAKE MARKETPLACE/MEDICAID WEBSITE, and LIMITED-TIME/FINAL-NOTICE HEALTH-INSURANCE ROBOCALL. Flat rule stated TWICE + SEPARATE caution that HFS/IDHS/Medicaid, Get Covered Illinois, HealthCare.gov, Navigators/FQHCs, and 2-1-1 are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains whether she may qualify, how to start via Get Covered Illinois/ABE, find nearest Navigator/FQHC + hours, documents to bring; does NOT enroll, decide eligibility, or promise a plan/premium, never hands over SSN/bank number, not a substitute for the state or a real Navigator; verify with Get Covered Illinois/HFS). Rotated to a WOMAN age 52 off #255 man 33; distinct from #254 woman 68, #253 man 29, #252 woman 39, #251 man 46, #250 woman 34. WHOLLY NEW health-coverage-access domain (getting covered in the first place) distinct from medical debt (#248, existing bills), child care (#255), SNAP/food (#254), expungement (#253), tax (#252), disability (#251), job search (#250), utility (#249), citizenship (#247), college aid (#246), eviction (#245). Serves Plug AI community + faith-community + working-family + health-access + digital-literacy pillars AND BigHeart My Health My Power church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-31-health-insurance-enrollment-medicaid-get-covered-illinois-aca-marketplace-navigator-fqhc-free-coverage-junk-plan-fake-insurance-advance-fee-imposter-gift-card-verify-coverage-robocall-scam-ministry.md. PRIOR (#255): child care/CCAP/Head Start/free preschool (single working father 33). PRIOR (#254): SNAP/food/LINK-EBT/pantry/senior meals (grandmother 68). PRIOR (#253): expungement/record sealing/reentry (man 29). The plug is in."
runs_completed: 255
items_processed: 380
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
