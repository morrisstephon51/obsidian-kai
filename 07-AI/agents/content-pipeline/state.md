---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-14T23:05:00Z"
current_task: "Generated LinkedIn post #190 -- the PRESCRIPTION / MEDICATION-AFFORDABILITY ministry (patient-assistance programs, community-health-center & sliding-scale/340B pharmacies, generics & 90-day supplies, discount comparison, Medicare Extra Help / Low-Income Subsidy, insulin affordability programs, and the flat safety rule \"never split, skip, or stop your medicine on your own to save money\"), a NEW lane: the recurring monthly life-or-death cost of the pills and insulin themselves. Distinct from medical-bills (a hospital/ER bill already incurred, charity care after the fact) and from health-coverage enrollment (getting COVERED) -- #190 is the ongoing cost of the medicine, and the quiet, dangerous thing people do when they cannot afford it: rationing (cutting pills in half, skipping doses before payday, stretching insulin past empty). QUIET-HELPER + augment-not-replace: AI explains generic / therapeutic alternative / 90-day supply / patient-assistance program / copay card / sliding-scale / 340B / formulary / Extra Help in plain words, helps her write the exact questions for her doctor and pharmacist, helps her find the health center and free clinic and the real official program -- but does NOT tell her to split/skip/stop any medicine (doctor + pharmacist decide), does NOT diagnose, does NOT give medical advice, does NOT replace her doctor/pharmacist/health center, and must NEVER be fed her SSN, Medicare/insurance number, medical records, or account numbers. NEW persona rotated off the recent run (housekeeping woman 52 #185 ... young man 28 #186 ... young mother 34 #187 ... grandmother 72 #188 ... working man 57 #189): a WOMAN, 63, still working (home health aide + part-time school-cafeteria worker) with diabetes and high blood pressure, quietly splitting pills, skipping doses, and stretching insulin to reach payday, too proud and private to tell anyone she cannot afford her medicine. Rotates gender back to a WOMAN off the man (#189) and centers a still-WORKING woman (63) caught by chronic-illness medication cost -- distinct from the young mother (34 #187), grandmother (72 #188), and housekeeping woman (52 #185). Dignity, never deficit (PULSE guard vs she-should-budget-better / she-is-being-dramatic / just-take-the-generic): she is not careless and not helpless -- rationing heart medicine or insulin can land her in the ER or the grave; the problem is not her budgeting, it is that nobody walked her to the doors. Doors, durable/hedged/routed, none ranked: (1) her DOCTOR (generics, therapeutic alternative, 90-day supply, simplify; NEVER split/skip/stop on her own -- a medical decision, deadly with insulin/heart/BP). (2) her PHARMACIST (cash vs insurance price, discount programs, cheaper pharmacies). (3) manufacturer PATIENT-ASSISTANCE PROGRAMS + copay cards (free to apply via official maker sources). (4) COMMUNITY HEALTH CENTERS / FQHCs with sliding-scale (340B) pharmacies. (5) DISCOUNT / price-comparison tools -- but never enter SSN/Medicare/insurance ID/bank account to unlock a price. (6) Medicare EXTRA HELP / Low-Income Subsidy for Part D, else the health-coverage door. (7) INSULIN-specific programs and caps. (8) 211/211.org, free and charitable clinics/pharmacies. Scam/caution weighted for THIS barrier: fake prescription-discount-card mailers/sites harvesting a Medicare number/insurance ID/SSN, we-will-get-your-meds-free outfits charging upfront, unlicensed online pharmacies selling counterfeit drugs -- the truth that legitimate assistance is free to apply, a real discount card never needs an SSN or bank account, and prescription meds should never be bought from an unverified online seller. Compliance TWICE in-body -- general navigation, NOT medical advice, NOT an endorsement; never split/skip/stop a prescribed medicine to save money without your doctor/pharmacist; AI can be confidently wrong, verify with your doctor, pharmacist, and the official Medicare.gov / SSA / manufacturer sources; never put an SSN, Medicare/insurance number, medical records, or account numbers into a public AI tool; legitimate assistance is free and no honest program charges upfront. Core reframe: the woman across town had a daughter who caught her splitting pills and said there-is-a-program-for-this, called the community health center, walked her through the manufacturer program -- now she takes her medicine exactly as prescribed; the woman in the pew never knew, kept splitting and stretching, and ended up in the ER -- not less careful, just never told the doors were there. DELIBERATELY did NOT rank any program/pharmacy/tool/health center, did NOT promise she qualifies or will pay any particular price, and did NOT assert any specific dollar amount, insulin cap, income limit, or eligibility rule as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intake routing and the Enrollment Funnel. Saved to output/linkedin-2026-08-14-prescription-medication-affordability-ministry.md. PRIOR (#189): disability-benefits SSDI/SSI -- working man 57. PRIOR (#188): estate-planning/wills -- grandmother 72. PRIOR (#187): special-education/IEP -- young mother 34. The plug is in."
runs_completed: 190
items_processed: 315
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
