---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-09-25T21:42:00Z"
current_task: "Run 381 (fleet review). Re-ran the authoritative per-repo sweep across ALL 25 non-archived repos. The 5 agent repos + 4 Section-6 non-agent repos are byte-identical to R380 (JobScout 19i/6pr, Community 13i/14pr, EFA 3i/5pr, avrg 4i/2pr, content 3i/5pr; psychic-bassoon 0i/2pr, Link-inbio 0i/3pr, kai-obsidian-vault 0i/2pr, forming-paws 1i/0pr) -> still 0 merges fleet-wide, every agent-fleet code issue still has a covering PR, ZERO uncovered. NEW this run: the sweep surfaced TWO repos with open items that the runbook Section 6 never listed -> investigated + classified BOTH as NON-actionable (no PR, no merge): (1) skills-introduction-to-git #1 is the GitHub-Skills COURSE exercise tracker (repo templated from skills/introduction-to-git, issue auto-opened by app/github-actions) = a learning artifact not a code defect; (2) ----Workspace-notes-2025-01-07_notes.md PR #1 is the owner's own DRAFT (isDraft:true) Obsidian master-vault build (+2677/-0, 24 files) = unmergeable until Stef marks it ready, owner-only. DELIVERABLE: appended an R381 completeness note to the EXISTING MERGE-RUNBOOK-2026-09-24.md (no new file -- sprawl flagged) + updated memory agent-fleet-is-five-repos-not-four with the classify-by-author/draft-state lesson. Now every non-archived repo is accounted for. No code changed, no merges executed (reserved for owner). Bottleneck remains SOLELY owner-merge."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; R381 re-confirmed still 0 merges since ~Sep 11-12; ~39 open MERGEABLE PRs fleet-wide; EVERY agent-fleet code issue has a covering PR -> DO NOT ship new tower PRs, the whole job is to help the owner MERGE). Execute-ready plan is MERGE-RUNBOOK-2026-09-24.md (Sections 1-5 agent fleet, Section 6 non-agent, R381 completeness note at the tail) -- re-verified unchanged 2026-09-25 ~21:40 UTC, execute AS WRITTEN. Agent-fleet merge order: JobScout(default claude/clever-cannon-IDh3G) merge #61(keystone,NO closing kw)->#63/#25/#27/#65/#67 then hand-close 30/32/34/36/38/41/43/45/47/49/51/53/55/57/59; Community(claude/quirky-galileo-UGnfz) merge #38(keystone,NO closing kw)->CLOSE 12 siblings 15/17/19/21/23/25/27/29/31/33/35/37 (10 non-default stacked=UI-merge is a silent no-op)->hand-close issues 14/16/18/20/22/24/26/28/30/32/34/36->merge #40; EFA(claude/keen-noether-VED1j) merge #25 FIRST(test-glob)->#26/#27/#29/#31 (recheck #31 after #29); content(claude/eloquent-edison-aF7yG) merge #2->retarget #4 base->default->merge #4->#6->#9->CLOSE #8; avrg(main) merge #27(auto-closes #26+#28)+#31(auto-closes #30). Section 6: psychic-bassoon merge #1+#25; Link-inbio merge #5+#15, CLOSE #6(stale empty-diff behind13); kai-obsidian-vault merge #3+#2(confirm current, behind7). Owner-only remainders: EFA #30(schema persist)/#24(retire main), avrg #5(Supabase), forming-paws #8(founder IL-SOS filing). NON-actionable (do NOT re-flag as uncovered): skills-introduction-to-git #1 (GitHub-Skills course bot issue), ----Workspace-notes-2025-01-07_notes.md PR #1 (owner draft vault build). NEXT: nothing to build/certify anywhere -- pure owner-MERGE. Each loop re-run the per-repo sweep of ALL non-archived repos (never account-wide search); classify new items by author (app/github-actions=course bot) + draft state before treating as an uncovered gap."
runs_completed: 381
items_processed: 704
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
