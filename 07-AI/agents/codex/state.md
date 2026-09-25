---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-25T13:20:00Z"
current_task: "Run 379 (fleet review). Nothing to build — fix queue is 100% covered, so the meaningful unit was keeping the merge runbook trustworthy for the owner. Re-ran the authoritative per-repo sweep across ALL 24 non-archived repos and LIVE-verified every claim in MERGE-RUNBOOK-2026-09-24.md still holds: still 0 merges/closes fleet-wide since ~Sep 11-12 (last-merged SHAs unchanged: JobScout #24@09-11, Community #13@09-12, EFA #23@09-11, avrg #25@09-10, content #1@Jun6); all 32 open agent PRs + 7 non-agent PRs = 39 still MERGEABLE; Community 10 fix/* non-default stacked bases (#17/#19/#21/#25/#27/#29/#31/#33/#35/#37) + content #4/#8 stacking confirmed; Section 6 behind_by currency holds (psychic #1(+7800)/#25, Link-inbio #5/#15, kai-vault #3 all behind_by:0; Link-inbio #6 still +0/-0 behind 13 -> CLOSE stale; kai-vault #2 behind 7 but CLEAN). Coverage spot-PROVED on JobScout (deepest, 19 open issues): every issue maps to a covering PR (#66->#67, #64->#65, #62->#63, cadence tower #30-#59 -> keystone #61, #26->#27) -> no new uncovered issue anywhere. Corrected R378 off-by-one: 32 open agent PRs, not 33 (no PR closed; 6+14+5+5+2). DELIVERABLE: added R379 LIVE RE-VERIFICATION banner + title/footer stamp to the EXISTING runbook (NOT a 7th merge doc — Stef flagged sprawl). No code changed, no merges executed (reserved for owner)."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; R379 LIVE-confirmed still 0 merges since ~Sep 11-12; 39 open MERGEABLE PRs fleet-wide (32 agent + 7 non-agent); EVERY open code issue has a covering PR -> DO NOT ship new tower PRs, the whole job now is to help the owner MERGE). The execute-ready plan is MERGE-RUNBOOK-2026-09-24.md (Sections 1-5 agent fleet, Section 6 non-agent) — R379 re-verified LIVE-accurate 2026-09-25 ~13:15 UTC, execute AS WRITTEN. Agent-fleet merge order: JobScout(default claude/clever-cannon-IDh3G) merge #61(keystone,NO closing kw)->#63/#25/#27/#65/#67 then hand-close 30/32/34/36/38/41/43/45/47/49/51/53/55/57/59; Community(claude/quirky-galileo-UGnfz) merge #38(keystone,NO closing kw)->CLOSE 12 siblings 15/17/19/21/23/25/27/29/31/33/35/37 (10 non-default stacked=UI-merge is a silent no-op)->hand-close issues 14/16/18/20/22/24/26/28/30/32/34/36->merge #40; EFA(claude/keen-noether-VED1j) merge #25 FIRST(test-glob)->#26/#27/#29/#31 (recheck #31 after #29); content(claude/eloquent-edison-aF7yG) merge #2->retarget #4 base->default->merge #4->#6->#9->CLOSE #8; avrg(main) merge #27(auto-closes #26+#28)+#31(auto-closes #30). Section 6: psychic-bassoon merge #1+#25; Link-inbio merge #5+#15, CLOSE #6(stale empty-diff behind13); kai-obsidian-vault merge #3 +#2(confirm current, behind7). Owner-only remainders: EFA #30(schema persist)/#24(retire main), avrg #5(Supabase), forming-paws #8(founder IL-SOS filing). NEXT: nothing to build/certify anywhere — pure owner-MERGE. Each loop re-run the per-repo sweep of ALL non-archived repos (never account-wide search) to catch a 6th agent repo OR new non-agent backlog OR a newly-filed issue lacking a covering PR."
runs_completed: 379
items_processed: 701
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
