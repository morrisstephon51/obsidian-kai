---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-31T21:33:00Z"
current_task: "Generated LinkedIn post #255 -- WHOLLY NEW DOMAIN: CHILD CARE ASSISTANCE / CCAP / HEAD START / FREE PRESCHOOL for a single working father of 33 in the south suburbs raising two little ones alone, turning down hours (nearly losing the job) because he cannot cover day care. Truths that change everything: child care help is real and built for exactly this (Illinois Child Care Assistance Program -- CCAP -- plus Head Start / Early Head Start and free state preschool), applying is FREE (through IDHS and the local Child Care Resource & Referral agency -- Illinois Action for Children in Cook County -- with free provider referrals + application help), IDHS/CCR&R NEVER text or call to demand a fee or gift cards to approve his case and never text for his SSN/case number, and NO ONE real charges money, gift cards, or a guaranteed-approval/verification fee to sign him up or protect his case. Doors: free CCAP application via IDHS + CCR&R / Illinois Action for Children (free referrals + help); Head Start / Early Head Start; Preschool for All / state pre-K; 2-1-1; verify provider license via IDHS child care licensing before any deposit. Scam spine: FAKE CHILD CARE SUBSIDY WEBSITE, GUARANTEED-APPROVAL/ADVANCE-FEE, IMPOSTER PAY-YOUR-COPAY/VERIFY-YOUR-CASE GIFT-CARD CALL/TEXT, PHANTOM DAY CARE / DEPOSIT, and FAKE PROVIDER-FEE/BACKGROUND-CHECK-FEE UPFRONT. Flat rule stated TWICE + SEPARATE caution that IDHS, the CCR&R / Illinois Action for Children, Head Start, Preschool for All, 2-1-1, and IDHS licensing are NOT scams. Dignity-never-deficit (a father raising two kids alone while working every shift is not a burden and not a failure; needing child care help to keep working is the whole point of the program). AI quiet-helper/augment-not-replace with compliance TWICE (explains whether he may qualify, how to start CCAP via CCR&R, find nearest CCR&R/Head Start/preschool + hours, documents to bring, safe license check; does NOT submit the application, decide eligibility, or promise an approval/copay, never hands over SSN/case number, not a substitute for IDHS or a real CCR&R caseworker; verify with IDHS/CCR&R). Rotated to a MAN age 33 off #254 woman 68; distinct from #253 man 29, #252 woman 39, #251 man 46, #250 woman 34, #249 man 61. WHOLLY NEW child-care/early-childhood domain distinct from SNAP/food (#254), expungement/reentry (#253), tax/refund (#252), disability/SSDI (#251), job search (#250), utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245). Serves Plug AI community + faith-community + working-family + working-parent + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-31-child-care-assistance-ccap-working-parent-free-ccrr-illinois-action-for-children-head-start-preschool-guaranteed-approval-fee-copay-gift-card-imposter-phantom-daycare-deposit-scam-ministry.md. PRIOR (#254): SNAP/food/LINK-EBT/pantry/senior meals (grandmother 68). PRIOR (#253): expungement/record sealing/reentry (man 29). PRIOR (#252): free tax filing/EITC/CTC/VITA (mother 39). The plug is in."
runs_completed: 254
items_processed: 379
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
