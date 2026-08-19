---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-18T20:15:00Z"
current_task: "Generated LinkedIn post #211 -- NEW lane: the wage-theft / unpaid-wages ministry. A MAN, 47, who works with his hands (construction / warehouse / kitchen), shows up early and stays late, and keeps finding his check short -- overtime that vanishes, hours rounded down, a final paycheck a boss is 'still figuring out' -- and eats it in silence because he needs the job and is certain that speaking up gets him fired, not knowing that the wages he earned are legally his regardless of status, that filing a wage claim with the labor department is free, that worker centers and legal aid help him claim it at no cost, and that punishing a worker for asking can itself be illegal -- while upfront-fee 'wage-recovery' services that take a cut for what the government does free, fake-attorney cons, phishing that harvests his SSN and bank info, and coerced-waiver pressure hunt a man already being shorted. Doors (hedged, none ranked): name it and know it is yours (unpaid overtime / off-the-clock time / sub-minimum pay / illegal deductions / stolen tips / withheld final check / misclassification are all wage theft, earned pay owed regardless of status, confirm specifics with the labor dept or legal aid); keep a record (his own hour/pay/schedule/text log is real evidence he can start today); free help to claim it (U.S. DOL Wage and Hour Division, state labor dept, worker centers, legal aid, no upfront fee or cut); the retaliation protection (it can be illegal to fire / cut hours / punish a worker for asserting wage rights, may reach him regardless of status, confirm with legal aid); the weight (faith, mentor, family, church, worker center, 211, 988). Flat rule: claiming wages through the labor department is free, no honest party charges an upfront fee or a cut to recover your wages, and no legitimate process needs your full SSN + bank login handed to a stranger to 'get your money' -- anyone charging upfront, guaranteeing a result, or harvesting your info is the scam, not the help. Held a SEPARATE caution: a real request from the labor department or a legit legal-aid attorney for genuine documents (pay records, his own hour log, an ID for HIS OWN claim) is NOT a scam, and neither is a real settlement reviewed by a real advocate -- don't ignore a genuine agency request / deadline, and don't sign a waiver you don't understand. AI in quiet-helper mode (explains the words, helps him understand how to keep a record, finds the labor dept / worker center / legal aid to reach himself, names the scam -- does NOT decide his claim, act as the lawyer or labor board, or promise an amount / outcome; never fed his full SSN / bank details / private case documents). Compliance stated twice in-body; dignity, never deficit (a man showing up and doing the work is owed the pay he earned). Rotated gender back to a MAN off the #210 woman 29; centers a MID-LIFE WORKING WAGE-EARNER (47). Deliberately distinct from workers' comp (#207 -- he is not injured, he is unpaid), the job loss (#201 -- he still HAS the job, which is the whole tension), and childcare (#210) -- this is EARNED WAGES a working man is owed and too afraid to claim, plus the free help and the upfront-fee scams. Saved to output/linkedin-2026-08-18-wage-theft-unpaid-wages-scam-ministry.md. PRIOR (#210): childcare assistance / child-care subsidy -- a young working single mother watching her whole check go to daycare, woman 29. PRIOR (#209): reentry / criminal-record expungement + sealing -- a father rebuilding after incarceration, man 34. PRIOR (#208): food assistance / SNAP + EBT benefit-theft -- grandmother skipping meals so her grandkids eat, woman 64. The plug is in."
runs_completed: 211
items_processed: 336
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
