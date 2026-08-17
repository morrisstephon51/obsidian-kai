---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-17T00:00:00Z"
current_task: "Generated LinkedIn post #201 -- the JOB-LOSS / UNEMPLOYMENT / REEMPLOYMENT-SCAM ministry: the week an older worker is laid off after thirty years at the same plant and, instead of the help he earned, sits ashamed at the kitchen table sure he is too old to start over -- not knowing the unemployment insurance he paid into for three decades is his to file, that free reemployment help (American Job Centers, Illinois workNet, dislocated-worker services, career coaching, funded WIOA retraining/certifications) exists a few miles away, and that no real employer asks you to pay to work -- while job scams, fake recruiters, and pay-to-work schemes hunt him the moment he applies. Doors: FILE FOR WHAT YOU EARNED (unemployment insurance; deadline-sensitive, eligibility decided by the state); REAL FREE REEMPLOYMENT HELP (American Job Centers / Illinois workNet / dislocated-worker services / funded WIOA retraining + resume and interview help); UNDERSTAND THE OPTIONS (unemployment insurance, dislocated-worker programs, WIOA, registered apprenticeships, Trade Adjustment Assistance); HELP HE MAY QUALIFY FOR (SNAP/utility/medical bridge, COBRA/marketplace health coverage, retraining scholarships); SUPPORT FOR THE SHAME (faith, a trusted friend, 211, 988 if heavy); CHURCH BENEVOLENCE + 211. Scam weighted for THIS barrier: JOB/TASK scams (fake remote-job & 'we saw your resume' offers, fake-check overpayment / package-reshipping mule schemes, pay-for-training/equipment/background-check/starter-kit up front, MLM dressed as a job); RECRUITER/OFFER phishing (never video-calls, moves to a chat app, asks for SSN/bank/direct-deposit/ID before a real job); UNEMPLOYMENT-IMPOSTER phishing (fake state-workforce texts/sites demanding a fee or his login/SSN/bank to 'release your benefits'). Flat rule: a real employer never asks you to pay to get a job, never sends a check to deposit-and-wire-back, never needs your bank login or full SSN before a real offer; unemployment is filed free through the official state agency; no legitimate program charges to unlock a benefit. QUIET-HELPER + augment-not-replace: AI explains unemployment insurance / dislocated worker / WIOA / American Job Center / Illinois workNet / apprenticeship / Trade Adjustment Assistance in plain words, rewrites 30 years of skill into a machine-readable resume, coaches interviews, and names the scam -- but does NOT file his claim, does NOT decide eligibility or which program, is NOT the state agency/an employer, and must NEVER be fed his full SSN, bank/direct-deposit details, or account logins. NEW system (workforce/reemployment), distinct from the recent benefits/debt/immigration run (SNAP #193, funeral #194, utility #195, medical debt #196, auto #197, IRS #198, veterans #199, immigration/notario #200). NEW persona rotated off the run (woman 63 #190 ... woman 29 #200): a MAN, 58, thirty years at a plant/warehouse closed out from under him, proud, ashamed to job-hunt at his age, sure he is too old and too far from the computer, unaware the unemployment is his and free retraining exists. Rotates gender back to a MAN off the woman (#200) and centers an OLDER DISPLACED WORKER (58) in a different system and a different barrier (age + shame + tech-distance + predatory job scams). Dignity, never deficit (PULSE guard vs he-should-have-saved / should-have-reskilled / too-old-to-retrain / just-get-any-job / should-already-know-computers). Core reframe: the man across town was laid off from the same kind of plant, same age, same shame, but a friend at church said 'the unemployment is yours, you paid into it, and there is a place that retrains you for free, let me take you there,' so he filed, walked into an American Job Center, got a funded certification, and is working again -- while the man in the pew almost cashed a scammer's fake check and almost left the benefit he earned unclaimed. Compliance TWICE in-body -- general navigation, NOT legal/financial/career-guarantee advice, NOT a determination of eligibility or which program; eligibility/amounts/timelines/outcomes decided by the state workforce agency and the programs under their rules, not a machine or a guess; verify with Illinois workNet, an American Job Center, the official state unemployment agency, and 211; never put a full SSN, bank login, or direct-deposit info into a job posting or public AI tool. Did NOT rank any door, did NOT promise a job/benefit/approval, did NOT assert any rule/amount/timeline/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to JobScout routing and the Enrollment Funnel. Saved to output/linkedin-2026-08-17-job-loss-unemployment-reemployment-scam-ministry.md. PRIOR (#200): immigration / citizenship / notario fraud -- young first-gen home health aide woman 29. PRIOR (#199): veterans / VA disability -- young Army veteran man 34. The plug is in."
runs_completed: 201
items_processed: 326
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
