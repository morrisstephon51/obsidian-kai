---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-31T16:31:00Z"
current_task: "Generated LinkedIn post #254 -- WHOLLY NEW DOMAIN: SNAP / FOOD ASSISTANCE / LINK-EBT / FOOD PANTRIES / SENIOR MEALS for a grandmother of 68 in the south suburbs raising her grandkids on a fixed income, quietly skipping her own meals so the children eat. Truths that change everything: food help is real and built for exactly this (SNAP -- the Illinois LINK card -- plus free food pantries and free senior meal programs), applying is FREE (Illinois DHS at abe.illinois.gov / ABE portal or a Family Community Resource Center, with free application help from the Greater Chicago Food Depository + SNAP outreach partners), DHS NEVER texts or calls to ask for her LINK card number and PIN and never charges a fee to keep benefits, and NO ONE real charges money, gift cards, or a verification fee to sign her up or protect her food benefits. Doors: free ABE application / FCRC; free Food Depository SNAP application help; free food pantry for groceries today; AgeOptions (Area Agency on Aging, suburban Cook County) senior congregate + home-delivered meals; 2-1-1; check LINK balance safely via official ConnectEBT app / number on card + report skimmed benefits to IDHS. Scam spine: EBT/LINK SKIMMING & CLONING, FAKE RECERTIFICATION/VERIFY-YOUR-LINK PHISHING TEXT/CALL, BENEFIT-THEFT GIFT-CARD IMPOSTER, PAY-A-FEE/EXPEDITE/GET-MORE-BENEFITS ADVANCE-FEE, and FAKE SNAP APPLICATION WEBSITE. Flat rule stated TWICE + SEPARATE caution that DHS/ABE, the FCRC, the Greater Chicago Food Depository, food pantries, AgeOptions, 2-1-1, and the official ConnectEBT line are NOT scams. Dignity-never-deficit (a grandmother who worked her whole life and now raises a second generation is not a burden and not a beggar; needing food help is a bridge she paid into, not failure). AI quiet-helper/augment-not-replace with compliance TWICE (explains whether she may qualify, how to start ABE, finds nearest FCRC/pantry/senior meal site + hours, documents to bring, safe balance check; does NOT submit the application, decide eligibility, or promise an amount, never hands over card number/PIN/SSN, not a substitute for IDHS or a real caseworker; verify with IDHS/FCRC). Rotated to a WOMAN age 68 off #253 man 29; distinct from #252 woman 39, #251 man 46, #250 woman 34, #249 man 61, #248 woman 52. WHOLLY NEW food-security/nutrition-benefits domain distinct from expungement/reentry (#253), tax/refund (#252), disability/SSDI (#251), job search (#250), utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245). Serves Plug AI community + faith-community + working-family + senior + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-31-snap-food-assistance-link-ebt-free-pantry-senior-meals-skimming-phishing-benefit-theft-scam-ministry.md. PRIOR (#253): expungement/record sealing/reentry (man 29). PRIOR (#252): free tax filing/EITC/CTC/VITA (mother 39). PRIOR (#251): SSDI/SSI (tradesman 46). The plug is in."
runs_completed: 253
items_processed: 378
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
