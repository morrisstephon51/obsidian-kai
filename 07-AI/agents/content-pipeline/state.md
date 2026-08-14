---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-13T20:20:00Z"
current_task: "Generated LinkedIn post #184 -- the property-tax relief / keeping-the-home-you-already-own ministry, a NEW lane opened deliberately as a KEEP door (not a GET door): every recent lane (#178 job, #181 diploma, #182 coverage, #183 clean record) was a door someone tries to walk THROUGH; this one meets the person on the far side of a door they walked through decades ago and are now quietly pushed back out of -- a longtime homeowner losing the paid-off house not to a mortgage but to the property-tax bill. Distinct from homeownership/first-time-buyer #174 (GETTING a home), housing/eviction (renters), and utility/energy (bills, not the tax): this is the person who OWNS free and clear and faces a tax sale anyway. Biblical (the inheritance, the family land, a good man leaves an inheritance to his children's children) and deeply local: south suburban Cook County (Harvey, Dolton, Robbins) carries some of the heaviest effective property-tax burdens around, and those homeowners appeal assessments and claim exemptions at far lower rates than wealthier townships -- the people paying most are least likely to be walked to the free relief. QUIET-HELPER mode: AI explains assessment/exemption/Senior Freeze/appeal/tax sale/redemption in plain words, never the subject, never the tax lawyer, never the one who files. NEW persona rotated off the recent run (SNAP mother #173 ... woman 41 #183): a MAN LATE SIXTIES (68), retired longtime deacon/usher, WIDOWER two years out who buried the wife who always handled the mail, paid off the same family home over 40 years, now silently drowning in a climbing tax bill on a fixed income, hiding the envelopes, at real risk of a tax sale on a house he owns outright. Distinct from elder church mother #179 (diff lane/gender) and barber 58 #182: elder widower, grief as undertone NOT the lane. Dignity, never deficit (PULSE guard vs. he should have planned/downsized): he did everything right and loses it anyway to a bill nobody showed him how to lower, in a township taxed harder than the ones that appeal. Doors, durable/hedged/routed, none ranked: (1) FREE Cook County Assessor exemptions -- General Homestead, Senior, Low-Income Senior Citizens Assessment Freeze (Senior Freeze), Persons-with-Disabilities, Veterans; free to apply, possibly missed for years; hedged HARD (Assessor decides). (2) FREE assessment appeal via Assessor + Board of Review -- the lever wealthy townships pull constantly, south suburbs rarely; hedged (deadlines by township/year). (3) Cook County Treasurer -- pay the bill, check for money owed back, real tax-sale/redemption info; routed, hedged. (4) Relief for what is owed -- homeowner-assistance/deferral programs that open/close/change, so ask the county + 211 what is available RIGHT NOW; hedged HARD (deliberately did NOT assert any specific program is currently open). (5) FREE legal aid for a tax-sale or deed threat -- get free help before signing anything. (6) 211/211.org. (7) Scam warning weighted for THIS barrier: we-buy-houses/cash-fast investors + deed theft targeting elders/grieving heirs, surplus-recovery cuts on money the Treasurer names for free, we'll-lower-your-taxes up-front-fee outfits filing exemptions/appeals that are FREE to file yourself; county-and-FTC-aligned truth that exemptions/appeals cost nothing, no up-front fee for surplus recovery, real help runs through the Assessor/Treasurer/free legal aid. AI held in quiet-helper + augment-not-replace: explains terms, helps him spot missed exemptions and overpaid years, finds the free application + deadline, drafts the questions, checks whether the Treasurer shows money owed back, sits with him so he stops hiding the envelope -- but does NOT give legal/tax advice, does NOT say what he qualifies for (Assessor + lawyer do), does NOT file, does NOT replace the county offices/attorney, and must NEVER be fed his SSN, bank/account numbers, or deed. Core reframe: the man across town has the same house, same paid-off note, same fixed income, but lives where people appeal every year and a neighbor/lawyer put every exemption on the bill automatically and told him about relief when he slipped; one keeps the family home and passes it down, the other loses a paid-off house to a tax sale he was never shown how to stop -- not less deserving, differently taxed and differently walked to the free help. Compliance TWICE in-body -- general navigation, NOT an endorsement of any office/program/attorney/company, NOT legal or tax advice; AI can be confidently wrong so verify every exemption/deadline/amount/eligibility with the Assessor, Treasurer, or a real legal-aid attorney; never feed an SSN, bank/account numbers, or deed to a public AI tool; big up-front fees to lower taxes or recover surplus, cold-callers, and fast cash for the deed are red flags. DELIBERATELY did NOT rank any office/program/attorney/company or promise a specific exemption, dollar amount, or that a home can be saved. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. A KEEP-what-you-own counterpart alongside homeownership/first-time-buyer #174; ties to Community Intake routing. PRIOR (#183): reentry / criminal-record sealing & expungement -- dependable woman 41. PRIOR (#182): health-coverage/insurance-enrollment -- barber 58. PRIOR (#181): adult-education/GED -- facilities-lead man late-30s. The plug is in."
runs_completed: 184
items_processed: 309
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
