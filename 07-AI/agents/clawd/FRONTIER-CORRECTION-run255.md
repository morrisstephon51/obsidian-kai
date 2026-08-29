# Frontier Correction — clawd Run 255 (2026-08-29T19:38Z)

**Why this memo exists:** `~/clawd/AI-Organization/FOUNDER-ACTION-QUEUE.md` (antigravity Run 229, verified 2026-08-29T05:48Z) still headlines **"17 open PRs / 4 repos."** Source-verified live this run, the true frontier is **18 open PRs / 5 repos.** The queue is one whole repo behind reality. `~/clawd` writes are harness-permission-gated this session (OS reports the file writable, but the write-tool is blocked), so — exactly as in Runs 253/254 — I cannot patch the canonical file directly; this memo + a bus route to antigravity carries the fix.

## The single defect: the 5th repo is invisible to the founder

antigravity Run 229's footer lists the repos it enumerated as *job_opportunity_scanner, psychic-bassoon, ai-video-reel-generator, Enrollment_Funnel_Agent, forming-paws*. That is 5 names, but **forming-paws has 0 open PRs** — it was counted as the "5th repo" while the repo that actually holds an open, mergeable PR was never checked:

- **`-Community_intake_Routing` PR #2** — `fix(classify): intake keywords matched as substrings misroute learners (fund/invest/serve/teach)`
  - **OPEN · non-draft · MERGEABLE · CLEAN** (live `gh pr view 2 --repo morrisstephon51/-Community_intake_Routing`, 2026-08-29T19:38Z)
  - base `claude/quirky-galileo-UGnfz` (repo default), **+31/−7**, 2 files: `api/intake.js`, `intake.js`, 0 open issues
  - created 2026-08-28T03:03:30Z
  - **Same defect class as jobscout #7/#8 and Enrollment #14:** intent keywords matched as raw substrings misroute people (fund/invest/serve/teach). One-click mergeable into the repo default **now.**

This PR was first surfaced by clawd Run 254 and routed to antigravity; Run 229 folded in the *Enrollment #14* correction but not this one. It has now been missed by two antigravity runs.

## Corrected account-wide frontier — 18 open PRs / 5 repos (17 non-draft MERGEABLE/CLEAN + 1 draft)

| Repo | Open PRs | Notes |
|------|----------|-------|
| job_opportunity_scanner | #7–#16 (10, non-draft) | base `clever-cannon` default; codex Run 236/239 empirically batch-merged 10/10 CLEAN + 58 pytest green — any order, no rebases |
| psychic-bassoon | #22, #20, #19, #1 (non-draft) + #11 (draft) | order #20 CVE → #22 (closes #21) → #19 → **#1 last** (edit/delete conflict w/ #22 on `lib/utils.ts`, 1 manual resolve — keep #1's dead-code `formatShortDate` deletion) |
| ai-video-reel-generator | #25 (non-draft) | base `main`; shared-mutable-state fix, +5/−1 |
| Enrollment_Funnel_Agent | #14 (non-draft) | base default `claude/keen-noether-VED1j`; substring-misroute csv fix, +18/−6 |
| **-Community_intake_Routing** | **#2 (non-draft) ← MISSING FROM QUEUE** | base default `claude/quirky-galileo-UGnfz`; substring-misroute intake fix, +31/−7 |

Non-draft one-click-mergeable = **17** (jobscout 10 + psychic 3 + avrg 1 + Enrollment 1 + Community_intake **1** — psychic #1 is the +1 non-draft that needs the manual resolve, so 16 clean-any-order + #1). Draft = psychic #11. Total open on production repos = **18 / 5 repos.**

> Note: `gh search prs --owner morrisstephon51 --state open` returns ~30 open PRs total, but the extra ~12 are all **drafts** on vault/doc/scaffolding repos (obsidian-kai, kai-obsidian-vault, content-machine #3/#4/#5/#10, Link-inbio #5/#6, command-center-redirect #1, Workspace-notes #1) — correctly excluded from the founder merge queue. The 18/5 count is the production-code frontier.

## What is NOT wrong (verified, no change needed)

- The psychic #1 ↔ #22 edit/delete merge-order hazard (codex Run 239) is **correctly captured** in the queue — re-confirmed live: #22 is CLEAN and touches `lib/utils.ts` + `tests/utils.date.test.ts`.
- jobscout batch-safety, avrg #25, Enrollment #14, and the Stef Week-1 gate details are accurate.
- Frontier delta vs Run 254 = **ZERO merged/closed** — nothing regressed; the only change is this run's more-complete enumeration.

## Action for antigravity (next refresh)

1. Add **-Community_intake_Routing #2** to the 🟢 PR REVIEW QUEUE as its own repo section (mirror the Enrollment #14 block).
2. Correct every headline count **17/4 → 18/5** (lines ~12, ~26, and the footer roll-up).
3. Fix the "all 5 active repos" verified-line — enumerate via `gh search prs --owner morrisstephon51 --state open` so no owned repo is ever silently dropped again; forming-paws (0 PRs) is not the 5th repo.
4. Keep everything else as-is.

**Bottleneck remains 100% founder-authority** — zero code blockers. This memo only corrects visibility, not merge-readiness.
