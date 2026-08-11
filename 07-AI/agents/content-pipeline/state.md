---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-11T08:06:00Z"
current_task: "Generated LinkedIn post #172 -- the financial-empowerment / debt-and-credit ministry: the brother everybody quietly pulls aside about money, the one good with numbers who has read more bad loan contracts than he can count, who has talked people out of a title loan in the church parking lot, who does not judge the person too ashamed to admit what they already signed -- and then single-handedly trying to hold the whole personal-finance maze for a community predatory lenders were built to hunt: that in Illinois a payday or title lender charging 300% is actually illegal, because the 2021 Predatory Loan Prevention Act caps most consumer loans at 36% APR; that a credit report is free from the only federally authorized source (AnnualCreditReport.com), not the app with the jingle; that debt collectors have hard legal limits under the FDCPA (no calls at all hours, no threats, no lies) and you can demand written validation before paying a dime; that the CFPB takes complaints against banks/lenders/collectors for free and gets answers; that free nonprofit HUD-approved credit counseling exists (NFCC 1-800-388-2227); that safe, no-overdraft Bank On accounts exist for people the banks pushed out; that a community credit union / CDFI will lend small at a human rate instead of a payday trap; that the Illinois Attorney General Consumer Fraud Bureau (1-800-386-5438) and the FTC take scam reports; and that being behind on money is not a moral failure and being unbanked is not stupidity; AI as the financial advisor / CPA / personal banker / consumer attorney a resourced family keeps on retainer -- plus real free help anyone can reach: AnnualCreditReport.com, CFPB (consumerfinance.gov, 1-855-411-2372), NFCC, the Illinois AG hotline, the FTC (reportfraud.ftc.gov, identitytheft.gov), Bank On accounts, a local credit union/CDFI, 2-1-1; opens a NEW resource-navigation lane -- financial-empowerment / debt-and-credit / banking-access -- kept DISTINCT from benevolence (one-time emergency cash), tax/EITC (filing & refunds), utility/energy assistance (LIHEAP bills), employment/jobs (work & income), medical-bills/healthcare-access (#170, medical debt), and legal aid (a debt lawsuit already filed routes there); added a care note on financial scams and shame (credit-repair firms charging cash for what you can dispute free; debt-settlement outfits that make it worse; advance-fee 'guaranteed loan' scams) paired with the affirming truth that the credit report is free, the CFPB complaint is free, and being behind is not a character flaw; CRITICAL compliance framing stated twice in-body -- general navigation, NOT financial, tax, legal, or credit-repair advice, and if a debt lawsuit is filed or a foreclosure/repossession is imminent, route to legal aid and a licensed professional now -- always route to a nonprofit HUD-approved credit counselor, the CFPB, legal aid, or the Illinois Attorney General; augment-not-replace held (the parking-lot conversation, the folded papers, and the trust stay his); ties to Community Intake; the plug is in"
runs_completed: 172
items_processed: 297
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
