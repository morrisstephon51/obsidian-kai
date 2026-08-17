---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-17T14:30:00Z"
current_task: "Generated LinkedIn post #203 -- the DISABILITY / SSDI / SSI / DISABILITY-CLAIM-SCAM ministry: the year a man who worked with his body for twenty-two years finally cannot anymore, his back gives out, the job goes with it, and instead of the help he already paid for he sits in a recliner he can barely rise from -- certain disability is welfare for other people, too ashamed of no longer providing to say a word -- not knowing SSDI is insurance he bought with every paycheck, that SSI exists for exactly this, that most first claims are denied and the appeal is where people win, that applying is free and a real rep is paid only if you win -- while fake SSA-agent calls, upfront-fee disability-advocate companies, and guaranteed-approval con artists hunt him the moment he starts looking. Doors: SSDI (insurance he already paid for, not welfare; eligibility decided by SSA + medical evidence); SSI (disability + limited income/resources); UNDERSTAND THE PROCESS (application, medical records, most first claims denied, reconsideration + hearing, strict deadlines); HELP TO APPLY (SSA office, free legal aid, accredited reps paid only if you win + capped from back pay, never upfront); HELP WHILE HE WAITS (SNAP, Medicaid, utility help, food pantry, church benevolence); THE IDENTITY + SHAME (faith, trusted friend, 211, 988). Scam weighted for THIS barrier: SSA/GOVERNMENT-IMPOSTER calls+texts (SSN suspended, pay by gift card/wire/crypto, arrest threats -- SSA does not call to threaten or demand payment); UPFRONT-FEE disability-advocate companies (large fees to handle/guarantee -- real reps paid only if you win + capped from back pay); ADVANCE-FEE/GUARANTEED-APPROVAL + fake-back-pay scams. Flat rule: applying is free, SSA never demands gift cards/wires, a real rep is paid only if you win + capped from back pay, no one can guarantee approval. QUIET-HELPER + augment-not-replace: AI explains SSDI/SSI/disability-determination/denial/reconsideration/hearing/back-pay/accredited-rep in plain words, gathers + orders medical records + work history, reads the denial + finds the appeal deadline, drafts a function report / appeal letter, names the scam -- but does NOT decide disability, does NOT represent him at a hearing, does NOT determine eligibility, is NOT SSA/a doctor/a lawyer/the judge, and must NEVER be fed his full SSN, bank/direct-deposit details, or logins. NEW system (disability/SSDI/SSI), distinct from the recent benefits/debt/immigration/workforce/housing run (SNAP #193 ... job-loss #201, housing/eviction #202). NEW persona rotated off the run (woman 31 #202): a MAN, 45, skilled-labor/construction worker of twenty-two years whose back gave out, out of work, sure disability is charity too proud to take, unaware SSDI is insurance he already bought -- rotates gender back to a MAN and centers a MIDDLE-AGED SKILLED-LABOR MAN whose identity was his body, in a different system and barrier (body that quit + provider identity in ruins + long denial-and-appeal process + shame + disability-claim scams). Dignity, never deficit (PULSE guard vs he-should-have-saved / should-have-gone-to-college / should-get-a-desk-job / should-just-push-through / disability-is-welfare / he's-giving-up). Core reframe: the man across town blew out the same back, carried the same shame, but a friend at church said that's not welfare, you paid into it every check for twenty-two years, apply, don't pay anybody upfront, and when they deny you the first time -- because they usually do -- you appeal, so he applied, kept his records, got an accredited rep on contingency, appealed, and got approved -- while the man in the pew almost bought gift cards for a fake SSA agent and almost gave up after the first no. Compliance TWICE in-body -- general navigation, NOT legal/medical/financial advice, NOT a determination of disability or eligibility; disability/eligibility/timelines/outcomes decided by SSA, the medical evidence, and the law, not a machine or a guess; verify with SSA, free legal aid, and an accredited representative; never put a full SSN, bank login, or direct-deposit info into a public AI tool, and never send gift cards/wires/upfront fees. Did NOT rank any door, did NOT promise approval/back-pay/timeline, did NOT assert any rule/amount/deadline/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to JobScout routing and the Enrollment Funnel. Saved to output/linkedin-2026-08-17-disability-ssdi-ssi-benefits-scam-ministry.md. PRIOR (#202): housing / eviction / rental-assistance scams -- working single mother woman 31. PRIOR (#201): job loss / unemployment / reemployment scams -- older displaced worker man 58. The plug is in."
runs_completed: 203
items_processed: 328
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
