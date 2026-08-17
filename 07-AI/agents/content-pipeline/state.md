---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-17T18:35:00Z"
current_task: "Generated LinkedIn post #204 -- NEW lane: the student-loan / income-driven-repayment / loan-forgiveness-scam ministry. A WOMAN, 26, the first in her family to ever finish college, back home in the south suburbs working an entry-level nonprofit/care job, frozen at a federal student-loan payment she is sure she cannot make and certain her only options are pay-in-full or default -- not knowing income-driven repayment can lower it (sometimes to zero), that her public-service job might count toward PSLF forgiveness, that getting out of/avoiding default is free, that all of it is free at studentaid.gov and through her servicer -- while "forgiveness" robocalls, upfront/monthly-fee "debt relief" and "enrollment" companies, and FSA-ID-phishing con artists hunt her. Doors (hedged, none ranked): income-driven repayment; forgiveness (PSLF/teacher/others); get out of/avoid default (consolidation, rehabilitation, deferment, forbearance); understand the loans (federal vs private, the servicer, deferment vs default, all free at studentaid.gov); free help to navigate (studentaid.gov, servicer, nonprofit counselor, school financial aid); the shame + fear (faith, mentor, 211, 988). Flat rule: managing + applying is always free, ED + servicer never charge to lower a payment or forgive loans and never cold-call to enroll, no one legitimate needs your FSA ID password. AI held in quiet-helper mode (explains the words, helps her find her servicer + reach studentaid.gov herself, reads the notice + drafts the questions, names the scam -- does NOT enroll her or decide eligibility, is NOT ED/servicer/lawyer/financial advisor, never fed FSA ID password/full SSN/logins). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a WOMAN off the #203 man 45; centers a YOUNG FIRST-GEN COLLEGE GRAD (26); new system distinct from the SNAP #193 -> disability #203 run. Saved to output/linkedin-2026-08-17-student-loans-forgiveness-repayment-scam-ministry.md. PRIOR (#203): disability/SSDI/SSI -- skilled-labor man 45. PRIOR (#202): housing/eviction -- single mother woman 31. The plug is in."
runs_completed: 204
items_processed: 329
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
