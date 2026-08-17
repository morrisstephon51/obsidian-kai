---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-16T17:45:00Z"
current_task: "Generated LinkedIn post #200 (milestone) -- the IMMIGRATION / CITIZENSHIP / NOTARIO-FRAUD ministry: the week a young lawful permanent resident finally decides she is ready to apply for citizenship and, instead of real help, walks into a storefront with a 'notario publico' / 'immigration consultant' sign -- a man who is NOT a lawyer -- who charges her hundreds she cannot spare to fill out the wrong form, invent an answer, miss a deadline, and quietly wreck a case a real accredited nonprofit would handle free or nearly free, while the DOJ-accredited help she has never heard of sits a few miles away and the USCIS forms he is selling are free at uscis.gov. Doors: DON'T LET A FORM OR DEADLINE DECIDE IT BLIND (get it checked first; deadline-sensitive); REAL ACCREDITED HELP (a licensed immigration attorney or a DOJ-accredited representative at a recognized organization, plus nonprofit immigration legal aid, law-school clinics, legal aid -- free/low-cost and legally allowed to represent her, unlike the notario); UNDERSTAND THE OPTION (naturalization, green card renewal, adjustment of status, family petition, DACA renewal, work permit, fee waiver); HELP SHE MAY QUALIFY FOR (USCIS fee waivers/reductions, free citizenship/civics/ESL classes; eligibility decided by USCIS); SUPPORT FOR THE FEAR (trusted community org, know-your-rights, faith, 211, 988 if heavy); CHURCH BENEVOLENCE + 211. Scam weighted for THIS barrier: NOTARIO FRAUD (a 'notario' is a lawyer in many home countries but NOT in the US -- unlicensed practice of immigration law can file wrong/fraudulent applications, miss deadlines, take her money, trigger denial or removal); GUARANTEE/FEE scams ('guaranteed green card/approval,' visa-lottery fraud, selling the free USCIS forms); GOVERNMENT-IMPOSTER PHISHING (fake USCIS/ICE calls/texts demanding gift cards, wire, or her A-number/SSN/bank info to 'fix your status'/'stop your deportation'); DOCUMENT/IDENTITY theft. Flat rule: real immigration legal help comes only from a licensed attorney or a DOJ-accredited representative at a recognized organization, the forms are free at uscis.gov, a notario is not a lawyer, no real agency demands gift cards or threatens instant deportation by phone, never hand over originals/A-number/payment to anyone who can't prove in writing they are licensed/accredited. QUIET-HELPER + augment-not-replace: AI explains the words in plain language and across the language barrier, helps her understand a notice/form, compare a free accredited nonprofit vs a paid notario, gather/organize her OWN documents, and study for the civics test -- but does NOT give legal advice, does NOT decide her eligibility or what to file, does NOT act as her legal representative, is NOT USCIS/an attorney/an accredited rep, and must NEVER be fed her A-number, full SSN, or original document details. NEW system (immigration, not US federal benefits), distinct from the recent debt/bill/benefits run (SNAP #193, funeral #194, utility #195, medical debt #196, auto #197, IRS #198, veterans #199). NEW persona rotated off the run (woman 63 #190 ... man 34 #199): a WOMAN, 29, a first-generation immigrant and home health aide (community-health-worker tie-in), a lawful permanent resident for years now eligible to naturalize, English her second language, exhausted and afraid, with a notario storefront down the block. Rotates gender back to a WOMAN off the man (#199) and centers a YOUNG WORKING FIRST-GEN IMMIGRANT in a different system and a different barrier (language + fear + unlicensed practice of law). Dignity, never deficit (PULSE guard vs she-should-know-English / she's-cutting-a-line / should've-hired-a-lawyer / it-can't-be-that-risky / just-fill-it-out-yourself). Core reframe: the woman across town had the same storefront and fee, but a friend at church said 'he is not a lawyer, the real help is free, let me take you there,' so a DOJ-accredited rep checked and filed her citizenship application with a fee waiver and she took the oath -- while the woman in the pew almost paid a notario to file the wrong thing and endanger the case she waited years for. Compliance TWICE in-body -- general navigation, NOT legal advice, NOT an endorsement, NOT a determination of her status or eligibility; immigration law is complex and case-specific and outcomes belong to USCIS/the courts/the law; verify with a licensed attorney or a DOJ-accredited rep at a recognized organization, uscis.gov, and 211; never put an A-number/SSN into a public AI tool or hand originals to a notario. Did NOT rank any door, did NOT promise any outcome, did NOT assert any rule/timeline/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-16-immigration-citizenship-notario-fraud-ministry.md. PRIOR (#199): veterans / VA disability -- young Army veteran man 34. PRIOR (#198): tax / IRS back taxes -- working woman 47. The plug is in."
runs_completed: 200
items_processed: 325
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
