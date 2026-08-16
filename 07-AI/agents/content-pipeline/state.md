---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-16T12:45:00Z"
current_task: "Generated LinkedIn post #198 -- the TAX / IRS-DEBT ministry (the crisis the day a hardworking woman opens an official IRS envelope saying she owes back taxes she cannot pay, penalties stacking, and within days a 'federal agent' is calling threatening arrest unless she pays today in gift cards while a TV company promises to 'settle her tax debt for pennies on the dollar' for a big fee upfront): DON'T PANIC / VERIFY THE NOTICE IS REAL (the IRS mails you first; the notice has a number and appeal rights; call the number on the official notice or IRS.gov, never a caller's number); IRS PAYMENT OPTIONS (installment agreement / payment plan, possibly an offer in compromise or currently-not-collectible -- eligibility decided by the IRS); FREE TAX HELP (VITA / TCE, the Taxpayer Advocate Service, a Low-Income Taxpayer Clinic); CHECK THE NOTICE IS EVEN RIGHT (underreporting notices can be wrong / double-counted / miss deductions -- right to respond & dispute); CREDITS SHE MAY BE OWED (EITC & others); LEGAL AID / LITC for a dispute or predatory tax-relief fraud; CHURCH BENEVOLENCE + 211. Scam weighted for the tax bill: IRS-IMPERSONATION gift-card / wire / crypto arrest-threat calls & texts (the real IRS mails first, never demands gift cards, never threatens immediate arrest by phone), the 'TAX-RELIEF / pennies on the dollar' UPFRONT-FEE FIRM trap (predatory -- charge thousands, often deliver nothing, when a real offer-in-compromise can be pursued free via a LITC; parallel to the title-loan trap in #197 and the deferred-interest medical card in #196), GHOST PREPARERS (promise a huge refund, take a cut, won't sign the return, vanish), REFUND-ANTICIPATION-LOAN / 'instant refund' traps, and 'verify your refund / account locked, click to pay' PHISHING. QUIET-HELPER + augment-not-replace: AI explains installment agreement / offer in compromise / currently-not-collectible / a CP2000 underreporting notice / penalty abatement / the Taxpayer Advocate / VITA / a Low-Income Taxpayer Clinic in plain words and helps her read the notice, draft a response / payment-plan letter, and compare doing it herself or with free help against a paid 'tax-relief' firm -- but does NOT decide what she owes, does NOT promise the debt reduced or forgiven, does NOT determine her tax liability or eligibility, is NOT the IRS / a CPA / a tax attorney, and must NEVER be fed her SSN, ITIN, or bank / card numbers. NEW lane, distinct from the recent debt/bill run (SNAP #193, funeral #194, utility #195, medical debt #196, auto/car #197): this is BACK TAXES and an IRS NOTICE. NEW persona rotated off the run (woman 63 #190 ... man 64 #191 ... woman 44 #192 ... man 49 #193 ... woman 56 #194 ... man 41 #195 ... woman 52 #196 ... man 38 #197): a WOMAN, 47, a home health aide / CNA working two jobs who took on some 1099 side work she didn't understand the taxes on, single, one grown kid, terrified of arrest, halfway to wiring gift cards to a 'federal agent' and halfway to paying a big upfront fee to a 'tax-relief' company. Rotates gender back to a WOMAN off the man (#197), centering a MIDDLE-AGED WORKING WOMAN (47) in an acute tax-debt-and-scam emergency -- distinct from the fixed-income seniors (#190, 63; #191, 64), the widow (#194, 56), the caregiver (#196, 52), and the recent working men (auto #197 man 38; utility #195 man 41; SNAP #193 man 49). Dignity, never deficit (PULSE guard vs she-should-have-kept-records / should-have-known-she'd-owe / is-bad-with-money / must-have-cheated). Core reframe: the woman across town had the same envelope -- same balance due, same penalties, same 'federal agent' caller, same pennies-on-the-dollar company -- but a friend said the IRS mails you first and never wants gift cards, you can ask for a payment plan, and there's free tax help, so she set up an installment agreement, got a free clinic to check the notice (it had overstated the bill), and kept her money and peace, while the woman in the pew almost wired gift cards to a thief and almost signed thousands to a firm. Compliance TWICE in-body -- general navigation, NOT tax/legal advice, NOT an endorsement, NOT a determination of what she owes or her eligibility; tax liability and eligibility belong to the IRS and the law; verify at IRS.gov, the number on the official mailed notice, the Taxpayer Advocate Service, a VITA site, a Low-Income Taxpayer Clinic, and 211; never put an SSN or ITIN into a public AI tool or hand it to a caller; the real IRS mails you first and never demands gift cards. Did NOT rank any door, did NOT promise the debt reduced/forgiven, did NOT assert any amount/rule/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-16-irs-back-taxes-tax-notice-ministry.md. PRIOR (#197): car / auto-debt / repossession -- working father 38. PRIOR (#196): medical debt / hospital bill -- working caregiver woman 52. The plug is in."
runs_completed: 198
items_processed: 323
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
