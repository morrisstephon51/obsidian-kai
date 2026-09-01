---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-09-01T00:00:00Z"
current_task: "Generated LinkedIn post #257 -- WHOLLY NEW DOMAIN: STUDENT LOAN REPAYMENT / FORGIVENESS / INCOME-DRIVEN REPAYMENT (IDR) / PUBLIC SERVICE LOAN FORGIVENESS (PSLF) for a first-generation college MAN of 41 in the south suburbs who went back to school to build something better, now carries a federal student-loan balance that feels like a permanent wall, has quietly stopped opening the letters, and does not know the truths that change everything: lowering the payment and even earning forgiveness are real and built for exactly this (Income-Driven Repayment via studentaid.gov + his official servicer, where a payment can drop to what he can afford and sometimes to $0; Public Service Loan Forgiveness if he works full-time for government, a public school, a hospital, or a qualifying nonprofit), applying is FREE (studentaid.gov, his servicer, free nonprofit credit/student-loan counselors + legal aid), the Department of Education/his servicer NEVER demand gift cards or a fee to enroll and never text for his FSA ID or SSN, and NO ONE real charges to lower his payment, consolidate, or guarantee forgiveness. Doors (hedged, none ranked): studentaid.gov + official servicer (free); IDR (income-set payment, as low as $0); PSLF (free employment certification); free nonprofit counselor (NFCC)/legal aid; 2-1-1; verify via studentaid.gov + servicer, guard FSA ID + SSN. Scam spine: FORGIVENESS/ENROLLMENT ADVANCE-FEE, FAKE TOTAL-CANCELLATION ACT-NOW ROBOCALL/TEXT, IMPOSTER SERVICER/DEPT-OF-ED GIFT-CARD-OR-PAYMENT, FAKE STUDENT-AID SITE/FSA-ID PHISHING, and DEBT-RELIEF/CONSOLIDATION COMPANY THAT TAKES OVER HIS PAYMENTS. Flat rule stated TWICE + SEPARATE caution that studentaid.gov/Federal Student Aid, his servicer, IDR/PSLF, nonprofit counselors/legal aid, and 2-1-1 are NOT scams. Dignity-never-deficit (going back to school and carrying the debt is not failure; IDR/PSLF were built for exactly this borrower) + AI quiet-helper/augment-not-replace with compliance TWICE (explains IDR vs PSLF, whether his job may qualify, how to start at studentaid.gov, find a free counselor + hours, which income docs to gather; does NOT enroll, decide eligibility, or promise forgiveness/a payment, never handles FSA ID/SSN, not a substitute for studentaid.gov or his servicer; verify with studentaid.gov + servicer). Rotated to a MAN age 41 off #256 woman 52; distinct from #255 man 33, #254 woman 68, #253 man 29, #252 woman 39, #251 man 46, #250 woman 34. WHOLLY NEW student-debt domain (existing federal loans / repayment / forgiveness) distinct from college financial aid (#246, getting INTO school), health insurance enrollment (#256), child care (#255), SNAP/food (#254), expungement (#253), tax (#252), disability (#251), job search (#250), utility (#249), medical debt (#248), citizenship (#247), eviction (#245). Serves Plug AI community + faith-community + first-gen-student + working-family + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-student-loan-repayment-forgiveness-idr-pslf-studentaid-forgiveness-fee-fake-cancellation-robocall-imposter-servicer-fsa-phishing-debt-relief-takeover-scam-ministry.md. PRIOR (#256): health insurance enrollment / Medicaid / Get Covered Illinois / ACA (uninsured working woman 52). PRIOR (#255): child care / CCAP / Head Start / free preschool (single working father 33). PRIOR (#254): SNAP / food / LINK-EBT (grandmother 68). The plug is in."
runs_completed: 256
items_processed: 381
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
