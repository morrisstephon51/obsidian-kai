---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-14T18:35:00Z"
current_task: "Generated LinkedIn post #189 -- the DISABILITY-BENEFITS ministry (SSDI / SSI / the appeal ladder), a NEW lane: the door a working-age man walks through when his body gives out and he can no longer do the only work he has ever known. Distinct from unemployment insurance (#185, housekeeping woman 52 -- temporarily out of work but ABLE to work, actively looking): #189 is the opposite case -- a man who cannot work AT ALL because of a lasting medical condition, and does not know he may have EARNED Social Security Disability Insurance through decades of payroll taxes, or that Supplemental Security Income exists for those without enough work credits. Also distinct from health-coverage enrollment (getting COVERED) and from property-tax/estate (#184/#188, keeping/passing down a home) -- this is INCOME and dignity when the body can no longer earn it; and distinct from disability/special-needs #08-09 (a church VOLUNTEER carrying a benefits maze) -- #189 centers the disabled worker himself and his own claim. QUIET-HELPER + augment-not-replace: AI explains SSDI / SSI / work credits / onset date / listing of impairments / reconsideration / ALJ hearing in plain words, never the doctor, never SSA, never the one who decides whether he is disabled, never his representative. NEW persona rotated off the recent run (grandmother 72 #188 ... young mother 34 #187 ... young man 28 #186 ... housekeeping woman 52 #185 ... elder deacon widower 68 #184): a MAN IN HIS LATE FIFTIES (57) -- thirty-five years of warehouse/dock/factory work, a steady man in the pews, whose back, knees, and heart have given out, burning through savings and leaning on his wife's check, too proud to go on disability because he was raised to believe it is a handout. Rotates gender back to a MAN off the two women (#187, #188) and centers a WORKING-AGE man (57) forced out by his body -- distinct in age from the recent man (28 #186) and the retired deacon (68 #184). Dignity, never deficit (PULSE guard vs he should just get another job / disability is a handout / he is milking the system): he is not lazy and not gaming anything -- he worked harder and longer than most people ever will, his body is the thing that broke, and the benefit he is too proud to claim is money he already paid for with every paycheck of a 35-year working life. Doors, durable/hedged/routed, none ranked: (1) SSDI -- for workers who paid in enough and now cannot work due to a lasting medical condition (hedged; work credits/eligibility/medical determination decided by SSA, confirm at ssa.gov and with a real representative). (2) SSI -- for people with disabilities and very limited income/resources who may lack work credits (hedged; rules set by SSA). (3) the APPEAL ladder -- the first application is often denied; reconsideration, then an ALJ hearing where many finally win; do NOT quit at the first no (routed/hedged). (4) FREE and low-cost HELP -- legal aid, disability-rights orgs, and legitimate representatives paid only out of back benefits (capped by federal law), only if he wins, nothing up front (routed/hedged). (5) his own FACTS to line up (work history, conditions, doctors/clinics, meds, onset dates) WITHOUT feeding his SSN or medical records to a machine. (6) 211/211.org and the local Aging & Disability Resource Center / Area Agency on Aging. (7) Scam/caution weighted for THIS barrier: outfits promising we-will-get-you-approved for an upfront fee, guaranteeing approval, or pressuring him to sign over benefits / pay cash before anything happens -- the truth that applying with SSA is free, that legitimate representatives are paid only from back pay, only if he wins, capped by federal law, and that no honest person guarantees an approval or charges up front. AI does NOT decide whether he is disabled (SSA + his doctors do), does NOT fill out/submit the application, does NOT give legal/medical advice, does NOT replace SSA/doctor/legal aid/representative, and must NEVER be fed his SSN, medical records, or account numbers. Core reframe: the man across town -- same worn-out body, same 35 years -- had a brother-in-law who said that is not welfare, that is YOUR insurance, you paid into it every check; apply, and when they say no the first time you do not quit, you appeal, and legal aid will help you free; he applied, got denied, appealed, won at the hearing, and it steadied his whole house; the man in the pew never applied (too proud), gave up at the first they-deny-everybody, and burned through his savings, his wife's paycheck, and his dignity -- not lazier, just never told the door was his and the money already his. Compliance TWICE in-body -- general navigation, NOT an endorsement, NOT legal or medical advice; eligibility and the medical determination are SSA's to decide and AI can be confidently wrong, so verify at ssa.gov and with a real representative or free legal aid; never put an SSN, medical records, or account numbers into a public AI tool; applying is free and no honest person guarantees approval or charges up front. DELIBERATELY did NOT rank any attorney/representative/clinic, did NOT promise he qualifies or will be approved, and did NOT assert any specific current dollar amount, work-credit count, income/resource limit, or approval rate as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intake routing and the Enrollment Funnel. Saved to output/linkedin-2026-08-14-disability-benefits-ssdi-ssi-ministry.md. PRIOR (#188): estate-planning/wills/transfer-on-death -- grandmother 72. PRIOR (#187): special-education/IEP-504 -- young mother 34. PRIOR (#186): student-loan repayment -- young man 28. The plug is in."
runs_completed: 189
items_processed: 314
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
