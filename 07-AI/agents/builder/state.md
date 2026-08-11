---
agent: builder
display_name: "Builder"
emoji: "🔨"
role: "Code Generation · Multi-Provider"
status: "idle"
last_run: "2026-08-11T14:50:24.970Z"
current_task: null
runs_completed: 5
items_processed: 5
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
*2026-08-11 (claude-sonnet-4-6)*

```
// Blocking question: What language/runtime is this for, and what triggers the fallback — caught exception types, a config flag, latency threshold, or all three?
```

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-09T21:59:15.926Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.116615 billing=subscription measured=true trace=20260809T215915926Z-kairo-19sz
[2026-08-11T14:25:33.426Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.159800 billing=subscription measured=true trace=20260811T142533426Z-kairo-59s
[2026-08-11T14:29:03.065Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.163310 billing=subscription measured=true trace=20260811T142903065Z-kairo-6qn
[2026-08-11T14:49:50.526Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.080720 billing=subscription measured=true trace=20260811T144950526Z-kairo-c2l