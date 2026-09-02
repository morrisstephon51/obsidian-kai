---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-09-01T22:40:00Z"
current_task: "Generated LinkedIn post #262 -- WHOLLY NEW DOMAIN: WIC / MATERNAL-AND-CHILD NUTRITION (Special Supplemental Nutrition Program for Women, Infants, and Children -- free healthy food + infant formula + fruits/veg/milk/eggs + free breastfeeding support + nutrition counseling + doctor/dentist referrals) for a proud YOUNG WORKING MOTHER of 27 in the south suburbs with a toddler and a new baby whose real paycheck still runs out before the month does, who skips her own plate so the kids eat and has never signed up for WIC because she was raised that a good mother provides for her own and 'we don't take handouts' -- so she quietly goes without and does not know: WIC is a RIGHT her pregnancy/postpartum months and children under five already qualify her for, NOT welfare/charity; a working paycheck usually does NOT put her over the line (WIC reaches far more working families than assumed, and Medicaid/SNAP families often qualify automatically); applying is FREE through Illinois WIC (dph.illinois.gov WIC) + local WIC clinic, county/city health department, or FQHC; no real WIC office demands gift cards/wire/'enrollment' or 'activation' fee and never texts/calls out of the blue for SSN, eWIC card number + PIN, or bank login to 'verify/reactivate/keep' benefits; and NO ONE real charges to sign her up or 'get her approved faster' for a fee. Doors (hedged): apply free via Illinois WIC + local clinic/health dept/FQHC; WIC referral through child's doctor, OB, delivery hospital, or Head Start; 2-1-1 for nearest WIC agency + other food help (pantries, SNAP, school meals); treat eWIC card like cash (guard card number, PIN, SSN, logins, bank info); verify via official Illinois WIC site + clinic's real number. Scam spine: FAKE 'WIC ENROLLMENT/ACTIVATION FEE' (charging to sign up for or speed up a free program), eWIC CARD SKIMMING / CARD-AND-PIN THEFT (reader skimmer or caller/texter fishing 16-digit card number + PIN), IMPOSTER 'YOUR WIC WILL BE CUT OFF/SUSPENDED UNLESS YOU VERIFY OR PAY NOW' GIFT-CARD/WIRE/PHISHING, FAKE WIC WEBSITE/APP (lookalike that charges a fee or steals login/card/SSN), PHISHING TEXT/CALL to 'confirm/reactivate/protect' benefits via card number/PIN/SSN/bank login. Flat rule TWICE + SEPARATE caution that Illinois WIC, county/city health dept, FQHCs, her child's doctor + OB, Head Start, and 2-1-1 are NOT scams. Dignity-never-deficit + AI quiet-helper/augment-not-replace with compliance TWICE (explains what WIC is + who generally qualifies incl. working/Medicaid/SNAP families, how to start at Illinois WIC site, docs to gather, how to find local clinic + what an appointment is like; does NOT enroll her, decide eligibility, promise approval/amount, never handles SSN/card number/PIN/bank login, not a substitute for a WIC clinic; verify via official Illinois WIC site + local clinic). Rotated to WOMAN 27 off #261 man 54; distinct from #260 woman 66, #259 man 61, #258 woman 44, #257 man 41, #256 woman 52, #255 man 33, #254 woman 68, #253 man 29, #252 woman 39. WHOLLY NEW WIC/maternal-and-child nutrition domain distinct from citizenship (#261), property-tax relief (#260), veterans benefits (#259), unemployment (#258), student loans (#257), health insurance (#256), income-tax (#252), disability/SSDI-SSI (#251), renter eviction (#245); adjacent to but distinct from general SNAP/food-assistance and child-care (CCAP) posts (focused on pregnancy/postpartum + children under five: formula, breastfeeding support, nutrition counseling). Serves Plug AI community + faith-community + working-family + young-parents/mothers + maternal-and-child-health + financial-literacy + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-09-01-wic-nutrition-young-mother-women-infants-children-illinois-free-formula-breastfeeding-fqhc-health-dept-enrollment-fee-ewic-skimming-phishing-verify-cutoff-fake-wic-site-scam-ministry.md. PRIOR (#261): U.S. citizenship / naturalization / N-400 + I-912 fee waiver / free accredited-rep legal help (lawful permanent resident man 54). PRIOR (#260): property-tax relief / homeowner-senior exemptions + Senior Freeze / free appeal / Cook County Assessor (widowed homeowner woman 66). PRIOR (#259): veterans benefits / VA disability compensation / accredited VSO / free claim + appeal (veteran man 61). The plug is in."
runs_completed: 261
items_processed: 386
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
