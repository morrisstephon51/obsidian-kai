---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-19T06:30:00Z"
current_task: "Generated LinkedIn post #212 -- NEW lane: the utility-shutoff / energy-assistance (LIHEAP) ministry. A WOMAN, 58, on a tight fixed income (some part-time work, a small check, a grandchild or aging parent under her roof), opens the gas/electric bill in the August heat, sees a shutoff date and a number she cannot pay, and quietly starts rationing her own necessities to keep the power on -- not knowing that energy assistance (LIHEAP) and utility hardship / deferred-payment plans exist, that applying is free, that her utility has options she was never told about, and that a past-due bill is a problem with named help, not a private shame -- while utility-imposter 'pay now with gift cards or we shut you off in thirty minutes' callers (often spoofed numbers), fake 'utility assistance' / grant sites that harvest her SSN and bank login, upfront-fee 'we'll get your bill paid' cons, and overpayment/refund tricks hunt a woman already scared of losing the lights. Doors (hedged, none ranked): name it and know help exists (LIHEAP + hardship / payment plans, confirm with the agency / 211 / utility); call the utility directly from the number on the REAL bill (payment plans, budget billing, hardship, disconnection steps -- never a number a scary caller gives); free help to apply (energy-assistance agency, community action agencies, 211, no upfront fee or gift cards); gather what it asks (bill, shutoff notice, proof of income, ID -- a step today); the weight (faith, mentor, family, church, community action agency, 211, 988). Flat rule: real energy assistance is free to apply for, the real power company does not demand gift cards or crypto in thirty minutes, and no legitimate process needs your full SSN + bank login handed to a stranger to stop the shutoff -- anyone demanding gift cards, charging upfront, or harvesting info is the scam, not the help. Held a SEPARATE caution: a real shutoff notice, past-due balance, and deadline from her actual utility are NOT scams -- do not ignore a genuine notice / deadline; calling the number on the real bill or applying through the real agency / 211 is the right move. AI in quiet-helper mode (explains the words, helps her understand what an application gathers, finds the LIHEAP agency / utility real hardship line / 211 to reach herself, names the scam -- does NOT apply for her, act as the utility or agency, or promise the power stays on; never fed her full SSN / bank login / account passwords). Compliance stated twice in-body; dignity, never deficit (a person on a fixed income squeezed by a bill rising faster than the check, not careless). Rotated gender back to a WOMAN off the #211 man 47; centers a MID-LIFE / EARLY-SENIOR FIXED-INCOME PERSON (58). Deliberately distinct from housing/eviction (#202 -- utilities, not rent/landlord), SNAP (#208 -- power on, not groceries), debt collection (a current account + shutoff date, not a collector), and wages (#211) -- this is KEEPING THE LIGHTS AND COOLING ON, the free energy-assistance help, and the utility-imposter pay-now scam. Timely for the August heat. Saved to output/linkedin-2026-08-19-utility-shutoff-energy-assistance-liheap-scam-ministry.md. PRIOR (#211): wage theft / unpaid wages -- a working man quietly eating a short check for fear of losing the job, man 47. PRIOR (#210): childcare assistance / child-care subsidy -- a young working single mother, woman 29. PRIOR (#209): reentry / expungement -- a father rebuilding after incarceration, man 34. The plug is in."
runs_completed: 212
items_processed: 337
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
