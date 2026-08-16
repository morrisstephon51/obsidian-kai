---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-16T00:00:00Z"
current_task: "Generated LinkedIn post #197 -- the CAR / AUTO-DEBT ministry (the crisis the week a working man's only car dies: the vehicle that gets him to every shift needs a repair he cannot cover, the auto loan is already behind, a repossession notice is circling, and he is halfway to signing over his title at a triple-digit storefront and halfway to paying a caller who swears he can 'stop the repo today' for a fee): CALL THE LENDER FIRST for a hardship / deferment / modified payment (better before the repo than after); a REAL CREDIT-UNION / BANK LOAN or refinance instead of a title loan; KNOW YOUR REPOSSESSION RIGHTS (reinstatement / redemption, the deficiency balance, how a repo can legally happen -- vary by state/contract, verify current IL rules); CHECK EXISTING COVERAGE (gap insurance / warranty / service contract); NONPROFIT / CHARITABLE CAR & REPAIR HELP; LEGAL AID for auto fraud / predatory lending / wrongful repo; CHURCH BENEVOLENCE + 211. Scam weighted for the car: the TITLE-LOAN / BUY-HERE-PAY-HERE TRAP (not a phone scam but predatory -- sign over the title at triple-digit interest, one missed payment and they take the car and you can still owe a deficiency balance; the parallel to the deferred-interest medical card in #196), 'STOP YOUR REPOSSESSION TODAY FOR A FEE' scams (caller/text wanting gift card / prepaid / wire / Zelle -- a real lender works through your own account), FAKE AUTO-WARRANTY 'your warranty is expiring' robocalls, 'CREDIT REPAIR / fix your auto loan' upfront-fee scams, and 'your auto loan is past due, click to pay' PHISHING. QUIET-HELPER + augment-not-replace: AI explains title loan / buy-here-pay-here / repossession & reinstatement / redemption rights / the deficiency balance / gap insurance / refinancing / a lender hardship or deferment in plain words and helps him understand the repo notice, draft the hardship letter, and compare a credit-union loan to the title storefront -- but does NOT decide what he owes, does NOT promise the car is saved or the payment lowered, does NOT determine his repossession rights, is NOT the lender / loan office / lawyer, and must NEVER be fed his SSN, account number, or bank/card numbers. NEW lane, distinct from transportation / transit-access (that was ACCESS -- how a person without a car reaches work/doctor/store); this is the CAR ITSELF as a debt-and-scam emergency. NEW persona rotated off the run (woman 63 #190 ... man 64 #191 ... woman 44 #192 ... man 49 #193 ... woman 56 #194 ... man 41 #195 ... woman 52 #196): a MAN, 38, a warehouse / forklift worker, married with two kids, only car blew a $2,800 transmission, auto loan already a month behind, repossession warnings starting, halfway to signing over his title and halfway to paying a 'stop-the-repo' caller. Rotates gender back to a MAN off the woman (#196), centering a YOUNGER WORKING FATHER (38) in an acute car-and-debt emergency -- distinct from the fixed-income seniors (#190, 63; #191, 64), the widow (#194, 56), the caregiver (#196, 52), and the other recent working men (utility #195 man 41; SNAP #193 man 49). Dignity, never deficit (PULSE guard vs he-should-have-bought-a-more-reliable-car / should-have-saved / shouldn't-have-financed-it / is-bad-with-money). Core reframe: the man across town had the same week -- dead transmission, payment behind, repo notice, title storefront, 'stop-the-repo' caller -- but a friend said call your lender about a hardship, get a real loan before a title loan, know your rights, and don't pay that caller a fee, so he kept his car and title and worked out a plan, while the man in the pew almost signed his title away at triple-digit interest and almost wired a fee to a thief. Compliance TWICE in-body -- general navigation, NOT financial/legal advice, NOT an endorsement, NOT a determination of what he owes / whether the car is saved / his repo rights; repossession and lending rules belong to state law and the loan contract; verify at the lender hardship / loss-mitigation line, a legal-aid attorney, the Illinois AG / state regulator, and 211; never put an SSN, account number, or bank/card numbers into a public AI tool; real help is free or a real regulated loan and you make anyone prove it in writing first. Did NOT rank any door, did NOT promise the car is saved, did NOT assert any rule/amount/right as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-16-auto-car-loan-repossession-title-loan-ministry.md. PRIOR (#196): medical debt / hospital bill -- working caregiver woman 52. PRIOR (#195): utility / energy bill -- working father 41. The plug is in."
runs_completed: 197
items_processed: 322
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
