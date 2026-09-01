---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-09-01T22:10:00Z"
current_task: "Generated LinkedIn post #261 -- WHOLLY NEW DOMAIN: U.S. CITIZENSHIP / NATURALIZATION (N-400 + I-912 fee waiver + free/low-cost accredited-rep legal help + free citizenship/civics classes) for a proud LAWFUL PERMANENT RESIDENT (green card) MAN of 54 in the south suburbs who has lived/worked/paid taxes here 20+ years, raised his kids as Americans, missed a parent's last months rather than risk a trip, and never naturalized because he was raised to keep his head down, cost no one anything, and never make trouble -- so he stayed a permanent resident (afraid of the fee, afraid he'd fail the English/civics test, afraid a wrong form would hurt his status), and does not know: citizenship is a RIGHT he can earn and apply for (N-400), NOT charity/trouble; a fee waiver/reduced fee (I-912) exists if he can't afford the cost; real legal help is FREE/low-cost (USCIS uscis.gov, DOJ-recognized nonprofits + accredited representatives, NIJC + ICIRR + New Americans Initiative, free citizenship/ESL classes at libraries/nonprofits); USCIS does NOT call/text out of the blue for gift cards/wire/upfront 'fine' to 'fix status' or 'stop deportation'; and NO ONE real sells guaranteed approval, a faster result, or citizenship for a fee -- and no honest helper is a notario/'consultant' charging thousands to fill out a form an accredited rep does free/low-cost. Doors (hedged): learn+file at uscis.gov (N-400, I-912 waiver); free/low-cost accredited legal help (DOJ-recognized org + accredited rep, NIJC, ICIRR, New Americans Initiative); free citizenship/English/civics classes; 2-1-1 for local legal help; verify via uscis.gov (real gov = .gov), guard A-number/SSN/logins/money/originals, never hand papers or cash to an unlicensed consultant. Scam spine: NOTARIO/'IMMIGRATION CONSULTANT' FRAUD (US notary is NOT a lawyer; big fees + unauthorized advice + wrong filings), IMPOSTER USCIS/ICE 'PROBLEM WITH YOUR STATUS / WARRANT -- PAY NOW OR BE DEPORTED' GIFT-CARD/WIRE SCAM, GUARANTEED-APPROVAL/'SPEED UP YOUR CITIZENSHIP' UPFRONT-FEE SCAM, FAKE USCIS WEBSITE/FEE (real: uscis.gov), PHISHING TEXT/CALL to 'verify' A-number/SSN or pay via link. Flat rule TWICE + SEPARATE caution that USCIS, DOJ-recognized nonprofits + accredited reps, NIJC, ICIRR, New Americans Initiative, legal aid, libraries, and 2-1-1 are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains N-400/I-912 + who generally qualifies, how to start at uscis.gov, docs to gather, how English/civics tests work + where free classes are, how to find a DOJ-recognized org; does NOT file his application, decide eligibility, give legal advice, promise approval/timeline, never handles A-number/SSN/payment, not a substitute for USCIS or a real accredited rep/attorney; verify via uscis.gov). Rotated to MAN 54 off #260 woman 66; distinct from #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68, #253 man 29, #252 woman 39. WHOLLY NEW citizenship/naturalization domain distinct from property-tax relief (#260), veterans benefits (#259), unemployment (#258), student loans (#257), health insurance (#256), income-tax (#252), disability/SSDI-SSI (#251), renter eviction (#245). Serves Plug AI community + faith-community + working-family + immigrant/new-American + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-citizenship-naturalization-n400-lpr-uscis-free-fee-waiver-accredited-rep-nijc-icirr-notario-consultant-fraud-guaranteed-approval-fee-imposter-ice-pay-or-deport-gift-card-fake-uscis-site-phishing-scam-ministry.md. PRIOR (#260): property-tax relief / homeowner-senior exemptions + Senior Freeze + free appeal / Cook County Assessor (widowed homeowner woman 66). PRIOR (#259): veterans benefits / VA disability compensation / accredited VSO / free claim + appeal (veteran man 61). PRIOR (#258): unemployment insurance / IDES / free claim + appeal (laid-off woman 44). The plug is in."
runs_completed: 260
items_processed: 385
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
