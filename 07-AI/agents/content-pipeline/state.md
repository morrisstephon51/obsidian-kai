---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-16T17:45:00Z"
current_task: "Generated LinkedIn post #199 -- the VETERANS / VA-DISABILITY ministry (the crisis the day a young veteran opens the brown VA envelope and reads that his disability claim was denied on part and lowballed on the rest, for injuries he earned in uniform, and within days a 'claims consulting' company is calling to promise a big rating and thousands in back pay if he signs over a cut of that money, while the free VA-accredited help he has never heard of sits unused a few miles away): DON'T ACCEPT A DENIAL AS FINAL (appeal rights + a deadline; the decision letter names the lanes -- supplemental claim, higher-level review, or a Board appeal); FREE VA-ACCREDITED HELP (a VSO through the county Veterans Assistance Commission, the state/county veterans office, VFW / American Legion / DAV, plus veterans law clinics & legal aid -- files & appeals free); UNDERSTAND THE CLAIM (service connection, the rating, the C&P exam, secondary conditions, the effective date -- see why he was denied & what evidence is missing); OTHER BENEFITS HE MAY BE OWED (VA health care, GI Bill, VR&E vocational rehab, TDIU -- eligibility decided by the VA); THE WEIGHT HE CARRIES (Veterans Crisis Line, dial 988 then press 1); CHURCH BENEVOLENCE + 211. Scam weighted for the VA claim: CLAIM SHARKS -- unaccredited 'claims consulting' firms taking an illegal cut of retroactive back pay or a monthly fee to 'maximize your rating,' when a VA-accredited VSO does it free and no one may legally charge to file an initial claim (parallel to the tax-relief pennies-on-the-dollar trap in #198, the title-loan trap in #197, the deferred-interest medical card in #196); PENSION POACHERS ('restructure your assets' for a fee, often harming the veteran); BENEFIT-BUYOUT / 'cash for your benefits' schemes (buy future disability payments at a brutal discount); and VA-IMPOSTER PHISHING ('your VA.gov account is locked / verify your benefits / release your back pay' texts, emails, and callers after his SSN, VA file number, or bank / direct-deposit info). QUIET-HELPER + augment-not-replace: AI explains service connection / a disability rating / a C&P exam / a secondary condition / an effective date / a supplemental claim / a higher-level review / TDIU / a VSO / VA accreditation in plain words and helps him read the decision letter, gather & organize his own service and medical records, draft his own personal / lay statement, and compare a free accredited VSO against a paid claim-shark -- but does NOT decide his rating, does NOT promise any rating or back pay, does NOT determine his service connection or eligibility, is NOT the VA / an accredited representative / a lawyer, and must NEVER be fed his SSN, VA file number, or bank / card numbers. NEW lane, distinct from the recent debt/bill/benefits run (SNAP #193, funeral #194, utility #195, medical debt #196, auto/car #197, IRS back taxes #198): this is VETERANS and a VA CLAIM. NEW persona rotated off the run (woman 63 #190 ... man 64 #191 ... woman 44 #192 ... man 49 #193 ... woman 56 #194 ... man 41 #195 ... woman 52 #196 ... man 38 #197 ... woman 47 #198): a MAN, 34, a post-9/11 Army veteran on a warehouse forklift job, married with two young kids, carrying a bad back, tinnitus, and sleepless nights, denied/lowballed on his VA claim, never heard the word 'VSO,' halfway to signing a claim-shark contract. Rotates gender back to a MAN off the woman (#198) and centers a YOUNG WORKING VETERAN (34) -- filling the young-adult gap in a recent run of fixed-income seniors (#190, 63; #191, 64), middle-aged women (#192, 44; #194, 56; #196, 52; #198, 47), and older working men (#193, 49; #195, 41; #197, 38) -- in an acute benefits-denial-and-scam emergency distinct in age, system, and barrier from every recent lane. Dignity, never deficit (PULSE guard vs he's-just-chasing-a-check / gaming-the-system / it-can't-be-that-bad / should-be-able-to-work / real-vets-don't-complain / should-have-documented-it-better). Core reframe: the veteran across town had the same brown envelope -- same partial denial, same lowball rating, same 'claims consulting' company promising to maximize it for a cut -- but a buddy at the VFW said a VSO does this free and it's illegal for that company to take a piece of your back pay, so he filed a supplemental claim with new evidence for free and kept every dollar of his back pay when the rating was corrected, while the man in the pew almost signed thousands to a shark. Compliance TWICE in-body -- general navigation, NOT legal advice, NOT medical advice, NOT an endorsement of any consultant/company/organization, and NOT a determination of his rating or eligibility; ratings, service connection, and eligibility belong to the VA and the law; verify at VA.gov, a VA-accredited VSO, the county Veterans Assistance Commission, the state/county veterans office, and 211; never put an SSN or VA file number into a public AI tool or hand it to a caller; real accredited help is free and no one may charge a percentage of back pay to file a claim. Did NOT rank any door, did NOT promise any rating/back pay, did NOT assert any rule/amount/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-16-veterans-va-disability-claims-ministry.md. PRIOR (#198): tax / IRS back taxes -- working woman 47. PRIOR (#197): car / auto-debt / repossession -- working father 38. The plug is in."
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
