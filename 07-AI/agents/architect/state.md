---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-04T01:47:32.694Z"
current_task: null
active_spec: null
runs_completed: 3
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

A standards-compliant OAuth 2.0 Authorization Server exposed as a REST API, supporting the Authorization Code (+ PKCE), Client Credentials, and Refresh Token grant types. It issues signed JWTs as access tokens, stores refresh tokens as opaque references in a database, and exposes endpoints for authorization, token exchange, introspection, and revocation — suitable for both first-party apps and third-party integrations.

---

## Key Decisions

1. **JWT access tokens, opaque refresh tokens.** JWTs let resource servers validate locally without a round-trip; opaque refresh tokens allow server-side revocation without token-scanning complexity. Signing key is RS256 (asymmetric) so public keys can be published via JWKS.

2. **PKCE mandatory for all public clients.** Removes the need for client secrets on SPAs/mobile apps and closes the authorization-code interception attack without adding an extra credential to manage. Confidential clients must also supply `client_secret` in addition to PKCE.

3. **Scope as a first-class resource.** Scopes are stored and validated server-side (not embedded only in token claims) so they can be updated or revoked without reissuing tokens. The introspection endpoint is the canonical truth for resource servers.

---

## Spec

### Data Models

```
Client
  id            UUID PK
  client_id     VARCHAR UNIQUE        -- public identifier
  client_secret BCRYPT(VARCHAR)       -- null for public clients
  type          ENUM(public, confidential)
  redirect_uris TEXT[]
  allowed_scopes TEXT[]
  grant_types   TEXT[]
  created_at    TIMESTAMP

AuthorizationCode
  code          VARCHAR(64) UNIQUE    -- short-lived, one-time use
  client_id     UUID FK
  user_id       UUID FK
  redirect_uri  VARCHAR
  scope         TEXT
  code_challenge VARCHAR(128)         -- PKCE S256
  expires_at    TIMESTAMP             -- TTL: 10 min
  used          BOOLEAN

RefreshToken
  token         VARCHAR(64) UNIQUE    -- opaque, stored hashed
  client_id     UUID FK
  user_id       UUID FK
  scope         TEXT
  expires_at    TIMESTAMP             -- TTL: 30 days (sliding)
  revoked       BOOLEAN

AccessToken (JWT claims)
  sub           user_id or client_id
  aud           resource server audience
  scope         space-separated
  iat / exp     issued-at / expiry (TTL: 15 min)
  jti           UUID for optional blocklist

JWKS Key
  kid           VARCHAR
  public_key    RSA 2048 PEM
  active        BOOLEAN
  created_at    TIMESTAMP
```

---

### API Contracts

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/oauth/authorize` | Authorization endpoint — redirects user to consent |
| `POST` | `/oauth/token` | Token endpoint — all grant types |
| `POST` | `/oauth/token/revoke` | Revoke access or refresh token |
| `POST` | `/oauth/token/introspect` | Active/inactive + claims for a token |
| `GET` | `/.well-known/openid-configuration` | Discovery document |
| `GET` | `/.well-known/jwks.json` | Public key set for JWT verification |
| `POST` | `/oauth/clients` | Register a new client (admin-auth required) |

#### `GET /oauth/authorize`
```
Query params:
  response_type  = "code"
  client_id      required
  redirect_uri   required (must match registered)
  scope          space-separated
  state          required (CSRF token)
  code_challenge required (Base64url SHA-256 of verifier)
  code_challenge_method = "S256"

Success → 302 {redirect_uri}?code=…&state=…
Error   → 302 {redirect_uri}?error=…&error_description=…
```

#### `POST /oauth/token`
```
Content-Type: application/x-www-form-urlencoded

Authorization Code grant:
  grant_type    = "authorization_code"
  code          (authorization code)
  redirect_uri
  client_id
  code_verifier (PKCE plaintext verifier)
  client_secret (confidential clients only, or via Basic auth header)

Client Credentials grant:
  grant_type    = "client_credentials"
  scope
  (client auth via Basic or body params)

Refresh Token grant:
  grant_type    = "refresh_token"
  refresh_token
  scope         (optional — subset of original)

200 OK:
{
  "access_token":  "eyJ…",
  "token_type":    "Bearer",
  "expires_in":    900,
  "refresh_token": "opaque64chars",  // absent for client_credentials
  "scope":         "read write"
}

4xx:
{
  "error":             "invalid_grant",
  "error_description": "Authorization code expired or already used."
}
```

#### `POST /oauth/token/introspect`
```
Body: token=…  (caller auth: Bearer token of resource server)

200 OK (active):
{
  "active": true,
  "sub": "user-uuid",
  "scope": "read",
  "exp": 1754265000,
  "client_id": "app-client-id"
}

200 OK (inactive):
{ "active": false }
```

#### `POST /oauth/token/revoke`
```
Body: token=… (+ client auth)
200 OK — always (per RFC 7009, even unknown tokens return 200)
```

---

### Components

| Component | Responsibility | Interface |
|-----------|---------------|-----------|
| **AuthorizationEndpoint** | Validates client/redirect/scope, creates `AuthorizationCode`, renders consent UI or redirects | Handles `GET /oauth/authorize` |
| **TokenEndpoint** | Routes grant types, validates all inputs, mints JWT + refresh token | Handles `POST /oauth/token` |
| **PKCEValidator** | Verifies `code_challenge` vs `code_verifier` (S256) | `validate(challenge, verifier) → bool` |
| **JWTService** | Signs/verifies JWTs, exposes JWKS, rotates keys | `sign(claims)`, `verify(token)`, `getPublicKeys()` |
| **TokenStore** | CRUD for `AuthorizationCode` + `RefreshToken` (Redis + Postgres) | `saveCode()`, `consumeCode()`, `saveRefresh()`, `revokeRefresh()` |
| **ClientRegistry** | Validates `client_id`, `client_secret`, `redirect_uri`, allowed grants | `authenticate(id, secret)`, `validateRedirect(id, uri)` |
| **IntrospectionEndpoint** | Token decode + revocation check for resource servers | Handles `POST /oauth/introspect` |
| **ScopeService** | Validates requested scope ⊆ client's registered scopes | `validate(clientId, requestedScope)` |

---

### Integration Points

- **User Identity Provider** — `AuthorizationEndpoint` calls internal authn service to authenticate the resource owner (session cookie or redirect to login page).
- **Resource Servers** — call `/oauth/introspect` with a dedicated service credential; or validate JWT locally using JWKS.
- **Key Management (KMS/Vault)** — `JWTService` fetches the signing private key from Vault/AWS KMS; never stores it in app memory beyond the request lifecycle.
- **Rate Limiter** — token endpoint protected by IP + client-ID rate limits (recommend: 10 req/s per client, 100 req/s per IP).
- **Audit Log** — every token issuance, revocation, and introspection call emits a structured event (`client_id`, `grant_type`, `user_id`, `timestamp`, `ip`) to a SIEM/log sink.

---

## Risks

1. **Authorization code replay** — mitigated by marking codes `used=true` atomically on first exchange (compare-and-swap in Redis with TTL).
2. **Refresh token theft** — mitigated by refresh token rotation (issue new token on each use, immediately revoke the old one) and binding tokens to client fingerprint.
3. **JWKS cache poisoning at resource servers** — mitigated by short cache TTL (5 min), `kid`-based key selection, and signing keys rotated on a 90-day schedule with overlap period.

---

## Done When

1. `POST /oauth/token` with a valid PKCE Authorization Code flow returns a JWT that resource servers can verify offline using `/jwks.json`, and replay of the same code returns `invalid_grant`.
2. `POST /oauth/token/revoke` on a refresh token causes all subsequent `/introspect` calls on tokens issued from it to return `"active": false` within 1 second.
3. A public client (SPA) with no `client_secret` can complete the full Authorization Code + PKCE flow end-to-end; a request missing `code_challenge` is rejected with `invalid_request`.

---

## Handoff

Build **`TokenStore`** first — it is the single point of truth that `AuthorizationEndpoint`, `TokenEndpoint`, and `IntrospectionEndpoint` all depend on. Implement atomic code consumption (`consumeCode` with a CAS operation in Redis) and refresh token revocation before any endpoint goes live. Schema migrations for `AuthorizationCode` and `RefreshToken` tables should be included in this first PR.
