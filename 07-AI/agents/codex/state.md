---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-25T22:15:00Z"
current_task: "Run 382 (fleet review). Unit of work: ran the first LIVE MERGE-READINESS AUDIT (isDraft + mergeable + mergeStateStatus, not just behind_by currency) of every runbook-target PR. Agent fleet (Sections 1-5) all clean: 32 PRs (JobScout 6, Community 14, EFA 5, content 5, avrg 2) every one MERGEABLE/CLEAN/non-draft, no conflict drift after ~2 weeks; JobScout issue->PR coverage re-proven 100% live (#66->#67, #64->#65, #62->#63, #26->#27, cadence tower #30-#59 -> keystone #61); Community 10 non-default stacked bases + content #4/#8 stacking confirmed. DEFECT FOUND + FIXED: 5 of Section 6 six `gh pr merge` commands targeted DRAFT PRs and would have died on 'Pull request is in draft state' -- psychic-bassoon #25=DRAFT, Link-inbio #5=DRAFT and #6=DRAFT, kai-obsidian-vault #2=DRAFT and #3=DRAFT (only psychic #1 + Link #15 are merge-ready). Prior R378/R379 checked behind_by but never isDraft. All 4 content-drafts are owner-editorial WIP = OWNER-ONLY until Stef marks Ready. Corrected MERGE-RUNBOOK-2026-09-24.md blocks 6a/6b/6c (commented out draft merges w/ OWNER-ONLY note), Net effect (6+1 -> 2 executable merges #1/#15 + 1 close #6), header, remaining-items list, + appended R382 note. Updated memory agent-fleet-is-five-repos-not-four + MEMORY.md. Sweep byte-identical to R381 (JobScout 19i/6pr, Community 13i/14pr, EFA 3i/5pr, avrg 4i/2pr, content 3i/5pr; psychic 0i/2pr, Link-inbio 0i/3pr, kai-vault 0i/2pr, forming-paws 1i/0pr); still 0 merges fleet-wide. No code changed, no merges executed (reserved for owner)."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; R382 re-confirmed 0 merges since ~Sep 11-12; every agent-fleet code issue has a covering MERGEABLE PR -> DO NOT ship new tower PRs; the job is to help the owner MERGE cleanly). Execute-ready plan is MERGE-RUNBOOK-2026-09-24.md, now draft-state-corrected R382. KEY R382 CORRECTION: Section 6 (non-agent) had 5 merge commands pointed at DRAFT PRs (would fail) -> executable Section-6 total is 2 merges (psychic #1, Link-inbio #15) + 1 close (Link #6); the 4 DRAFTS (psychic #25, Link #5, kai-vault #2 + #3) are OWNER-ONLY until Stef clicks Mark ready for review. Agent-fleet merge order UNCHANGED: JobScout(default claude/clever-cannon-IDh3G) merge #61(keystone,NO closing kw)->#63/#25/#27/#65/#67 then hand-close 30/32/34/36/38/41/43/45/47/49/51/53/55/57/59; Community(claude/quirky-galileo-UGnfz) merge #38(keystone,NO closing kw)->CLOSE 12 siblings 15/17/19/21/23/25/27/29/31/33/35/37 (10 non-default stacked=UI-merge is a silent no-op)->hand-close issues 14/16/18/20/22/24/26/28/30/32/34/36->merge #40; EFA(claude/keen-noether-VED1j) merge #25 FIRST-> #26/#27/#29/#31 (recheck #31 after #29); content(claude/eloquent-edison-aF7yG) merge #2->retarget #4 base->default->merge #4->#6->#9->CLOSE #8; avrg(main) merge #27(auto-closes #26+#28)+#31(auto-closes #30). Owner-only remainders: EFA #30(schema persist)/#24(retire main), avrg #5(Supabase), forming-paws #8(founder IL-SOS filing), + the 4 Section-6 draft PRs. NON-actionable (do NOT re-flag as uncovered): skills-introduction-to-git #1 (course bot), ----Workspace-notes PR #1 (owner draft). NEXT: nothing to build anywhere -- pure owner-MERGE. Each loop re-run the per-repo sweep of ALL non-archived repos AND audit isDraft+mergeable+mergeStateStatus on every merge target (behind_by alone is not merge-readiness); classify new items by author + draft state before treating as an uncovered gap."
runs_completed: 382
items_processed: 705
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
