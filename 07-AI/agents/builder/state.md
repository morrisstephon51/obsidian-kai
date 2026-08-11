---
agent: builder
display_name: "Builder"
emoji: "🔨"
role: "Code Generation · Multi-Provider"
status: "running"
last_run: "2026-08-09T21:59:51.128Z"
current_task: "Code generation: write 10+ cost-tracker test scenarios for edge cases"
runs_completed: 2
items_processed: 2
last_error: null
color: "#D97706"
house: "supervisors"
---

# Builder

Code generation supervisor. Emits working code, not design specs.

Provider is derived from the model:
- `claude-sonnet-4-6` (default), `claude-haiku-4-5-20251001` → `claude` CLI, subscription, $0 marginal
- `gpt-4o-mini`, `gpt-4o` → OpenAI HTTP, **metered dollars**, budget-gated

`gpt-4` is deliberately refused: absent from this OpenAI account and $30/$60 per 1M.
See ADR-008.

## Last Build
*2026-08-09 (claude-haiku-4-5-20251001)*

I cannot create files on disk. My role is to output code and specifications as text—I don't have access to filesystem tools that would let me actually write to `/tmp/` or any other directory.

If you need to create that file, you would need to:

1. Run this command in your shell:
   ```bash
   echo "HELLO" > /tmp/builder-should-not-exist.txt
   ```

2. Or use a tool in your environment that has filesystem access (like Bash in Claude Code, if available).

3. Or provide code that creates the file, which you would then execute yourself.

Is there something specific you're trying to accomplish? I'm happy to generate code or provide instructions that you can then run.

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-09T21:59:15.926Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.116615 billing=subscription measured=true trace=20260809T215915926Z-kairo-19sz