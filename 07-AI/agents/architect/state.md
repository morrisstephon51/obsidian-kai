---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-04T01:48:21.543Z"
current_task: null
active_spec: null
runs_completed: 4
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

A standalone TypeScript utility function (`validateJwt`) that verifies the integrity, expiry, and claims of a JWT token against a configurable set of rules — supporting both symmetric (HMAC) and asymmetric (RSA/EC) key strategies, returning a typed result union so callers handle success and failure explicitly without relying on thrown exceptions.

---

## Key Decisions

1. **Result union over exceptions** — Returns `{ ok: true, payload: JwtPayload } | { ok: false, error: JwtError }` instead of throwing. Callers can't accidentally swallow a throw; the type system forces the error branch to be handled.

2. **`jose` library, not `jsonwebtoken`** — `jose` is Web Crypto-native, supports edge runtimes (Cloudflare Workers, Next.js Edge), has first-class ES module support, and handles both JWKS remote fetch and local keys uniformly. `jsonwebtoken` is Node-only and sync-only.

3. **JWKS URI as a first-class option** — Auth providers (Auth0, Keycloak, Cognito) rotate keys; caching the JWKS in-process with a TTL avoids per-request HTTP while staying rotation-safe. This is baked into the `KeySource` union rather than left to callers.

---

## Spec

### Data Models

```ts
// Key sources — local secret, local KeyLike, or remote JWKS
type KeySource =
  | { type: 'secret'; value: string | Uint8Array }
  | { type: 'jwks'; uri: string; cacheMaxAge?: number } // ms, default 600_000
  | { type: 'key'; value: KeyLike }

// Validation options
interface JwtValidateOptions {
  key: KeySource
  algorithms: string[]           // e.g. ['RS256', 'ES256', 'HS256']
  issuer?: string | string[]
  audience?: string | string[]
  clockTolerance?: number        // seconds, default 60
  requiredClaims?: string[]      // additional claims that must be present
}

// Standard + custom claims
interface JwtPayload {
  sub?: string
  iss?: string
  aud?: string | string[]
  exp?: number
  nbf?: number
  iat?: number
  jti?: string
  [claim: string]: unknown
}

// Error taxonomy
type JwtErrorCode =
  | 'EXPIRED'
  | 'NOT_YET_VALID'
  | 'INVALID_SIGNATURE'
  | 'INVALID_ISSUER'
  | 'INVALID_AUDIENCE'
  | 'MISSING_CLAIM'
  | 'MALFORMED'
  | 'KEY_FETCH_FAILED'
  | 'UNKNOWN'

interface JwtError {
  code: JwtErrorCode
  message: string
  cause?: unknown
}

// Return type
type JwtValidateResult =
  | { ok: true;  payload: JwtPayload }
  | { ok: false; error: JwtError }
```

### API Contract

```ts
// Primary export
async function validateJwt(
  token: string,
  options: JwtValidateOptions
): Promise<JwtValidateResult>

// Factory for performance: pre-wires key source & options, returns a bound validator
function createJwtValidator(
  options: JwtValidateOptions
): (token: string) => Promise<JwtValidateResult>
```

### Components

| Name | Responsibility | Interface |
|---|---|---|
| `validateJwt` | Orchestrates the full validation pipeline | `(token, options) => Promise<JwtValidateResult>` |
| `createJwtValidator` | Factory that closes over options; amortizes JWKS setup | `(options) => validator fn` |
| `resolveKey` | Resolves `KeySource` → `KeyLike` or JWKS getter; handles caching | `(source: KeySource) => Promise<KeyLike \| JWTVerifyGetKey>` |
| `JwksCache` | In-memory TTL cache for remote JWKS, keyed by URI | `get(uri): CachedJwks \| null`, `set(uri, jwks, ttl)` |
| `mapJoseError` | Converts `jose` internal errors → typed `JwtError` | `(err: unknown) => JwtError` |
| `assertRequiredClaims` | Checks `requiredClaims` are present on payload | `(payload, claims[]) => JwtError \| null` |

### Integration Points

- **Input**: raw JWT string (Bearer header value, cookie, etc.) — callers strip `"Bearer "` prefix
- **`jose`**: `jwtVerify`, `createRemoteJWKSSet`, `importSPKI`, `importSecret` — all from `jose` v5+
- **JWKS refresh**: `createRemoteJWKSSet` with `cacheMaxAge` passed through
- **Callers**: Express/Fastify middleware, Next.js Route Handlers, tRPC context builders — each wraps `validateJwt` and maps `ok: false` to the appropriate HTTP 401 response

---

## Risks

| Risk | Mitigation |
|---|---|
| JWKS fetch fails mid-request (network timeout, provider outage) | Serve stale cache under a `staleTtl` window; surface `KEY_FETCH_FAILED` so callers can fail-open or fail-closed by policy |
| Clock skew between issuer and validator causes spurious `EXPIRED` rejections | Expose `clockTolerance` (default 60 s); document it; do not hard-code |
| Caller passes `algorithms: []` or `['none']` accidentally | Guard at validation entry: reject empty array and the `"none"` algorithm with a thrown `TypeError` before any crypto runs |

---

## Done When

1. `validateJwt(validToken, opts)` returns `{ ok: true, payload }` with correct claims for HS256, RS256, and ES256 tokens — verified by unit tests with locally generated keys.
2. `validateJwt(expiredToken, opts)` returns `{ ok: false, error: { code: 'EXPIRED' } }` and never throws.
3. `createJwtValidator` with a JWKS URI option makes exactly one HTTP request across 10 consecutive calls within the cache TTL window — verified by intercepting `fetch` in tests.

---

## Handoff

**Build `resolveKey` + `JwksCache` first.** Everything else — `validateJwt`, the factory, the error mapper — depends on knowing a key is available. Stub `mapJoseError` and `assertRequiredClaims` as no-ops, wire `resolveKey` against a real JWKS endpoint in an integration test, and confirm caching behavior before touching the verification logic.
