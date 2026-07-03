# Credential Index — OpenClaw / clawdbot

This note tells you WHERE each secret lives and HOW to rotate it. It deliberately contains no actual key, token, or password values — those stay in the live config file only, to limit exposure if this vault ever syncs, backs up, or gets shared somewhere unexpected.

---

## 1. Telegram bot token

- **What it's for:** Lets the OpenClaw gateway send/receive messages as your Telegram bot (clawdbot channel).
- **Where the real value lives:** `~/.openclaw/openclaw.json` → `channels.telegram.botToken`
- **To view it:** open that file directly on this Mac.
- **To rotate it:** talk to @BotFather in Telegram → select your bot → Bot Settings → API Token → Revoke current token → generate new one. Paste the new value into `openclaw.json` in the same field, then restart the OpenClaw gateway.

## 2. Gateway auth token

- **What it's for:** Local authentication for the OpenClaw gateway process itself (binds to loopback only — not exposed to the network by default).
- **Where the real value lives:** `~/.openclaw/openclaw.json` → `gateway.auth.token`
- **To rotate it:** generate a new random token (e.g. `openssl rand -hex 24` in Terminal) and replace the value in that field. Restart the gateway after changing it.

## 3. Google Places API key (`goplaces` skill)

- **What it's for:** Powers the `goplaces` skill so agents can do location/places lookups.
- **Where the real value lives:** `~/.openclaw/openclaw.json` → `skills.entries.goplaces.apiKey`
- **To rotate it:** Google Cloud Console → APIs & Services → Credentials → find the key → Regenerate Key (or create a new restricted key and delete the old one). Update the value in `openclaw.json`.

## 4. Anthropic API auth

- **What it's for:** Lets OpenClaw's agents call Claude models.
- **Where it lives:** `~/.openclaw/openclaw.json` → `auth.profiles."anthropic:default"` — mode is `api_key`, meaning a key is stored via OpenClaw's own auth handling (check `openclaw auth status` or similar CLI command for exact storage location; not directly visible as plaintext in this config file the way the other three are).
- **To rotate it:** Anthropic Console → API Keys → revoke and reissue → re-run OpenClaw's auth/onboarding flow to re-link.

---

## General hygiene notes

- `openclaw.json` itself has several `.bak` copies in `~/.openclaw/` (`.bak`, `.bak.1`, `.bak.2`) — these likely also contain old or current plaintext secrets. Worth checking and cleaning up periodically, not just the live file.
- This vault (and Desktop/Context generally) is read by multiple autonomous agents with write access. None of them should ever be instructed to copy actual secret values into a vault note, a memory file, or a chat — if one ever does, treat that as a bug to fix, not a convenience to keep.
- If any of these three tokens ever appear in a chat log, a memory file, or a synced note by accident, rotate them — don't just delete the text. Deleted text isn't the same as a token nobody has seen.
