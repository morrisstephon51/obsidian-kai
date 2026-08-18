---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-17T19:05:00Z"
current_task: "Generated LinkedIn post #205 -- NEW lane: the debt-collection / collector-harassment / know-your-rights-scam ministry. A MAN, 63, a few years short of retirement, hounded by relentless collection calls over a decade-old debt he cannot confirm is his, a caller swearing a warrant is out and he will be arrested today unless he pays now, terrified for the Social Security check he is about to draw and the house he has nearly paid off -- not knowing no one is jailed for a consumer debt, that a real collector must prove the debt in writing before he pays, that old debt may be past the statute of limitations or not even his (phantom/zombie debt), that Social Security is generally shielded from garnishment, and that the help is free -- while fake-collector arrest scams, gift-card/wire/crypto demands, and SSN-phishing con artists hunt him. Doors (hedged, none ranked): know your rights (FDCPA -- no arrest threats, harassment, or lies; cease contact in writing); make them prove it (debt validation before paying, free); is it yours/collectible (statute of limitations, mistaken identity, phantom debt, restart-the-clock caution); protect what is protected (Social Security/federal benefits generally garnishment-shielded); free help (legal aid/senior legal services, nonprofit credit counselor, CFPB, FTC, state AG); the shame + fear (faith, mentor, 211, 988). Flat rule: you cannot be arrested for a consumer debt, a real collector must prove it in writing and never threatens jail, and no honest debt is paid by gift card/wire/crypto to a caller. Held a SEPARATE caution: a real court summons is NOT a scam call -- if actually sued, respond and get to legal aid fast. AI in quiet-helper mode (explains the words, drafts the validation + cease-contact letters, helps tell scam from summons, reads the letter/papers, names the scam -- does NOT contact the collector or decide whether the debt is valid/his/time-barred, is NOT a lawyer/CFPB/credit counselor, never fed full SSN/bank login/account numbers). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a MAN off the #204 woman 26; centers an OLDER NEAR-RETIREMENT BORROWER (63). Saved to output/linkedin-2026-08-17-debt-collection-collector-harassment-rights-scam-ministry.md. PRIOR (#204): student loans/IDR/forgiveness -- first-gen college graduate woman 26. PRIOR (#203): disability/SSDI/SSI -- skilled-labor man 45. PRIOR (#202): housing/eviction -- single mother woman 31. The plug is in."forgiveness" robocalls, upfront/monthly-fee "debt relief" and "enrollment" companies, and FSA-ID-phishing con artists hunt her. Doors (hedged, none ranked): income-driven repayment; forgiveness (PSLF/teacher/others); get out of/avoid default (consolidation, rehabilitation, deferment, forbearance); understand the loans (federal vs private, the servicer, deferment vs default, all free at studentaid.gov); free help to navigate (studentaid.gov, servicer, nonprofit counselor, school financial aid); the shame + fear (faith, mentor, 211, 988). Flat rule: managing + applying is always free, ED + servicer never charge to lower a payment or forgive loans and never cold-call to enroll, no one legitimate needs your FSA ID password. AI held in quiet-helper mode (explains the words, helps her find her servicer + reach studentaid.gov herself, reads the notice + drafts the questions, names the scam -- does NOT enroll her or decide eligibility, is NOT ED/servicer/lawyer/financial advisor, never fed FSA ID password/full SSN/logins). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a WOMAN off the #203 man 45; centers a YOUNG FIRST-GEN COLLEGE GRAD (26); new system distinct from the SNAP #193 -> disability #203 run. Saved to output/linkedin-2026-08-17-student-loans-forgiveness-repayment-scam-ministry.md. PRIOR (#203): disability/SSDI/SSI -- skilled-labor man 45. PRIOR (#202): housing/eviction -- single mother woman 31. The plug is in."
runs_completed: 205
items_processed: 330
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
