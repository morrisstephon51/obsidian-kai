---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-01T13:00:00Z"
current_task: "Generated LinkedIn post #260 -- WHOLLY NEW DOMAIN: PROPERTY TAX RELIEF (Cook County homeowner/senior exemptions + Senior Freeze/Low-Income Senior Citizens Assessment Freeze + free assessment appeal) for a proud WIDOWED HOMEOWNER WOMAN of 66 in the south suburbs who has owned/paid on her home for decades, watches the tax bill climb yearly while her fixed income does not, and never filed the exemptions/freeze she qualifies for because she was raised to pay what you owe and never ask for a break -- so she quietly cuts elsewhere and fears losing the house, and does not know: property-tax relief is NOT a handout but written into law for exactly her (filed FREE with the Cook County Assessor online/mail/phone/township, built for a long-time senior homeowner on a fixed income, assessment appealable FREE), free help to file+appeal is real (Assessor + Board of Review, free HUD housing counselors + legal aid for a threatened tax sale, township assessors), NO county office demands gift cards/wire/upfront fee to hold your home or release a refund and never texts out of the blue for SSN/login/bank info, and NO ONE real charges a percentage/upfront fee to file relief the Assessor files free -- and no honest person asks her to sign over her deed. Doors (hedged): file FREE at cookcountyassessor.com; Senior Freeze + Senior Exemption free; appeal FREE (Assessor + Board of Review, no lawyer/fee); check owed + payment options at cookcountytreasurer.com; 2-1-1 / free HUD counselor / legal aid if tax sale threatened; verify via official county sites+numbers, guard SSN/logins/bank/deed, never sign the house over. Scam spine: FEE-CHARGING TAX-APPEAL/EXEMPTION SHARK, IMPOSTER BEHIND-ON-TAXES PAY-NOW-OR-LOSE-YOUR-HOME GIFT-CARD/WIRE SCAM, DEED/TITLE THEFT (save your home from tax sale just sign here), FAKE ASSESSOR/TREASURER WEBSITE (real: cookcountyassessor.com + cookcountytreasurer.com), FAKE OVERDUE-TAX/SURPLUS-REFUND VERIFY-TO-CLAIM PHISHING TEXT. Flat rule TWICE + SEPARATE caution that the Cook County Assessor, Treasurer, Board of Review, township assessors, HUD counselors, legal aid, and 2-1-1 are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains exemptions/freeze + who qualifies, how to start at cookcountyassessor.com, docs to gather, township assessor + hours, what an appeal is; does NOT file her exemption/appeal, decide eligibility/savings, promise approval/refund, never handles SSN/bank/deed, not a substitute for the Assessor; verify via county sites). Rotated to WOMAN 66 off #259 man 61; distinct from #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68, #253 man 29, #252 woman 39, #251 man 46. WHOLLY NEW property-tax-relief domain distinct from renter eviction (#245), income-tax filing (#252), utility (#249), medical debt (#248), veterans benefits (#259), unemployment (#258), health insurance (#256), disability/SSDI-SSI (#251). Serves Plug AI community + faith-community + working-family + seniors + homeowners + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-property-tax-relief-homeowner-senior-exemption-freeze-cook-county-assessor-free-appeal-fee-shark-imposter-tax-due-gift-card-deed-title-theft-fake-assessor-site-surplus-refund-scam-ministry.md. PRIOR (#259): veterans benefits / VA disability compensation / accredited VSO / free claim + appeal (veteran man 61). PRIOR (#258): unemployment insurance / IDES / free claim + appeal (woman 44). PRIOR (#257): student loans / IDR / PSLF / studentaid.gov (man 41). The plug is in."
runs_completed: 259
items_processed: 384
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
