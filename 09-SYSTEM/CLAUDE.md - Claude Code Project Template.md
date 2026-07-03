---
type: reference
category: claude-code
status: active
last-updated: 2026-06-27
related: "[[Claude Code + Obsidian Master Guide]]"
---

# CLAUDE.md — Claude Code Project Template

> A drop-in configuration layer that makes Claude immediately productive in any codebase. No source code — just scaffolding: rules, skills, agents, hooks, workflows.

📁 Template lives at: `~/Desktop/claude-project/`

---

## How Configuration Loads (Priority Order)

```
CLAUDE.md           ← loaded every session
CLAUDE.local.md     ← personal overrides, gitignored, stacks on top
AGENTS.md           ← subagent roster, read before any delegation
.mcp.json           ← MCP wiring (GitHub, Postgres, Slack)
.claude/
  settings.json     ← tool permissions + hook event bindings
  rules/*.md        ← modular rule files, loaded on demand
skills/<name>/SKILL.md  ← auto-triggered by task context
agents/*.md         ← isolated subagents, own context window
hooks/*.sh          ← deterministic enforcement via shell
workflows/*.md      ← multi-step blueprints
memory/*.md         ← persistent context across sessions
commands/*.md       ← custom /project: slash commands
```

---

## Custom Slash Commands

| Command | What it does |
|---|---|
| `/project:review` | Code review against all `.claude/rules/` |
| `/project:deploy [staging\|production]` | Pre-flight → build → deploy → smoke tests |
| `/project:scaffold <name>` | Generates `src/features/<name>/` with service, types, tests |

---

## Subagents

Invoke with `@agent-name`. Each runs in an isolated context window — keeps main session clean.

- `@security-reviewer` — audits for vulns, returns severity-ranked JSON
- `@test-writer` — writes co-located tests, never touches source files
- `@research` — web search + doc fetch, returns structured findings with sources

---

## Skills

Auto-trigger by task context. One job each.

- `skills/code-review/` — PASS / NEEDS CHANGES / BLOCK verdict
- `skills/testing-patterns/` — tests only, no source modifications
- `skills/pr-description/` — full PR description from `git diff main`

---

## Hooks

Shell scripts — deterministic, not LLM interpretation. Exit 0 = allow, exit 2 = block.

- `PreToolUse(Write)` → `validate-code.sh` — blocks `.env*` and `secrets/` writes
- `PostToolUse(Write)` → `post-edit-format.sh` — runs prettier (TS/JS) or black (Python)
- `block-sensitive-writes.sh` — secondary block on credential-looking content

---

## Permissions (settings.json)

**Allowed:** `git *`, `npm *`, `pnpm *`, writes to `src/**` and `tests/**`  
**Denied:** `rm -rf *`, writes to `.env*`, `secrets/**`

Personal overrides → `.claude/settings.local.json` (gitignored)

---

## Code Conventions

**Style:** 2-space indent · single quotes · trailing commas · 100-char max  
**Naming:** `camelCase` functions · `PascalCase` classes · `SCREAMING_SNAKE_CASE` constants · `kebab-case` files  
**Imports:** external → internal → relative · no wildcards · named exports over default

**API:** `{ data, error, meta }` envelope · versioned paths `/api/v1/` · HTTP 422 for validation errors  
**Tests:** co-located `foo.test.ts` · Arrange/Act/Assert · mock all externals · 80% unit coverage min  
**PRs:** `<type>(<scope>): <summary>` ≤72 chars · always closes an issue

---

## Workflows

| Workflow | Sequence |
|---|---|
| `feature-build` | clarify → research → plan → scaffold → implement → test → review → PR |
| `bug-fix` | reproduce → locate root cause → fix minimally → regression test → review |
| `code-review` | diff → `@security-reviewer` → skill review → test coverage → summary |

**Hard stop on all workflows:** never open a PR without user confirmation.

---

## Memory Files (read at session start)

- `memory/project-context.md` — what we're building, current state
- `memory/decisions.md` — architectural decisions with reasoning
- `memory/progress.md` — running log of done / blocked

---

## Customizing This Template

When dropping into a real project, fill in:

1. `CLAUDE.md` — project overview, tech stack, architecture
2. `memory/project-context.md` — what the project does
3. `.mcp.json` — real env var names for your services
4. `.claude/settings.json` — adjust write paths for your directory structure
5. `CLAUDE.local.md` — your machine paths (never commit)

---

## Related

- [[Claude Code + Obsidian Master Guide]]
- [[Vault Setup Complete - Next Steps]]
