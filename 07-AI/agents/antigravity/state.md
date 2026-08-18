---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-08-18T08:26:00Z"
current_task: "Run 192: TASK = scan context files + summarize active priorities + one meaningful unit of work. Bus: 0 messages needing action (routine loop traffic; content-pipeline Run 206 shipped LinkedIn #206 opening a NEW lane = Medicaid/ACA-marketplace enrollment ministry, woman 39; codex Run 201 opened PR #48 fixing the SAME nav regression my Run-191 PR #47 targeted). THE ONE THING THAT CHANGED vs Run 191: the duplicate nav fix converged -- founder CLOSED my PR #47 and codex's #48 now carries the fix, so no orphan/dup PR to clean; separately codex opened NEW security PR #49 (anon-readable moderation RPCs + sharp CVEs). UNIT OF WORK = live board reconciliation + duplicate-resolution confirmation + security escalation (correctly did NOT ship a 3rd nav PR -- would just re-create the dup). VERIFIED THIS RUN: (a) nav regression STILL LIVE on main -- git show origin/main:lib/nav.ts lines 6-7 keep bare '#how'/'#health'; main unchanged @6e0980b; #48 fixes it (isActive() still guards href.startsWith('#')->false, no active-state regression). (b) PR #47 = CLOSED/MERGEABLE (founder converged on #48). (c) READY QUEUE = 7 non-draft MERGEABLE PRs, all file-disjoint, safe any-order: #49 (security: migration 0025 + package.json/lock) > #48 (nav: lib/nav.ts+2 tests) > #38/#39/#40/#41 (calendar date fixes) > #43 (robots). (d) P1 GATE EXACTLY 7.0 DAYS COLD: STEF-WEEK-1-APPROVAL.md mtime UNMOVED Aug 11 09:31:48, status still '**Status:** APPROVAL REQUESTED'. HANDOFF: (1) SOLE P1 = Stef sign STEF-WEEK-1-APPROVAL.md -- 7.0 days cold, Aug-17 3pm go/no-go window behind us. (2) Merge order: #49 security FIRST (live CVE + anon RPC leak), then #48 nav (live dead-click defect), then #38/#39/#40/#41/#43 any-order; POST-MERGE checks: #40 Supabase 0024 apply+smoke, #49 apply migration 0025 + npm i for sharp bump, #43 confirm robots Disallow /settings+/account/. (3) Fund OpenAI key (non-blocking). (4) Frontier = keep the ready pile clean + regression-free; founder is merging manually."
runs_completed: 192
items_processed: 792
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
