---
agent: antigravity
display_name: "Antigravity"
emoji: "🚀"
role: "General Agent · Explorer"
status: idle
last_run: "2026-08-19T01:52:00Z"
current_task: "Run 195: TASK = scan context files + summarize active priorities + one meaningful unit of work. Bus 17:20-01:52Z wave = clawd#220 + codex#205 + content-pipeline#210 (all loop-ends, agents self-running; nothing needing action). UNIT OF WORK = live independent reconciliation (verify-dont-trust-the-bus; created nothing). VERIFIED THIS RUN via gh api + stat: (a) P1 GATE STILL COLD -- STEF-WEEK-1-APPROVAL.md mtime UNMOVED 2026-08-11 09:31:48, status line 5 still APPROVAL REQUESTED, now ~7.7d cold. (b) PR QUEUE GREW 7->8: codex#205 landed #50 (self-contained #42 redirect fix, decoupled from #41). LIVE-verified all 8 OPEN MERGEABLE+non-draft: #50(#42 redirect,closes #42) #49(security: anon moderation RPCs+sharp CVEs,migration 0025) #48(nav: dead #how/#health anchors) #43(robots /settings+/account/) #41(upload redirect wrapper getRequestOrigin) #40(browse max-age off-by-year,+Supabase 0024) #39(health-docs future-date calendar) #38(dogs future-date calendar). (c) NEW OVERLAP: #50 and #41 BOTH fix #42 redirect leak -- #50 self-contained, #41 carries reusable getRequestOrigin wrapper; not a conflict (file-disjoint) but founder should merge ONE and treat other as superseded. (d) #46 NAV REGRESSION STILL LIVE: lib/nav.ts on main HEAD 6e0980b lines 6-7 still bare #how/#health under global SiteHeader = dead anchors on non-home pages; #48 fixes, unmerged. (e) main HEAD unchanged 6e0980b -- founder merged nothing. Grant-drift loop CLOSED. HANDOFF: (1) SOLE P1 = Stef sign STEF-WEEK-1-APPROVAL.md ~7.7d cold; only true blocker. (2) Merge order: #49 FIRST (security), then #48 (kills live #46 nav regression), then ONE of #50/#41 for #42 (#50 simplest), then #40/#39/#38/#43 any-order; POST-MERGE: #40 Supabase 0024 apply+smoke, #49 migration 0025 + npm i sharp, #43 confirm robots Disallow. (3) Fund OpenAI key (non-blocking). (4) Frontier = keep ready pile clean + regression-free; founder merges manually. All bottlenecks founder-gated."
runs_completed: 195
items_processed: 795
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
