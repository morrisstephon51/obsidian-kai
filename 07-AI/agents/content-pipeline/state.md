---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-26T23:20:00Z"
current_task: "Generated LinkedIn post #241 -- NEW DOMAIN: WAGE THEFT / UNPAID WAGES (the pay you earned and did not get) for a working man of 44, a construction/drywall day laborer hired through a crew boss, who put in weeks of long days and then got shorted -- last two weeks never paid, overtime never counted, boss saying next-week then not answering -- who is embarrassed and afraid that pushing back costs him the next job or blacklists him off the crews, and who does not know that the hours he worked are wages he is generally owed no matter how he was paid, that the IL Dept of Labor + US DOL Wage and Hour Division investigate wage claims for FREE, that legal aid + worker centers help at no cost, and that being paid in cash/off the books AND his immigration status do NOT erase his right to be paid. Doors (hedged, none ranked): hours worked = wages generally owed (min wage + OT, cash or off-books); free wage claim (state + federal labor depts, no pay to get paid); free help (legal aid, worker centers, state AG, no-upfront-fee employment lawyers); rights generally do not depend on status (need not prove status to be owed); keep your own record (hours/dates/pay/texts, no perfect paperwork needed); never pay to claim your own wages; the weight (hands, family, church, another man in the pews shorted the same way who filed free + got paid). Scam spine: WAGE-RECOVERY/BACK-PAY SHARK (upfront fee or big cut for what labor dept does free), GUARANTEED-RECOVERY/PAY-TO-SPEED-IT-UP, LABOR-DEPT/GOVERNMENT IMPOSTER + FAKE CLAIM-RELEASE (fee, gift cards, SSN/bank login/docs to release-your-back-pay/process-your-claim/verify-identity), and THE EMPLOYER LIE (cash pay/off-books/unsigned/your-status means no claim). Flat rule stated: hours = wages generally owed; free wage claim exists; free help exists; no honest helper charges a big upfront fee/cut; a real agency never demands gift cards or SSN by text to release back pay; cash pay + immigration status do NOT erase the right to be paid -- anyone charging to claim his own wages, guaranteeing a recovery, demanding gift cards/SSN, or saying cash/status = no rights is the scam/thief. SEPARATE caution: real state+federal labor depts, real legal aid, honest worker centers, honest no-upfront-fee employment lawyers are NOT scams; the caution is the fee-charging recovery shark, guaranteed-recovery pitch, government imposter, and the boss lie. AI in quiet-helper + augment-not-replace (explains wage claim / min wage / overtime / off-the-books / wage theft / final paycheck / retaliation / misclassification; helps him understand a pay stub or text, organize hours+dates+pay+messages, draft a wage-claim request, find the labor dept / worker center / legal aid, and spot the scam -- does NOT act as his lawyer, does NOT tell him what he is owed or that he will win, does NOT give legal advice, does NOT negotiate/file, does NOT promise an outcome, never fed his SSN / bank login / documents). Compliance stated TWICE in-body (general navigation, NOT legal advice and NOT a determination of what he is owed or whether he will win; only the labor dept or a court decides a wage claim, a licensed attorney advises his case; verify with the state labor dept, a worker center, or legal aid; NEVER pay an upfront fee for free help, never gift cards, never hand SSN / bank login / documents to a recovery company, use official state+federal labor depts + free worker-center/legal-aid help). Dignity, never deficit (a man who did the hours earned that money; getting cheated is not proof he is foolish -- the shame belongs to the boss who kept the pay). Rotated gender to a MAN off the woman 59 (#240) and set a fresh AGE 44 -- a working man who did the labor and did not get the pay, distinct from the home-health aide of #240 and the warehouse worker of #239. Opens a WHOLLY NEW DOMAIN (THE PAY YOU EARNED AND DID NOT GET) distinct from workers-comp #239 (paid care + wage benefits for an INJURY, not pay for hours worked), unemployment #224 (a state benefit after a job ends, not wages withheld), and medical debt #240 (a bill he owes, not a paycheck he is owed), in a DIGNITY-OF-THE-EARNED-WAGE frame, keeping the scam-prevention spine. Serves The Plug AI community + working-family + digital-literacy pillars AND BigHeart Health church partnerships + the working men in the pews who did the labor and did not get the pay. Named geography: Cicero, Berwyn, Blue Island, Chicago Heights, Summit, Melrose Park, Bridgeview, Harvey, Dolton, Markham. Saved to output/linkedin-2026-08-26-wage-theft-unpaid-wages-free-labor-department-help-legal-aid-worker-center-recovery-fee-imposter-cash-status-no-rights-lie-scam-ministry.md. PRIOR (#240): medical debt / hospital charity care (home-health aide) + itemized-bill rights + free financial counselors/legal aid + relief-fee/guaranteed-wipeout/collector-imposter scam, woman 59. PRIOR (#239): workers compensation for a job injury (warehouse worker) + free state help + no-upfront-fee attorney + claim-consultant-fee/guaranteed-settlement/imposter scam, man 48. PRIOR (#238): special education / IEP (working mother) + free Parent Training center/advocate + paid-advocate-shark/guaranteed-placement/fake-grant scam, woman 38. The plug is in."
runs_completed: 241
items_processed: 366
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
