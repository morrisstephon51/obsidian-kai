---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: running
last_run: "2026-08-27T19:10:00Z"
current_task: "Run 227: scan context + summarize priorities + one meaningful unit. MEANINGFUL UNIT = full live gh re-verify of the entire founder-action frontier (owner morrisstephon51) + precise coldness re-measure + refreshed the antigravity digest PRIORITIES.md to Run-227 live state. DELTA vs Run 226 = ZERO: nothing merged, nothing signed, nothing closed; board aged ~0.66 day. LIVE-CONFIRMED THIS RUN: jobscout #7-#16 all 10 OPEN/MERGEABLE non-draft, single shared base claude/clever-cannon-IDh3G, last merge still #6 (2026-07-18) => 39.92d cold, zero of #7-#16 landed. psychic-bassoon #22(date,closes #21)+#20(CVE Next 14.2.35)+#19(headers)+#1 all OPEN/MERGEABLE/CLEAN non-draft, #11 DRAFT MERGEABLE, last merge still #18 (2026-08-14T19:04Z) => 13.00d cold. forming-paws 0 open PRs, issue #8 open (founder IL filing). psychic issue #21 still open (auto-closes when #22 merges). STEF GATE STEF-WEEK-1-APPROVAL.md byte-frozen 3125b/mtime 2026-08-11T09:31:48Z, still APPROVAL REQUESTED => 16.40 DAYS COLD. ACCOUNT FRONTIER: 15 open PRs/2 repos (14 non-draft MERGEABLE + 1 draft #11) + 1 cold gate + 3 open issues (#21 / forming-paws #8 / avrg #5). NET: ZERO code blockers; bottleneck 100% founder-authority. Highest-value single click stays psychic #20 (published-CVE Next.js patch, 13.00d unmerged); suggested order #20 CVE -> #22 date-fix -> #19 headers. TOOLING NOTE: ~/clawd writes are PERMISSION-GATED this session (Run 226 had them open) — could not refresh ~/clawd/AI-Organization/FOUNDER-ACTION-QUEUE.md; its substance is unchanged from Run 226, only coldness figures advanced (jobscout 39.3->39.92 / psychic 12.3->13.00 / gate 15.74->16.40). Live Run-227 numbers captured in PRIORITIES.md instead. HANDOFF: next loop re-measure gate coldness + re-check merges (jobscout #7-#16 / psychic #19/#20/#22 / gate signature); if ~/clawd is writable again, propagate these Run-227 figures into FOUNDER-ACTION-QUEUE.md; if #22 merged confirm #21 auto-closed; if any jobscout PR merges confirm clever-cannon->main promotion path; forming-paws #8 filing is a live founder item until Stef files or defers."
runs_completed: 227
items_processed: 946
last_error: null
color: "#F4B942"
house: "launchpad"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent antigravity`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from antigravity --topic <topic> --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent antigravity`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Antigravity is a per-task general-purpose agent. Invoked on demand.
- Reports into clawd via the shared bus on task completion.
- me.md no longer exists; context.md is the canonical replacement (per its own header, updated 2026-07-08). Loop-start step 2 is a legacy reference — context.md covers it.
- ~/clawd writes are intermittently permission-gated (open Run 226, gated Run 227). When gated, land the digest in PRIORITIES.md (writable) and flag the FOUNDER-ACTION-QUEUE.md refresh as pending in the handoff.
