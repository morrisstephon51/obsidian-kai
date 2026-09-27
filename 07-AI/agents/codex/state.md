---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-09-27T08:05:00Z"
current_task: "Run 389 (executed the audit R388's carryover asked for: \"other unconditional close_pr calls that assume a prior merge landed\"). FOUND THE SAME BUG CLASS AT 39x THE SCALE, on the two biggest keystones. merge_ready downgrades an unmergeable PR to a [skip] and keeps going; THREE follow-up blocks then ran UNCONDITIONALLY, each asserting in its posted GitHub comment that a keystone had landed: JobScout's 15 hand-closes of issues #30-#59 (\"Fixed by #61\"), Community's 12 sibling PR-closes #15-#37 (\"Superseded by #38\"), and Community's 12 issue hand-closes #14-#36 (\"Fixed by #38\"). The Community pair is the worst: those 12 PRs are the ONLY other fixes for those 12 issues, so closing them as superseded with #38 absent ERASES THE WHOLE FIX SURFACE for that repo and leaves 12 issues marked fixed -- silently, since the summary still prints \"Issues closed: 27\". PROVEN NOT ASSERTED: built a stateful fake-gh harness (/tmp/ghsim) that reproduces the live dry run exactly (23/14/1/27/4), then forced each keystone UNMERGEABLE and diffed unpatched vs patched. Unpatched scenario B = 21 merges but still 14 PR-closes + 27 issue-closes; patched = 21/2/0 with 2 [HOLD]. Scenario A (happy path) IDENTICAL in both, scenario C (#9 unresolvable) IDENTICAL in both -> R388's gate survived the refactor, scenario D adds a WARN without blocking. Also verified IDEMPOTENT: a 2nd --execute pass issues 0 mutating actions and does not spuriously HOLD. FIX: shared require_merged <repo> <pr> <what> now wraps all three blocks AND R388's #8 case (one helper, four sites); in --execute it demands state==MERGED, in dry-run it PREDICTS from live mergeability rather than assuming success (else the dry run promises 27 closes that --execute would correctly refuse). Added warn_unless_merged for EFA #32/#29, where HOLDING would be worse than proceeding -- #29 carries the real code fix for #28, so it still merges but the owner is told #28 will auto-close with only the tautological engagement-parity.test.ts behind it. retarget now checks state before firing/counting. NET EFFECT ON THE OWNER'S PLAN IS UNCHANGED (23 merges / 14 PR-closes / 1 retarget / 27 issue-closes / 4 draft-skips) -- the gates engage only when something has already gone wrong. TWO SURFACE FACTS: (1) a closing keyword in a PR TITLE does NOT auto-close -- agent_I_content #8 is titled \"(closes #7)\" with closingIssuesReferences=[] while #9 carries the real closes=[7]; harmless here because the plan merges #9, but the inverse order would have orphaned #7, so read the API field never the title. (2) Every open issue fleetwide still has a covering MERGEABLE PR or is owner-only (JobScout #26<-#27 and content #7<-#9 were the two that looked unaccounted for; both covered) -> zero new fix PRs warranted. Live sweep: 41 open PRs across the 9 active repos, 0 unmergeable, 5 drafts but only 4 draft-SKIPS because Link-inbio #6 is a draft being CLOSED as stale, not merged. R389 addendum written to MERGE-RUNBOOK-2026-09-24.md; bash -n clean; live dry-run re-verified."
carryover: "CARRYOVER (owner-MERGE is the SOLE bottleneck; ~15 days, 0 merges since Sep 11-12). R389 RULE -- AUDIT THE WHOLE SCRIPT FOR A BUG CLASS, NOT JUST THE SITE WHERE YOU FOUND IT. R388 found one unconditional follow-up and patched that one site inline; the same class was live on the two biggest keystones at 39x the scale. When you fix a 'skipped merge + unconditional follow-up' hazard, grep EVERY close_pr/close_issues/auto-close for the keystone it silently presumes, and prefer ONE shared gate over N inline checks. SECOND R389 RULE -- A DRY RUN THAT ASSUMES SUCCESS IS A LYING DRY RUN. The obvious `|| [ \"$DRY\" -eq 1 ]` shortcut makes the dry run promise actions --execute would correctly refuse; gate dry-run on live PREDICTED mergeability instead, so plan and execution agree. THIRD -- NOT EVERY DEPENDENCY SHOULD HOLD: if the dependent action carries a correct fix (EFA #29 for #28), warn loudly and proceed; reserve HOLD for actions that would mark work DONE with no covering code. FOURTH -- a closing keyword in a PR TITLE does NOT auto-close; only the body registers (agent_I_content #8 title says 'closes #7', closingIssuesReferences=[]). Verify via the API field. HARNESS PATTERN WORTH REUSING: a stateful fake `gh` on PATH (plus a fake `git` so a resolver cannot touch the remote) reproduced the live plan exactly and let me mutation-test the gates in --execute mode against zero real repos; keep /tmp/ghsim's shape in mind (key state by OBJECT TYPE -- my first stub conflated PR and issue numbers and produced a false idempotency failure). CARRY R388's RULES: mutation-testing a helper is necessary but not sufficient -- also UNHOOK THE CALL SITE (leave the helper byte-identical, no-op its call, confirm tsc clean, re-run; if green the guard is blind). And a SKIPPED merge can be worse than a failed one. STATUS: all 5 agent queues execution-proven -- JobScout keystone #61 (R357/R385), Community keystone #38 (R386), EFA + hardened PR #32 (R387), agent_I_content + hardened PR #10 (R388); merge-fleet.sh gate-hardened (R389). Never merge Community #23 (nor #25/#27/#29/#31/#33/#37 stacked on it): they drop genuine volunteers. DO NOT ship new tower PRs -- every open issue fleetwide has a covering MERGEABLE PR. Runbook is BOTH prose (MERGE-RUNBOOK-2026-09-24.md) AND executable (merge-fleet.sh): Stef runs `./merge-fleet.sh` (dry-run, safe) then `./merge-fleet.sh --execute`. Net effect 23 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips. The 4 draft PRs (psychic #25, Link-inbio #5, kai-vault #2+#3) stay OWNER-ONLY until Stef clicks Mark ready for review. EFA order #25->#26->#27->#32->#29->#31. Owner-only remainders: EFA #30 schema-persist/#24 retire main, avrg #5 Supabase, forming-paws #8 (IL-SOS filing), + the 4 Section-6 drafts. NON-actionable (do NOT re-flag): skills-introduction-to-git #1 (course bot), ----Workspace-notes PR #1 (owner draft)."
runs_completed: 389
items_processed: 757
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
