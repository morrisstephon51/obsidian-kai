---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-15T23:20:00Z"
current_task: "Generated LinkedIn post #196 -- the MEDICAL-DEBT / HOSPITAL-BILL ministry (the crisis that lands weeks after the emergency, when a hardworking woman who did everything right opens a $23,000 hospital bill she cannot pay, the collection calls start, and she is halfway to signing a deferred-interest 'medical credit card' and halfway to wiring a 'settlement' to a caller): HOSPITAL FINANCIAL ASSISTANCE / CHARITY CARE she has to ask for by name (nonprofit hospitals generally required to have a written policy that can cut or forgive a bill by income, free to apply); an ITEMIZED BILL + error review; the NO SURPRISES ACT for surprise emergency out-of-network bills; PRESUMPTIVE / RETROACTIVE MEDICAID + a hospital financial counselor; an INTEREST-FREE HOSPITAL PAYMENT PLAN + a negotiated balance BEFORE any credit card; the changing medical-debt / credit-report rules (verify, don't assume); legal aid + church benevolence + 211. Scam weighted for medical debt: PHANTOM-DEBT / FAKE-COLLECTOR calls that won't send written validation and want gift card / prepaid / wire / Zelle (a real collector must validate in writing; never pay a caller until verified), MEDICAL-DEBT 'SETTLEMENT / FORGIVENESS' upfront-fee scams (real financial assistance is free), 'your hospital bill is past due, click to pay' PHISHING, and the DEFERRED-INTEREST MEDICAL CREDIT CARD trap (not a phone scam but predatory -- a missed payment / expired promo drops back-interest on the whole balance). QUIET-HELPER + augment-not-replace: AI explains charity care / financial-assistance policy / itemized bill / No Surprises Act / retroactive Medicaid / debt validation / deferred interest in plain words and helps her draft the itemized-bill and financial-assistance and payment-plan letters -- but does NOT decide what she owes, does NOT promise forgiveness or an amount, does NOT determine Medicaid eligibility, is NOT the hospital / billing office / financial counselor / lawyer, and must NEVER be fed her SSN, insurance ID, account number, or bank/card numbers. NEW lane, distinct from prescription meds (#190, the pharmacy counter) and funeral costs (#194, after a death) -- this is the HOSPITAL BILL ITSELF. NEW persona rotated off the run (man 57 #189 ... woman 63 #190 ... man 64 #191 ... woman 44 #192 ... man 49 #193 ... woman 56 #194 ... man 41 #195): a WOMAN, 52, a home health aide / CNA, single, thin high-deductible coverage, emergency gallbladder surgery, a $23,000 bill weeks later, collection calls starting, halfway to a deferred-interest card and halfway to paying a 'settlement' caller. Rotates gender back to a WOMAN off the man (#195), centering a MIDDLE-AGED WORKING CAREGIVER (52) in an acute medical-debt emergency. Dignity, never deficit (PULSE guard vs she-should-have-had-better-insurance / should-have-saved / ran-up-the-bill / irresponsible). Core reframe: the woman across town had the same emergency, surgery, $23,000 bill, and collection calls -- but a friend said ask the hospital for charity care before you pay anyone (it's free), get an itemized bill, ask for an interest-free plan before any medical credit card, and make any caller prove the debt in writing -- so she got most of the bill forgiven and paid the rest interest-free, while the woman in the pew almost signed a deferred-interest card and almost wired a settlement to a thief. Compliance TWICE in-body -- general navigation, NOT financial/legal/medical advice, NOT an endorsement, NOT a determination of what she owes / what's forgiven / Medicaid eligibility; what a hospital forgives and who qualifies belongs to the hospital's financial-assistance office and the Medicaid agency; verify at the hospital financial-assistance/billing office, the state Medicaid office, a legal-aid attorney + 211; never put an SSN, insurance ID, account number, or bank/card numbers into a public AI tool; a real collector must validate a debt in writing and the real application is free. Did NOT rank any door, did NOT promise forgiveness or an amount, did NOT assert any rule/amount/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-15-medical-debt-hospital-charity-care-ministry.md. PRIOR (#195): utility / energy bill -- working father 41. PRIOR (#194): funeral / burial costs -- widowed woman 56. The plug is in."
runs_completed: 196
items_processed: 321
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
