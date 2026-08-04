---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-04T01:46:34.374Z"
current_task: null
active_spec: null
runs_completed: 2
last_error: null
---

# Architect — General-Purpose System Design Supervisor

Designs systems before Codex builds them. Produces specs, ADRs, and architectural plans for **any project**.
Token-lean: no context.md injection, max_tokens 1024, concise prompts.

Two modes:
- **Full** — Sonnet, structured spec (What/Key Decisions/Spec/Risks/Done When/Handoff)
- **Lite** — Haiku, numbered steps + done-when bullets only

Invocation:
```
node run.js "<design task>" [--mode lite] [--project "name"]
```

Core question: **"What exactly are we building and why, before a single line of code is written?"**

> v1 (Plug AI / BigHeart scoped, max_tokens 2048, context.md injection) archived to `agents/_archived/architect-agent-v1/`

## Active Spec
<!-- Architect writes the current design here -->

## Last Architecture Decision
*2026-08-04 (full)*

## What We're Building
A standards-compliant OAuth2 authorization server exposing REST endpoints that support the Authorization Code (+ PKCE), Client Credentials, and Refresh Token grant flows. It issues opaque access tokens (JWT-signed) and refresh tokens, provides token introspection and revocation, and plugs into downstream resource servers via a shared public-key endpoint — suitable for both first-party apps and third-party integrations.

---

## Key Decisions

1. **JWT access tokens (RS256) over opaque tokens.** Resource servers validate tokens locally without a network round-trip to the auth server, reducing latency and coupling. Trade-off: tokens cannot be revoked mid-lifetime — mitigated by short TTLs (15 min) + refresh-token rotation.

2. **PKCE mandatory for all public clients.** Eliminates authorization-code interception without requiring a client secret, covering SPAs and mobile apps with a single flow rather than maintaining two separate security profiles.

3. **Refresh token rotation with family tracking.** Each refresh produces a new token and invalidates the previous one. Reuse of a revoked token (theft signal) invalidates the entire family, balancing UX continuity with session-hijacking defense.

---

## Spec

### Data Models

```
Client
  client_id        UUID PK
  client_secret    bcrypt hash (null for public clients)
  redirect_uris    text[]
  grant_types      enum[] {authorization_code, client_credentials, refresh_token}
  scopes           text[]
  is_public        bool
  created_at       timestamptz

AuthorizationCode
  code             varchar(64) PK   — random, single-use
  client_id        FK → Client
  user_id          FK → User
  redirect_uri     text
  scope            text
  code_challenge   text            — PKCE S256 hash
  expires_at       timestamptz     — now + 10 min
  used             bool

Token (refresh)
  jti              UUID PK
  family_id        UUID            — links sibling tokens for rotation
  client_id        FK → Client
  user_id          FK → User (null for client_credentials)
  scope            text
  revoked          bool
  expires_at       timestamptz     — now + 30 days

JWKS (key store)
  kid              varchar PK
  public_key       text (PEM)
  algorithm        varchar
  active           bool
```

---

### API Contracts

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET`  | `/oauth/authorize` | none | Start auth-code flow |
| `POST` | `/oauth/token` | Basic or body | Exchange code / credentials / refresh |
| `POST` | `/oauth/revoke` | Basic or Bearer | Revoke access or refresh token |
| `POST` | `/oauth/introspect` | Basic (resource server) | Validate any token |
| `GET`  | `/.well-known/oauth-authorization-server` | none | Discovery metadata |
| `GET`  | `/.well-known/jwks.json` | none | Public keys for JWT verification |

**`GET /oauth/authorize`**
```
Query: response_type=code
       client_id, redirect_uri, scope, state
       code_challenge, code_challenge_method=S256   ← required for public clients
Response: 302 → redirect_uri?code=…&state=…
Errors:   302 → redirect_uri?error=invalid_request|unauthorized_client&state=…
```

**`POST /oauth/token`**  
Content-Type: `application/x-www-form-urlencoded`

*Authorization Code*
```
grant_type=authorization_code
code, redirect_uri, client_id, code_verifier
→ 200 { access_token, token_type:"Bearer", expires_in:900,
         refresh_token, scope }
```
*Client Credentials*
```
grant_type=client_credentials  scope
Authorization: Basic {client_id:secret}
→ 200 { access_token, token_type:"Bearer", expires_in:900, scope }
```
*Refresh Token*
```
grant_type=refresh_token  refresh_token  [scope]
→ 200 { access_token, expires_in:900, refresh_token (new), scope }
   if refresh token is from a revoked family → 400 invalid_grant + family revoked
```

**`POST /oauth/revoke`** (RFC 7009)
```
token, [token_type_hint]
→ 200 OK always (idempotent)
```

**`POST /oauth/introspect`** (RFC 7662)
```
token
→ 200 { active:true, sub, scope, exp, client_id, … }
     | { active:false }
```

---

### Components

| Component | Responsibility | Interface |
|-----------|---------------|-----------|
| **AuthorizationEndpoint** | Renders consent screen, validates PKCE params, issues auth code | HTTP GET handler; reads session for authenticated user |
| **TokenEndpoint** | Dispatches to grant handlers, signs JWTs, rotates refresh tokens | HTTP POST handler; returns `application/json` |
| **GrantHandlers** | `AuthCodeGrant`, `ClientCredentialsGrant`, `RefreshTokenGrant` — each validates, exchanges, emits tokens | Internal service classes called by TokenEndpoint |
| **TokenSigner** | Creates/validates RS256 JWTs, manages key rotation via `kid` | `sign(claims) → JWT`, `verify(jwt) → claims` |
| **TokenStore** | CRUD for refresh-token families, auth codes; enforces TTL + single-use | Repository interface backed by Postgres |
| **ClientRegistry** | Validates client_id/secret, allowed redirect URIs, grant types | `authenticate(id, secret)`, `assertRedirectUri(id, uri)` |
| **IntrospectionEndpoint** | Validates JWT signature + expiry, checks refresh-token revocation | HTTP POST; resource-server authenticated |
| **RevocationEndpoint** | Marks refresh tokens revoked; for access tokens logs hint only | HTTP POST |
| **JWKS Endpoint** | Serves active public keys; cached 1 h | HTTP GET; no auth |
| **Discovery Endpoint** | RFC 8414 metadata doc | HTTP GET; no auth |

---

### Integration Points

- **Upstream:** User authentication service — `AuthorizationEndpoint` delegates identity verification (SSO, local login) via internal session cookie or `/internal/session` call.
- **Downstream resource servers:** Validate access tokens using `/.well-known/jwks.json` (public key fetch, cached); call `/oauth/introspect` for opaque-like validation if preferred.
- **Key management:** HSM or secrets vault (e.g., AWS KMS / HashiCorp Vault) — `TokenSigner` fetches private key at startup, rotates on scheduled key ceremony.
- **Persistence:** Postgres for `Client`, `AuthorizationCode`, `Token`; Redis for short-lived auth-code TTL enforcement and revocation bloom filter.
- **Observability:** Emit structured events — `token.issued`, `token.refreshed`, `token.revoked`, `introspect.called` — to audit log pipeline.

---

## Risks

| Risk | Mitigation |
|------|-----------|
| **Refresh token theft via DB breach** — attacker replays a stolen token | Store refresh tokens as bcrypt hashes; return plaintext only at issuance; rotation + family revocation limits blast radius |
| **Key compromise** — private signing key leaked, all issued JWTs trusted | Short JWT TTL (15 min) limits window; JWKS endpoint + `kid` rotation lets resource servers hot-swap public keys without downtime |
| **Redirect URI mismatch / open redirector** — attacker registers lookalike URI | Exact-string match (no wildcard, no path prefix) against pre-registered `redirect_uris`; reject on any deviation |

---

## Done When

1. `POST /oauth/token` with a valid PKCE authorization code returns a signed JWT verifiable against `/.well-known/jwks.json` with correct `sub`, `scope`, and `exp`.
2. Reusing a revoked refresh token returns `400 invalid_grant` **and** all tokens in the same family are marked revoked in the DB within 100 ms.
3. A resource server calling `POST /oauth/introspect` with an expired or tampered access token receives `{ "active": false }` with no PII in the response body.

---

## Handoff

**Build `ClientRegistry` + `TokenStore` first.** All grant handlers depend on client validation and token persistence. Stand up the Postgres schema (`clients`, `authorization_codes`, `tokens` tables), implement `authenticate(client_id, secret)` with bcrypt compare, and write `assertRedirectUri` with exact-match logic. Seed one confidential client and one public client, and cover both with unit tests — every other component gates on this foundation.
