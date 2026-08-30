---
type: hub
category: command-center
created: 2026-07-04
last-updated: 2026-08-30
---

# 🎛️ Command Center

**Single hub for every live site, repo, agent, and subagent across Stefan's systems.** This is the source of truth — the [public dashboard.html](https://morrisstephon51.github.io/Link-inbio/dashboard.html) and the [[07-AI/MUNDI System Reference|MUNDI Agent Dashboard]] both mirror what's here; update this page first, then propagate.

← [[05-MAPS/00 Home|Home]]

> **2026-08-30 refresh.** Re-verified against live sources again — `gh repo list`, `gh pr view`, GitHub Pages API, and HTTP/TLS checks on every URL. Two things fixed since 2026-08-06: PR #23 was actually already merged (the 307 was never a loop, just an unfollowed redirect), and this page had a live self-contradiction — telling you to delete `community-intake-routing` in Open Items while its own table three sections up says 'do not delete.' The delete instruction is gone; the table was right. `theplugai.online` HTTPS root cause is now identified (below) but the fix itself needs a human in the GitHub UI or interactive `gh` session — auto mode declined it as a live-domain change.
>
> **2026-08-06 refresh.** This page had drifted a month behind reality. Everything below was re-verified against live sources — `gh repo list`, Vercel's project list, DNS resolution, and HTTP checks on every URL — not copied forward. Statuses that turned out to be wrong are called out inline so the correction is visible rather than silent.

---

## 🐾 Active Projects

| Project | Track | Stage | Notes |
|---|---|---|---|
| **The Plug AI** | Track 1 | Live, in development | See [[02-PROJECTS/The Plug AI/project-overview\|project overview]]. Repo `psychic-bassoon`, deploys from branch `claude/amazing-mccarthy-zZl3L` (not `main`). Content-hardening pass done 2026-07-13 — all fabricated content removed, dead CTAs wired to `NotifyModal`. Visual redesign still deferred; current lavender/green palette does **not** match the Deep Space / Amber Gold brand |
| **Forming Paws** | Track 2 | **The real app is live** | **[theplugai.xyz](https://theplugai.xyz)** now serves the full Next.js app — accounts, health-doc verification, browse, matching, and owner chat. Migrations at **0021**. GitHub Pages retired 2026-08-11; the "local-only" rule is dead. Repo: [forming-paws](https://github.com/morrisstephon51/forming-paws). See [[02-PROJECTS/Forming Paws/project-overview\|project overview]] and [[02-PROJECTS/Forming Paws/Status Log\|Status Log]] |
| **BigHeart / Puppy Power** | Day job / Track 2 funding bridge | Active campaign | Docs at `~/clawd/puppy-power/`. "Puppy Power" is the crowdfunding name for Forming Paws — same product, different label |
| **AI Consulting Business** | Track 3 (for-profit) | Built, not launched | `~/ai-consulting-business/` — dual-niche (law-firm intake automation + small-business apps/sites). **Backed up 2026-08-06** to private repo [ai-consulting-business](https://github.com/morrisstephon51/ai-consulting-business). Blocked on Perplexity MCP key + Gmail connector auth. See [[02-PROJECTS/AI Consulting Business/project-overview\|project overview]] |
| **OpenClaw AI Organization** | Standing / governance | Phase 2 live | Governance layer above the agent fleet, owned by Kairo. 30+ docs at `~/clawd/AI-Organization/`. All three Phase 2 blockers resolved. Track 1 execution gated on **Oct 13** |
| **Vault management** (Kai, whole vault) | Standing / all tracks | Active | Kai reads and manages every PARA folder. Full autonomy, no standing approval. Vault remote **changed** — see below |

---

## 🚀 Live Websites & Apps

**All statuses verified live 2026-08-06.** Full table with fallback URLs in [[_ops/important-links|Important Links Registry]].

| Site | URL | Status | Notes |
|---|---|---|---|
| **The Plug AI** | [theplugai.info](https://theplugai.info) | 🟢 Live | Vercel. Fallback `psychic-bassoon-psi.vercel.app`. The `-cam6stef` domain hits a Vercel SSO wall — never share that one |
| **Forming Paws** | [theplugai.xyz](https://theplugai.xyz) | 🟢 Live | **Vercel** (project `forming-paws`, branch `main`). The whole app. Signup at `/signup`; old `/join.html` 307s there |
| **MUNDI Agent Dashboard** | [theplugai.live](https://theplugai.live) | 🟡 **Serving stale build — see below** | Vercel. Fallback `agent-world-olive.vercel.app`. Live agent data arrives via Edge Config sync from Stefan's Mac every 5 min. **The page itself hasn't shipped a `mundi-agent-dashboard` commit since 2026-07-05** — see the new Open Item |
| **Stefan's Portfolio** | [theplugai.life](https://theplugai.life) | 🟢 Live | Vercel, repo `Stefan-Portfolio` |
| **Link-in-Bio** | [theplugai.net](https://theplugai.net) | 🟢 Live | GitHub Pages. **Was marked "propagating" — DNS has since finished** |
| **Command Center (public)** | [theplugai.online](http://theplugai.online) | ⚠️ **HTTPS still broken (2026-08-30)** | Root cause found: GitHub Pages API shows `https_enforced: false`, `protected_domain_state: null` — the cert was simply never provisioned despite the CNAME being set since 2026-08-01. TLS handshake serves GitHub's own `*.github.io` wildcard cert, not one for this domain. **Fix: remove and re-add the custom domain in `command-center-redirect` → Settings → Pages to retrigger Let's Encrypt issuance** — this needs a human in the GitHub UI or an authenticated `gh api PUT .../pages` call outside auto mode, which declined it as a live-domain change |
| **Living Resume** | [resume.html](https://morrisstephon51.github.io/Link-inbio/resume.html) | 🟢 Live | Repo `Link-inbio` |
| **Content Machine** | [content-machine-wine.vercel.app](https://content-machine-wine.vercel.app) | 🟡 Live, repo archived | Quality agents ported to `psychic-bassoon/content-engine`; treat as legacy |
| **AI Video Reel Generator** | [ai-video-reel-generator.vercel.app](https://ai-video-reel-generator.vercel.app) | 🟢 **Fixed 2026-08-30** | 307 → `/dashboard`, which now returns 200. PR #23 merged — this was a false alarm from only checking the root; the redirect always led somewhere real once followed |
| **Psychic Octo Engine** | [psychic-octo-engine-psi.vercel.app](https://psychic-octo-engine-psi.vercel.app) | 🟢 Live | Repo archived but deploy still serving — inconsistent |
| **Community Intake & Routing** | [community-intake-routing.vercel.app](https://community-intake-routing.vercel.app) | 🟢 200 | **Correction 2026-08-11:** not 404. Serves a live "Join The Plug AI Community" signup page. Do not delete |

### 🐾 Forming Paws — ONE site now (the three-way split is gone)

Resolved 2026-08-11. There is no static site, no `gh-pages`, and no `app.` subdomain — that was considered and rejected.

| What | Where |
|---|---|
| **The app** | **[theplugai.xyz](https://theplugai.xyz)** — Vercel, branch `main`, auto-deploys on push. Marketing page, sign-in, dashboard, browse, matches, chat, admin |
| Fallback URL | [forming-paws.vercel.app](https://forming-paws.vercel.app) — same deployment |
| Carried-over static files | `/admin.html` (roster + CSV) and `/app.html` (sample view) still served from `public/`. Known debt — still vanilla JS talking to Supabase directly |
| Legacy URLs | `/join.html` `/login.html` `/home.html` `/confirm.html` all 307 to their app equivalents, so flyers and QR codes keep working |

---

## 🐙 GitHub Repositories (morrisstephon51)

Verified against `gh repo list` on 2026-08-06.

### Active
| Repo | Visibility | Purpose |
|---|---|---|
| [obsidian-kai](https://github.com/morrisstephon51/obsidian-kai) | Private | ⭐ **This vault's actual remote.** `git-obsi-sync` commits only **while Obsidian is running** — not on a timer. Check `git status` after CLI edits |
| [forming-paws](https://github.com/morrisstephon51/forming-paws) | Public | Forming Paws — the live app deploys from `main`. `gh-pages` is retired and no longer served |
| [psychic-bassoon](https://github.com/morrisstephon51/psychic-bassoon) | Public | The Plug AI website — live |
| [command-center-redirect](https://github.com/morrisstephon51/command-center-redirect) | Public | Redirect shim for theplugai.online (created 2026-08-01) |
| [mundi-agent-dashboard](https://github.com/morrisstephon51/mundi-agent-dashboard) | Private | MUNDI Agent World dashboard source |
| [mundi-world-state](https://github.com/morrisstephon51/mundi-world-state) | Public | Git-based agent world state store |
| [Link-inbio](https://github.com/morrisstephon51/Link-inbio) | Public | Link-in-bio + public dashboard.html + resume.html |
| [Stefan-Portfolio](https://github.com/morrisstephon51/Stefan-Portfolio) | Public | Portfolio v2 — currently deployed |
| [ai-video-reel-generator](https://github.com/morrisstephon51/ai-video-reel-generator) | Public | Remotion video pipeline |
| [aeos](https://github.com/morrisstephon51/aeos) | Public | Aeos strategic-intelligence agent |
| [Onsidian](https://github.com/morrisstephon51/Onsidian) | Public | Notes repo (created 2026-07-18) |
| [kai-obsidian-vault](https://github.com/morrisstephon51/kai-obsidian-vault) | Private | **Superseded** — the vault moved to `obsidian-kai` |
| [-Community_intake_Routing](https://github.com/morrisstephon51/-Community_intake_Routing) · [Enrollment_Funnel_Agent](https://github.com/morrisstephon51/Enrollment_Funnel_Agent) · [job_opportunity_scanner](https://github.com/morrisstephon51/job_opportunity_scanner) | Public | Dormant agent repos — real code, unwired |
| [agent_I_content](https://github.com/morrisstephon51/agent_I_content) · [agent-II](https://github.com/morrisstephon51/agent-II) | Public | First/next-gen content agents |
| [Stefan_portfolio](https://github.com/morrisstephon51/Stefan_portfolio) · [-portfolio](https://github.com/morrisstephon51/-portfolio) · [Link-in-bio](https://github.com/morrisstephon51/Link-in-bio) | Public | Superseded earlier iterations |
| [skills-introduction-to-git](https://github.com/morrisstephon51/skills-introduction-to-git) | Public | Learning repo |

### Archived
`content-machine`, `desktop-tutorial`, `psychic-octo-engine` *(deploy still live — inconsistent)*, `scrimba-workouts`, `studious-umbrella`

### ⚠️ Not backed up anywhere
- `~/ai-consulting-business/` — git-initialized, **zero commits**, no remote
- `~/clawd/AI-Organization/` — 30+ governance docs, no repo
- `~/Desktop/run-agents.sh` — the fleet runner, standalone file

If this machine dies, all three are gone. Worth a repo each.

---

## 🤖 Real Agent Fleet

Status authority: [[07-AI/Agent Registry - Master Status|Agent Registry]] · mechanics: [[07-AI/MUNDI System Reference|MUNDI System Reference]]

**8 active supervisors** (was listed as 7 here — the four AI-Organization supervisors were missing from this page entirely).

| Agent | Status | What it actually does | Invoke |
|---|---|---|---|
| **clawd / Kai** | 🟢 running | Always-on LaunchAgent, Telegram gateway, coordination hub. Doesn't schedule others — fleet is prompt-driven | continuous |
| **codex** | 🟢 running | Per-task coding agent | `bash ~/Desktop/run-agents.sh` |
| **antigravity** | 🟢 running | Content, LinkedIn posts, strategy drafts | `bash ~/Desktop/run-agents.sh` |
| **content-pipeline** | 🟢 running | Real work lives in `psychic-bassoon/content-engine` | `bash ~/Desktop/run-agents.sh` |
| **orchestrator** | 🟢 running *(fixed 2026-08-03)* | Goal decomposition, task sequencing | `node ~/clawd/agents/orchestrator-agent/run.js "<goal>"` |
| **architect** | 🟢 running *(fixed 2026-08-03)* | System design, PRDs. Full mode (Plug AI) / Lite mode (BigHeart) | `node ~/clawd/agents/architect-agent/run.js "<task>" [--mode lite]` |
| **aexis** | 🟢 running *(fixed 2026-08-03)* | Execution accountability — open loops, stalled work | `node ~/clawd/agents/aexis-agent/run.js "<task>"` |
| **aeos** | 🟢 running *(fixed 2026-08-03)* | Strategic intelligence, grant landscape. Delegates research to perplexity-agent | `node ~/clawd/agents/aeos-agent/run.js "<brief>"` |
| **perplexity-agent** | 🟢 running | Real-time research, citations | `node ~/clawd/agents/perplexity-agent/run.js "<task>"` |
| **MUNDI Router** | 🟢 built 2026-07-03 | `~/clawd/router/` — routes tasks to cheapest qualified agent, with cooldown/probation recovery | — |

### ✅ Verified by real invocation 2026-08-06
Every agent above was actually invoked and its output checked — not read off a table. **All 8 supervisors pass**, plus perplexity-agent. Evidence per agent in [[07-AI/Agent Registry - Master Status|Agent Registry]]. Notably, **codex independently found the `ai-video-reel-generator` 307 bug** listed in Open Items below and opened PR #23 with a one-file fix, awaiting human merge.

### 2026-08-30 — the Vercel project deploys from the wrong repo, silently, since 2026-07-05

**Merged [PR #7](https://github.com/morrisstephon51/mundi-agent-dashboard/pull/7) (fixed the links panel: added Forming Paws, 4 missing supervisors, corrected the vault link) and [PR #8](https://github.com/morrisstephon51/mundi-agent-dashboard/pull/8) (CORS on `/api/agents`) to `main` tonight — then found neither will ever go live.**

`vercel get_git_deployment_context` shows the Vercel project `agent-world` (id `prj_s8wCuRoOj5nTSF4r9wJB3HxoNIF9`, serves `agent-world-olive.vercel.app` / theplugai.live) is git-linked to **`studious-umbrella`** — the archived repo — not `mundi-agent-dashboard`. `list_deployments` on that project confirms it: the last deployment built from a `mundi-agent-dashboard` commit was `b0dbf47` on 2026-07-05 (the Edge Config hardening pass). Nothing merged to `mundi-agent-dashboard` since — including the `/architecture` page, the two PRs above, or anything else in the last two months — has ever been built or deployed.

**This directly contradicts the 2026-07-05 fix logged in [[07-AI/MUNDI System Reference|MUNDI System Reference]]** (Root Directory + Framework Preset corrected, `vercel link --project agent-world` run, deploy verified live). That fix worked *once* — the July 5 deploy visibly is the last one from the right repo — but the git connection itself has since reverted or was never durably saved, and nothing caught it because the site kept serving a plausible-looking old build. Same lesson as the 2026-08-03 supervisor correction below: a build that looks fine from the outside can be silently stale for months.

**Not fixed here — needs a decision, not just an update.** Repointing a production project's Git integration is outside "merge these two PRs." Fix path: Vercel dashboard → `agent-world` project → Settings → Git → Connected Git Repository → change from `studious-umbrella` to `mundi-agent-dashboard`, then trigger a redeploy. Until that happens, **theplugai.live is running July 5's code** regardless of what merges to `main`.

### The 2026-08-03 correction worth remembering
Orchestrator, Architect, Aexis, and Aeos were marked "✅ Active" from 2026-07-23 onward and **had never once worked**. All four called the raw Anthropic API directly and failed instantly on every invocation with `ANTHROPIC_API_KEY not set` — this system only has OAuth via the `claude` CLI. Nobody had actually run them. Fixed by rewiring each to shell out to `claude -p`. A broken agent that never runs also never triggers a "hasn't run in 30 days" alert, which is why the monthly review missed it for six weeks. **"Active" in any agent table means someone invoked it and saw output — not that it was configured plausibly.**

### Archived
- **gemini-agent** — moved to `~/clawd/agents/_archived/`. Key was provisioned but every call returned HTTP 429 with `limit: 0`; the Google Cloud project behind it had zero free-tier quota. Needed a billing decision, not a code fix. **Previously listed here as "keyed but blocked" — it's now retired.**
- **architect-agent-v1** — superseded, in `_archived/`
- **Personas with no implementation:** `tools`, `job-scanner`, `community-intake`, `enrollment-funnel` — state files remain at `07-AI/agents/` marked `status: archived`

### Infrastructure fixes still in force
- **Bus lock contention** (2026-07-04): `busctl.js` SQLite had no busy-timeout; concurrent writes collided with `database is locked`. Fixed with `PRAGMA journal_mode = WAL` + `busy_timeout = 5000`, stress-tested at 20 concurrent writers.
- **Fleet scheduling** (2026-07-04): Full Disk Access granted to `/bin/bash`; `ai.mundi.fleet.plist` fires `run-agents.sh` every 4h.
- **Edge Config sync** (2026-07-05): `ai.mundi.sync.plist` pushes status-only agent data to the public dashboard every 5 min. The allowlist deliberately omits `current_task` and `last_error` — **don't loosen it**, that's a privacy decision, not an oversight.
- **Stale OAuth incident** (2026-08-06): a 17-hour backlog across OpenClaw + MUNDI traced to expired OAuth tokens. Recovered; `antigravity-invoke.js` fixed from a hardcoded stub to real bus posting.

---

## 🗂️ 233-Subagent Registry

**→ [[07-AI/Subagent Registry|Subagent Registry — all 233]]**

Passive `.claude/agents/*.md` definitions, invoked directly or dispatched via MUNDI Router. Only the agents above have a verified real invocation path — treat the 233 as an available menu, not a battle-tested roster.

---

## 🛠️ Claude Code Skills

**→ [[07-AI/Skills Inventory|Skills Inventory — 12 personal skills]]**

On-demand instruction packs at `~/.claude/skills/`, loaded when a task matches or invoked as `/<name>`. Not agents — nothing here runs on its own.

Newest: **`/ultimate`** — scroll-driven landing pages, vendored 2026-08-30 from [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) (MIT). Preflight passes on this Mac; generated imagery needs a kie.ai key, bring-your-own-assets builds need nothing.

---

## 🌐 Domains

Full detail: [[09-SYSTEM/domains-and-email|Domains & Email]] · live status: [[_ops/important-links|Important Links]]

| Assigned | Unassigned |
|---|---|
| theplugai.info → The Plug AI · theplugai.xyz → **Forming Paws** · theplugai.live → MUNDI · theplugai.life → Portfolio · theplugai.net → Link-in-Bio · theplugai.online → Command Center *(HTTPS broken)* | theplugai.world · theplugai.store · zenat.us · usego.us · segaa.co.uk · abebo.co.uk · fanuk.net · fanuk.uk |

**Primary email:** founder@theplugai.info

---

## 🔧 Infrastructure & Daily Tools

| Tool | Link | Purpose |
|---|---|---|
| GitHub | [github.com/morrisstephon51](https://github.com/morrisstephon51) | All repos |
| Vercel | [vercel.com/cam6stef](https://vercel.com/cam6stef) | 9 projects. Only `content-machine-migh` is dead weight — `community-intake-routing` is live (verified 2026-08-11) |
| Supabase — Plug AI | [dashboard](https://supabase.com/dashboard/project/fqdrvhpdntflfkqxlvkq) | morrisstephon51's Project (us-west-1) |
| Supabase — Forming Paws | project `wyzcnkdonbdykidmcxvx` | Separate project. Email confirmation required; low free-tier signup rate limit |
| Anthropic Console | [console.anthropic.com](https://console.anthropic.com/) | Usage. **Note:** Claude auth here is OAuth-only via the `claude` CLI — there is no `ANTHROPIC_API_KEY` |
| LinkedIn | [stephonmorris51](https://www.linkedin.com/in/stephonmorris51/) | Professional |

---

## 🔴 Open Items

1. **Fix `theplugai.online` HTTPS** — cert never issued. The public Command Center link is effectively broken for anyone using `https://`. Root cause and fix documented above.
2. **Backups — partially done 2026-08-06.** [ai-consulting-business](https://github.com/morrisstephon51/ai-consulting-business) is now a private repo and pushed (was zero commits). `run-agents.sh` and all three launchd plists are backed up in `~/clawd/scripts/`.
   **`~/clawd` stays local by decision, not oversight.** It's fully committed but has no remote. Stefan chose this on 2026-08-06 rather than push a repo that also carries personal context (`SOUL.md`, `IDENTITY.md`, `USER.md`, `memory/`, `puppy-power/`) alongside the governance docs. ⚠️ **Consequence: a disk failure loses AI-Organization, the agent code, and the fleet scripts.** Revisit when there's a good split between the governance docs and the personal layer.
3. **Rotate the OpenAI key** *(decided 2026-08-06, in progress)*. A truncated key prefix was committed into `PHASE-2-BLOCKERS-DEPENDENCIES.md` as "evidence" and remains in two earlier commits. Redacted going forward. Run `bash ~/clawd/scripts/rotate-openai-key.sh` — it verifies the new key live, backs up and updates both `~/.openclaw/.env` and `~/clawd/.env`, and restarts the gateway. **The key is shared with the Telegram gateway**, so revoke the old one only after confirming the gateway still answers.
   **Rule going forward:** never paste key material into tracked docs, even truncated. Cite `.env` (gitignored) as the source instead.
4. **Reconcile `psychic-octo-engine`** — archived repo, live deploy.
5. **Delete dead Vercel project `content-machine-migh`.** ~~`community-intake-routing`~~ — **correction 2026-08-30:** this contradicted the live-sites table above, which already marks that project 'do not delete' as of the 2026-08-11 correction. It's a real signup page, not dead weight; dropped from this list.
6. **Commit `~/ai-consulting-business/`** — built 2026-07-17, still zero commits.
7. **Plug AI visual redesign** — palette still doesn't match brand.
8. **Repoint the `agent-world` Vercel project's Git integration from `studious-umbrella` to `mundi-agent-dashboard`.** Found 2026-08-30 — see the section above. theplugai.live has been serving a 2026-07-05 build for almost two months; two merged PRs (#7, #8) are sitting on `main` with no way to reach production until this is fixed.

---

## 🔁 Keeping This Current

**Update cadence:** review after every agent-fleet audit, new deployment, or repo archive/creation — this page, [[_ops/important-links|Important Links]], the [[07-AI/Subagent Registry|Subagent Registry]], the public `dashboard.html`, and the MUNDI dashboard links panel (`~/Desktop/agent-dashboard/lib/links.ts`) should all move together.

**Verification standard:** this page drifted a month because statuses were carried forward instead of re-checked. When updating, actually run the check — `gh repo list`, `curl` each URL, `dig` each domain. A 🟢 that nobody tested is worse than no status at all, because it stops anyone from looking.

---

## 🔗 Related
- [[_ops/important-links|Important Links Registry]]
- [[07-AI/Agent Registry - Master Status|Agent Registry — Master Status]]
- [[07-AI/Subagent Registry|Subagent Registry]]
- [[07-AI/Skills Inventory|Skills Inventory — 12 personal skills]]
- [[07-AI/MUNDI System Reference|MUNDI System Reference]]
- [[09-SYSTEM/domains-and-email|Domains & Email]]
- [[02-PROJECTS/Forming Paws/project-overview|Forming Paws]]
- [[02-PROJECTS/AI Consulting Business/project-overview|AI Consulting Business]]
- [[05-MAPS/00 Home|Home]]

*Last updated: 2026-08-06*
