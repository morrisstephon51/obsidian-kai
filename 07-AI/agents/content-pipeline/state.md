---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-11T22:05:00Z"
current_task: "Generated LinkedIn post #175 -- the college-access / FAFSA / financial-aid / first-generation-student ministry: a genuinely NEW resource-navigation lane that ties directly to The Plug AI's OWN stated mission (AI literacy for first-gen students in south suburban Cook County), so it deepens brand coherence rather than drifting. Kept DISTINCT from employment/jobs (#done, adult workforce), childcare/early-childhood (#done, youngest kids), homeownership/first-time-buyer (#174, adult wealth-building), financial-empowerment/debt-credit-banking (#172), and food/SNAP (#173). Like #174 an ASPIRATIONAL build-something lane, not a crisis/deficit lane, and it lands on the same Plug AI wall -- 'college is not for people like us' -- the exact belief the post dismantles. NEW persona for deliberate series variety: a FATHER, a working man who never went to college himself and got his DAUGHTER through as the first in the family via the FREE FAFSA, a Pell grant, and a state MAP grant nobody told him about -- a MALE peer-navigator chosen to rotate off the two prior women (homeownership woman #174, young SNAP mother #173), true to how college knowledge travels in these communities: from the one parent who finally got a kid through the door, quietly, after service. Holds the whole college-aid maze for families certain the door is bolted: that the FAFSA is genuinely FREE (never pay a site to fill it) and skipping it leaves every dollar on the table; that the Pell grant is real money never repaid and far more qualify than apply; that the Illinois MAP grant (via ISAC) is FREE money that RUNS OUT -- file early because funds are first-come, the calendar is the whole game; that you do NOT need perfect grades or a college fund -- aid is need-based and community-college-then-transfer is cheap, respected, and real; that free/reduced-lunch students get college-application AND test fee waivers most never claim; that dual-credit is free college credit banked in high school; that federal loans come first and private loans + for-profit 'fast degree' mills are the trap; that any scholarship charging a fee or 'guaranteeing' money is a scam; that in Illinois a student with no SSN may still apply for state aid via the Alternative Application (RISE Act) -- HEDGED and routed; and that one overworked counselor for hundreds of seniors is why nobody walked these families through -- the barrier is information and a deadline, not the child's worth. AI as the private college counselor / admissions coach / financial-aid adviser a resourced family hires for thousands -- reframe sharpened: the gap is not that their kid is smarter, it is that their family had someone PAID to walk the kid from junior year to move-in day and ours had one tired father holding the map from the one time he got his own girl through. Augment-not-replace held (the belief he puts in a kid, the after-service trust, the hand on another father's shoulder stay his). Real free help routed to: the FAFSA at studentaid.gov + Federal Student Aid Information Center (1-800-433-3243), the Illinois Student Assistance Commission / MAP grant (isac.org), the high school counselor / college-and-career center, the college's own financial-aid office, the local community college, and 2-1-1. Care note on four real current risks: paid-FAFSA/'guaranteed'-scholarship fee scams (real aid never charges), predatory for-profit colleges, private loans taken before federal aid is maxed, and the undocumented-student assumption the door is closed (IL Alternative Application may apply). DELIBERATELY did NOT cite Pell max / income cutoffs (change yearly) or a specific free-tuition program (City Colleges 'Star' is CPS-specific, our audience is south-suburban NOT CPS) -> hedged to studentaid.gov / financial-aid office / the community college. CRITICAL compliance framing stated TWICE in-body -- general navigation, NOT financial-aid, legal, immigration, admissions, or tax advice, and helping someone learn a grant exists is NOT filing their FAFSA or determining eligibility -- always route the actual application, current rules, and eligibility to the school counselor, the college financial-aid office, studentaid.gov, and ISAC. Ties to Community Intake; the plug is in. --- PRIOR (#174): the homeownership / first-time-homebuyer / down-payment-assistance ministry -- the woman who rented her whole life and bought her first home in her fifties through a free HUD counselor and down-payment assistance, now the peer younger families ask 'how did you do it?'; opened the homeownership / first-time-buyer / down-payment-assistance / foreclosure-prevention lane, distinct from housing-eviction."
runs_completed: 175
items_processed: 300
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
