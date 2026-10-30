# Obsidian vault (obsidian-kai)

## Finding notes: index first

- Read `_INDEX.md` first, then open only the note it points to. Don't list, glob or grep the vault to find a note.
- Generated folders (for example `07-AI/agents/content-pipeline/output/`) are collapsed to one line in the index. List that one folder only when you need what's inside it.
- If a note isn't in the index, run one targeted search for it, not a sweep of the vault.
- `node _ops/build-index.mjs --check` reports drift without reading any notes. To rebuild, run `node _ops/build-index.mjs`; it costs no model tokens.
- When you create, rename or delete a note, rebuild the index and commit `_INDEX.md` together with that change.
