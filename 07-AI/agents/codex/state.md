---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-15T14:36:22Z"
current_task: "Run 323 (review GitHub repos / fix open issues). Bus: 0 routing owed (all self-running peers). Standing state confirmed live: 9 open PRs across 5 repos, ALL [MERGEABLE] and stalled on OWNER MERGE (nothing merged since run 320); every filed code issue already has an open PR. Did NOT pile a redundant PR. UNIT OF WORK -- found a NEW uncovered same-class bug in -Community_intake_Routing (no open issue/PR): partner keyword list still contains the affiliation/context nouns 'organization'/'organisation' -- identical class to business/company/enterprise/agency (dropped #9) and brand/corporate (dropped #14/PR#15). A single incidental match clears the 0.7 evidence-only threshold -> org-affiliated LEARNERS misroute to the founder inbox with confidence 0.99 and never get the learner welcome email. Especially acute for The Plug AI's core audience (faith communities, community orgs) who self-describe via 'our organization'. PROVEN empirically via faithful classify() replica: 3 faith/community-org learners route partner(0.99) CURRENT -> learner after dropping org/organisation; control learner unchanged; a GENUINE partner ('organization would love to collaborate and sponsor') still routes partner(0.99) because collaborate/sponsor match -> fix costs no real partner signal. Present in BOTH intake.js and api/intake.js (kept in lockstep). Verified PR#15 already fixes BOTH copies in lockstep + parity-tests cli+api (twin-drift NOT an issue here). Right-sized action (owner-merge is the bottleneck; do not pile a 10th PR; fix edits the exact keyword-array hunk PR#15 already rewrites): filed tracking issue #16 with the confidence math + proof table + exact 2-file fix, AND posted a fold-in proposal on PR#15 (issuecomment-5682107890) so it closes in the SAME merge with no new branch/PR. Flagged investor/b2b as lower-confidence secondary same-class candidates for owner judgment (not in the tight fix). MERGE-RUNBOOK-2026-09-15.md order still holds; owner-only items unchanged (Enrollment #24 retire stale main, ai-video-reel #5 Supabase setup)."
runs_completed: 323
items_processed: 599
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
