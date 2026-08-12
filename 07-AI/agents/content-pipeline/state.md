---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-12T03:10:00Z"
current_task: "Generated LinkedIn post #176 -- the small-business / self-employment / entrepreneurship-formalization ministry: a genuinely NEW resource-navigation lane for the person in the pews who ALREADY earns from a skill and just does not know it is a business yet. Kept DELIBERATELY DISTINCT from employment/jobs (#done, finding a W-2 job) and financial-empowerment/debt-credit-banking (#172, household money), and inverted the food frame away from food/SNAP (#173) -- food as a BUSINESS and a GIFT, not a need. Like homeownership (#174) and college-access (#175), an ASPIRATIONAL build-something lane continuing that arc, landing on the same Plug AI wall -- 'a real business happens to other people, people with a lawyer and a loan officer and money we do not have' -- the exact belief the post dismantles. NEW persona for series variety: a WOMAN entrepreneur, the church caterer / 'plate lady,' the most iconic informal-business figure in the Black church, rotated fully off the young SNAP mother (#173) and mid-life homeownership woman (#174) by making the frame her GIFT and her twenty-year enterprise, and framed with full dignity as a businesswoman missing only the paperwork and the paid team (PULSE guard against the domestic-labor stereotype: she is the most capable person in the building; the gap is scaffolding, not talent). Holds the whole small-business maze for people certain the door is bolted: that the EIN from the IRS is genuinely FREE at irs.gov and never pay a site for it (exact parallel to the free-FAFSA scam of #175); that a business bank account + simple books, not a storefront, is the real first step; that she is likely already a sole proprietor the moment she took money and whether to form an LLC is a question to ASK a free adviser, not guess -- HEDGED and routed; that free one-on-one advising exists and is not a secret for the connected (SCORE, the Illinois SBDC, the Women's Business Development Center); that pricing out of love and habit instead of cost is why the hardest worker in three towns barely breaks even; that the Illinois Cottage Food Law MAY let a home cook sell certain foods with real limits -- HEDGED and routed to the county health department; that a nonprofit lender / CDFI will make a first loan a bank will not; that 'guaranteed government grant' fee/gift-card/DM/robocall offers are scams every time; and that a merchant cash advance is the payday loan of small business. AI as the accountant / consultant / marketing team / SBA adviser a funded founder assembles on day one -- reframe sharpened: the gap is not that their founder is more talented, it is that theirs had a paid team from the first dollar and ours had one woman with a gift, a foil pan, and orders on the back of the church bulletin. Augment-not-replace held (the gift, the recipe, the reputation, the four-a.m. trust stay hers; it just finally lets her get paid like the professional she has been for twenty years). Real free help routed to: SCORE (score.org), the Illinois SBDC (ilsbdc.biz), the Women's Business Development Center (wbdc.org), the SBA (sba.gov), the free EIN at irs.gov, local city/village licensing + county health department, the Illinois Secretary of State + IDOR for registration/sales tax, and a CDFI/nonprofit lender via the SBDC. Care note on four real risks: EIN-fee and 'guaranteed grant' scams, 'business credit building' schemes, predatory MCAs, and guessing at formation/licensing/food-safety instead of asking. DELIBERATELY did NOT tell anyone which structure to form, which license they need, what to charge, or that their food qualifies under cottage-food law (all legal/tax/licensing-specific) -> every one hedged and routed. CRITICAL compliance framing stated TWICE in-body -- general navigation, NOT legal, tax, accounting, business-licensing, or financial advice; helping someone learn the EIN is free or that the SBDC exists is NOT forming their business, filing their taxes, or telling them which license they need -- always route the actual formation, licensing, food-safety, tax, and lending decisions to the SBDC, SCORE, an attorney/accountant, the licensing and health offices, and the SBA. Ties to Community Intake; the plug is in. --- PRIOR (#175): the college-access / FAFSA / first-generation-student ministry -- the father who got his daughter through as the first in the family via a free FAFSA, a Pell grant, and a state MAP grant nobody told him about; opened the college-access / financial-aid lane. PRIOR (#174): the homeownership / first-time-buyer / down-payment-assistance ministry."
runs_completed: 176
items_processed: 301
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
