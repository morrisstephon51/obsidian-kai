---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-27T00:00:00Z"
current_task: "Generated LinkedIn post #243 -- NEW DOMAIN: SMALL BUSINESS / SELF-EMPLOYMENT / ENTREPRENEURSHIP (the business you want to build with your own hands) for a working man of 52, a skilled landscaper/handyman who has done the work for other people's companies for 25 years and now wants to put his own name on the truck and work for himself, dependable and respected but never taught the office side (LLC vs sole proprietor, license, registering a business, first equipment loan), embarrassed he does not know the paperwork and afraid one wrong move costs money he does not have, and who does not know that FREE real help to start a business exists (Small Business Development Centers + SCORE mentors, no cost), that most startup money is LOANS or savings and not free grants, that real grants are rare/competitive and NEVER unlocked by a fee, that he can register the business himself for a small state fee instead of paying a specialist, and that no honest funder charges a fee to guarantee a loan or release funding. Doors (hedged, none ranked): free SBDC/SCORE/city help; grants-vs-loans truth (don't build a plan on a stranger's grant); register it yourself cheaply through the state; start with a simple plan + real numbers; keep your own record (jobs/costs/income from day one); never pay to unlock funding; the weight (his hands, family, name on the truck, church, another man in the pews who started his business through free help). Scam spine: FAKE SMALL-BUSINESS/GOVERNMENT GRANT (fee or gift cards to unlock/release/guarantee), LLC/REGISTRATION/BUSINESS-SETUP MILL (big fee for state filings he can do cheap, often filed wrong + hidden recurring charges), ADVANCE-FEE/GUARANTEED-FUNDING LOAN BROKER + PREDATORY MERCHANT CASH ADVANCE (upfront fee for a loan that never comes; brutal daily paybacks that sink the business), SBA/GOVERNMENT IMPOSTER (fee, gift cards, SSN/EIN, bank login to process/approve/release funding), and BUSINESS-CREDIT/CPN/SHELF-CORPORATION SCHEME (pay to build business credit fast or buy a fake credit identity -- illegal + a trap). Flat rule: free help exists; most startup money is loans not grants; he can register it himself cheaply; no honest funder charges upfront to guarantee a loan/unlock a grant; a real agency never demands gift cards or SSN/EIN by text -- anyone charging to unlock a grant, guaranteeing funding, overcharging for cheap state filings, demanding gift cards/personal numbers, or selling a fake credit identity is the scam. SEPARATE caution: real SBDCs, SCORE, SBA programs, honest banks + CDFIs, honest advisors are NOT scams -- honest path runs through the free advisor + a legitimate lender; the caution is the fee-charging grant unlocker, setup mill, advance-fee broker, imposter, CPN scheme. Dignity, never deficit (a man who can do the work and did it well 25 years is not foolish for never being taught the office side; wanting to work for himself is honorable). AI in quiet-helper + augment-not-replace (explains LLC/EIN/license/business plan/grant-vs-loan/SBDC/SCORE/CDFI/merchant-cash-advance; helps him understand a form, draft a simple plan, organize costs/jobs/income, find free SBDC/SCORE/city office + a legitimate lender, spot the scam -- does NOT act as his accountant/lawyer, does NOT say he will get funded or succeed, does NOT give legal/tax/financial advice, does NOT file/apply, does NOT promise an outcome, never fed his SSN/EIN/bank login/financials). Compliance stated TWICE in-body (general navigation, NOT legal/tax/financial advice and NOT a guarantee of funding or success; licensed accountant/attorney/loan officer advises his case; AI can be confidently wrong -- verify with SBDC, SCORE, Secretary of State, or a legitimate lender; never pay upfront to unlock a grant or guarantee a loan, never gift cards, never hand SSN/EIN/bank login to a grant/funding outfit; use free SBDC/SCORE + legitimate lenders). Rotated gender back to a MAN off the grandmother 66 (#242) and set fresh AGE 52. Opens a WHOLLY NEW DOMAIN (economic mobility / entrepreneurship) distinct from wage theft #241 (getting paid as an EMPLOYEE, not building a business), unemployment #224 (a post-job benefit, not startup capital), and IRS back tax #233 (a debt owed, not financing), in a DIGNITY-OF-THE-BUILDER frame, keeping the scam-prevention spine. Serves Plug AI community + working-family + digital-literacy + Get-Skilled pillars AND BigHeart church partnerships + the working men/women in the pews with a skill in their hands and a business in their heart. Named geography: Cicero, Berwyn, Blue Island, Chicago Heights, Summit, Melrose Park, Bridgeview, Harvey, Dolton, Markham. Saved to output/linkedin-2026-08-27-small-business-self-employment-startup-free-sbdc-score-help-grants-vs-loans-fake-business-grant-llc-mill-advance-fee-funding-imposter-cpn-scam-ministry.md. PRIOR (#242): kinship care / grandparents raising grandchildren (grandmother) + child-only help + free legal aid + guardianship done free + guardianship-fee-shark / fake-caregiver-grant / agency-imposter / no-rights-lie scam, woman 66. PRIOR (#241): wage theft / unpaid wages (construction day laborer) + free labor-department wage claim + free legal aid/worker centers + wage rights regardless of status + recovery-fee-shark / guaranteed-recovery / labor-department-imposter / employer-lie scam, man 44. PRIOR (#240): medical debt / hospital charity care (home-health aide) + itemized-bill rights + free counselors/legal aid + relief-fee / guaranteed-wipeout / collector-imposter scam, woman 59. The plug is in."
runs_completed: 242
items_processed: 367
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
