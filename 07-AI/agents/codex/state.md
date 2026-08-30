---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: idle
last_run: "2026-08-30T14:15:00Z"
current_task: "Run 244: Live gh scan = frontier UNCHANGED (4 open issues: psychic-bassoon #21 [fixed by PR#22], forming-paws #8 [IL legal/founder], ai-video-reel #5 [Supabase infra/founder], skills-intro #1 [git tutorial]) -- only #21 code-actionable and already fixed. Rather than re-verify, did two things. (1) MERGE-READINESS: polled all 5 open psychic-bassoon PRs live -- ALL now CLEAN/MERGEABLE: #1, #11 (grant tracker, previously UNKNOWN -> now CLEAN), #19 (security headers, previously CONFLICTING -> my run243 conflict-fix HELD -> CLEAN), #20 (Next.js CVE bump), #22 (date fix +tests). Frontier fully unblocked on the CODE side; only founder merges remain, and founder can clear all 5 with zero conflicts. (2) FRESH SECURITY/CORRECTNESS AUDIT of the entire request surface on main (cloned depth-1): 5 API routes (contact/subscribe/workshop-request/health) all have input validation, length caps, non-blocking email, service-role DB writes -- clean; lib/mailer.ts HTML-injection escaping (escapeHtml over all 6 fields incl mailto attr) confirmed present from prior run; app/learn/[slug] dynamic route uses notFound() + generateStaticParams correctly; sitemap/robots/lib/site canonical (NEXT_PUBLIC_APP_URL->SITE_URL fallback) consistent; lesson internal-link integrity verified programmatically: 10 unique lesson slugs, 20 nextStep refs, 0 dead links, 0 duplicate slugs. No new defect found -- repo is genuinely hardened by runs 204-243. Net: confirmed the code frontier is 100% clean and fully mergeable; bottleneck remains solely the founder merge backlog. [runs 204-243 in .remember/ + prior state.md]."
runs_completed: 244
items_processed: 475
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
