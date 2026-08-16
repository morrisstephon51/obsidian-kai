---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-15T22:52:00Z"
current_task: "Generated LinkedIn post #195 -- the UTILITY / ENERGY-BILL ministry (the summer-heat crisis when the past-due electric bill hits, a shutoff notice is on the door in a 98-degree August, and a proud working father is about to wire $700 in gift cards to a thief spoofing the power company): LIHEAP + summer COOLING assistance; heat-wave SHUTOFF PROTECTIONS + a doctor MEDICAL CERTIFICATE for a home with electric medical equipment (baby on a nebulizer); the utility own DEFERRED-PAYMENT / BUDGET-BILLING / ARREARAGE-FORGIVENESS / low-income-rate programs you must ask for by name; PERCENTAGE-OF-INCOME payment plans; WEATHERIZATION; township general assistance + community action agency + church energy funds; 211. Scam weighted for utilities: the DISCONNECTION GIFT-CARD PHONE SCAM (spoofed name/caller ID, 'pay in 30 minutes with a prepaid card or the power is off tonight' -- a real utility never takes gift cards, never gives 30 minutes, mails written notice; hang up and call the number on your PAPER BILL), fake 'energy relief' phishing texts/sites (LIHEAP is free to apply for), door-to-door 'switch your supplier' rate schemes + 'let me see your bill' account-number lifts. QUIET-HELPER + augment-not-replace: AI explains LIHEAP / cooling program / budget billing / deferred-payment / arrearage forgiveness / medical certificate in plain words and helps him draft the hardship ask -- but does NOT decide eligibility, does NOT promise the bill is paid/forgiven, does NOT set his rate, is NOT the utility/community action agency/caseworker, and must NEVER be fed his SSN, utility account number, or bank/card numbers. NEW lane, distinct from eviction (#192, housing) and SNAP (#193, food) -- this is the LIGHTS AND THE AC. NEW persona rotated off the run (man 57 #189 ... woman 63 #190 ... man 64 #191 ... woman 44 #192 ... man 49 #193 ... woman 56 #194): a MAN, 41, a warehouse forklift operator whose hours got cut in a slow season, married with two young kids (one a baby on breathing treatments), $700 past-due + a disconnection notice in a heat wave, too proud to tell church he is behind, halfway to buy gift cards for the scammer. Rotates gender back to a MAN off the woman (#194), centering a WORKING FATHER (41) in an acute summer utility emergency. Dignity, never deficit (PULSE guard vs he-should-have-budgeted / irresponsible / too-proud / got-himself-behind). Core reframe: the man across town had the same cut hours, heat wave, notice, and scam call -- but a friend said there is LIHEAP + a cooling program, the electric company has a payment/hardship plan you ask for by name, a doctor note protects the power for the baby on a nebulizer, and the gift-card call is a scam -- hang up and call the number on your bill -- so he kept the lights and AC on through August without wiring $700 to a thief, while the man in the pew almost bought the cards and sat in the dark too proud to ask. Compliance TWICE in-body -- general navigation, NOT financial/legal advice, NOT an endorsement, NOT an eligibility determination; what LIHEAP/the utility pay and who qualifies belongs to the community action agency and the utility; verify at the community action agency and the utility number on your PAPER BILL + 211; never put an SSN, utility account number, or bank/card numbers into a public AI tool; a real utility never demands gift cards or a 30-minute deadline and the real application is free. Did NOT rank any option, did NOT promise he qualifies, did NOT assert any amount/rule as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-15-utility-energy-assistance-ministry.md. PRIOR (#194): funeral/burial costs -- widowed woman 56. PRIOR (#193): SNAP -- working man 49. The plug is in."
runs_completed: 195
items_processed: 320
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
