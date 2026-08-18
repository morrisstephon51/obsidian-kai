---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-18T08:26:00Z"
current_task: "Generated LinkedIn post #207 -- NEW lane: the workers' compensation / workplace-injury ministry. A MAN, 51, a warehouse/forklift worker who wrenched his back and shoulder lifting -- told by his supervisor to 'walk it off' and 'not make it a thing,' now paying cash for his own painkillers and a doctor visit and clocking in hurt every morning -- certain that reporting the injury means losing the job he needs and that 'guys like me don't win those' -- not knowing that reporting a workplace injury is generally his right (with short deadlines), that firing him for filing a legitimate claim is in many cases illegal, that medical care and a share of lost wages for a work injury are exactly what workers' comp exists to cover, and that the help to understand his rights is free -- while 'settlement advance / lawsuit loan' sharks, upfront 'filing fee / claim service' con artists, and SSN-phishing 'claim processors' hunt a frightened injured worker who thinks the system was built to say no. Doors (hedged, none ranked): report the injury (generally a right, short deadlines, retaliation often illegal, confirm with state agency/legal aid); medical care covered (comp meant to cover work-injury treatment, should not pay cash/burn own insurance); lost wages (temporary wage replacement may apply, state rules); free help / know your rights (state comp board, legal aid, worker centers; many attorneys on contingency, no upfront fee; understand the fee first); if retaliated against (may be unlawful, document dates/what/who, get to legal aid); the fear + pride (faith, mentor, 211, 988). Flat rule: reporting is your right, real help is free or a regulated contingency with no upfront cash, and no one honest offers a high-interest loan against your settlement or demands your SSN and a payment to 'process' your claim. Held a SEPARATE caution: a real official notice (state comp board / employer insurer with a real deadline to respond, appeal, or attend an exam) is NOT a scam call -- do not ignore genuine paperwork with a real clock. AI in quiet-helper mode (explains the words, finds the state agency/legal aid/worker center to reach himself, helps him understand the deadline + what to document, reads a claim letter/denial, names the scam -- does NOT file, decide/value his claim, or tell him to settle; is NOT a lawyer/doctor/adjuster; never fed full SSN/bank login/account numbers). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a MAN off the #206 woman 39; centers a MID-LIFE MANUAL LABORER HURT ON THE JOB AND AFRAID TO REPORT (51). Deliberately distinct from disability/SSDI (#203 = the body that can no longer work) and medical debt (#196 = the bill already owed) -- this is a work injury RIGHT NOW and the no-fault system meant to cover it. Saved to output/linkedin-2026-08-18-workers-compensation-workplace-injury-scam-ministry.md. PRIOR (#206): health coverage/Medicaid/ACA-marketplace enrollment -- working mother uninsured after a job loss, woman 39. PRIOR (#205): debt collection/collector harassment/know-your-rights -- older near-retirement man 63. PRIOR (#204): student loans/IDR/forgiveness -- first-gen college graduate woman 26. The plug is in."
runs_completed: 207
items_processed: 332
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
