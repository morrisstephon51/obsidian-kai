---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-25T04:42:53Z"
current_task: "Run 377 (fleet review). Ran a full-fleet PER-REPO issue sweep (account-wide gh search drops repos) and found a 5TH active agent repo the R376 runbook missed: ai-video-reel-generator (avrg; trends->avatar-video->clip->schedule->post loop, default branch=main). Same owner-merge-blocked state as the other 4: 2 MERGEABLE fix PRs, 0 merges since Sep 11. #27 (MERGEABLE, closingRefs #26+#28) removes a fail-closed ADMIN_SECRET guard that made the app's PRIMARY output 'Schedule for Publishing' return 401 in EVERY config (also silently no-op'd Remove persona); PR #29 (the #28-only fix) was correctly closed as redundant. #31 (MERGEABLE, closes #30) anchors best-post-times to America/New_York vs server-UTC (every auto-post fired 4-5h early; dev/prod diverged). Both PRs carry PROPER closing keywords -> auto-close on merge, NO hand-close loop (opposite of the JobScout #61 / Community #38 keystones which have closingRefs=[]). Only owner-only remainder: issue #5 (provision live Supabase). Re-verified the original 4 repos LIVE: STILL 0 merges since ~Sep 11-12, all covering PRs still MERGEABLE, runbook merge sequences unchanged. DELIVERABLE: amended MERGE-RUNBOOK-2026-09-24.md -> added Section 5 (avrg merge sequence: #27 then #31, order-independent/disjoint files), an R377 amendment banner, updated Situation to '5 agent repos not 4', updated Net effect. No code changed, no merges executed (reserved for owner per governance)."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; 0 merges since R320; ~42 open MERGEABLE PRs across 5 repos; EVERY open code issue has a covering PR -> DO NOT ship new tower PRs, help the merge). FLEET IS 5 REPOS NOT 4 (R377 fix): the 4 known agent repos + ai-video-reel-generator (avrg, default=main). R377 amended MERGE-RUNBOOK-2026-09-24.md to add avrg as Section 5. EXECUTE-READY MERGE PLAN (all MERGEABLE 2026-09-24): JobScout(default claude/clever-cannon-IDh3G): merge #61(keystone,NO closing kw)->#63/#25/#27/#65/#67; #61&#63 both scorer.py so recheck #63 after #61; then HAND-CLOSE cadence issues 30/32/34/36/38/41/43/45/47/49/51/53/55/57/59. Community(default claude/quirky-galileo-UGnfz): merge #38(keystone,NO closing kw)->CLOSE 12 superseded siblings 15/17/19/21/23/25/27/29/31/33/35/37 (10 non-default stacked=UI-merge is a silent no-op)->HAND-CLOSE issues 14/16/18/20/22/24/26/28/30/32/34/36->merge #40(web email). EFA(default claude/keen-noether-VED1j): merge #25 FIRST(test-glob)->#26/#27/#29/#31; #29&#31 both scorer.ts so recheck #31 after #29; #30(upsertPerformance)+#24(retire main)=OWNER-ONLY. content(default claude/eloquent-edison-aF7yG): merge #2->retarget #4 base->default then merge #4->merge #6->merge #9->CLOSE #8(redundant). avrg(default main): merge #27(auto-closes #26+#28; reverses hardening #20/#14=your-call)->merge #31(auto-closes #30); both HAVE closing kw so NO hand-close; #5(Supabase provisioning)=OWNER-ONLY. Fleet owner-only remainders: EFA #30/#24 + avrg #5. NEXT: nothing to build/certify — fix queue complete across all 5 repos; pure owner-MERGE. Each loop, re-run the PER-REPO gh issue sweep (never rely on account-wide gh search) to catch any new 6th repo."
runs_completed: 377
items_processed: 692
last_error: null
color: "#00FF88"
house: "dev-lab"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent codex`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from codex --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent codex`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Codex is a per-task coding agent. Runs, does work, and exits.
- Reports into clawd via the shared bus on task completion.
