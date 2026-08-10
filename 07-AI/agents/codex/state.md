---
agent: codex
display_name: "Codex"
emoji: "💻"
role: "Code Agent · GitHub Sync"
status: running
last_run: "2026-08-10T18:45:00Z"
current_task: "Run 164: INDEPENDENT CODE REVIEW of psychic-bassoon PR#1 (Add real content, working forms, resource detail pages) -- the only OPEN non-draft PR on the frontier that codex had un-drafted/build-verified but never actually logic-reviewed. Verdict: SAFE TO MERGE, posted issuecomment-5244527481. Verified core deliverables correct: lib/formspree.ts guards missing formId (no /f/undefined call) + graceful degrade; /resources/[slug] gate logic sound (showContent = !emailGated || unlocked, 404 fallback present); lib/data/resources.ts data integrity confirmed -- 6 slugs ALL UNIQUE (no silent .find() shadowing), 4 email-gated / 2 free exactly matching PR description. Client-side gate noted as intentional (lead capture, not access control). Non-blocking finding: scope bloat -- content-engine/ (14 files incl committed package-lock + trends json), docs/superpowers plans/specs, tasks/content-checklist.md all net-new vs main and unrelated to the PR title. Verified it CANNOT break the Next build: root tsconfig.json excludes content-engine and it is a self-contained npm project (own package.json/tsconfig.server.json/setup.sh) -- history-hygiene concern only, optional split recommended, not a blocker. Residual (re-flagged): set NEXT_PUBLIC_FORMSPREE_CONTACT_ID + NEXT_PUBLIC_FORMSPREE_NEWSLETTER_ID on Vercel or the 4 forms + resource unlock post to a dead endpoint. Frontier now: psychic-bassoon PR#1 reviewed+SAFE (needs Formspree env), PR#11 DRAFT (Supabase+4 env); ai-video-reel-generator issue #5 (Supabase project -- founder-blocked); forming-paws issue #8 (IL legal docs -- founder-blocked), Slice A PRs #16-#20 reviewed+ready; Link-inbio PRs #5/#6 DRAFT. ---- PRIOR Run 163: FIXED dangling cross-ref in forming-paws PR#18 spec (commit ea22e62), closed that review finding."
runs_completed: 164
items_processed: 374
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
