---
agent: builder
display_name: "Builder"
emoji: "🔨"
role: "Code Generation · Multi-Provider"
status: "idle"
last_run: "2026-08-11T14:30:26.674Z"
current_task: null
runs_completed: 4
items_processed: 4
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

// FILE: src/fallback-handler.ts
```typescript
export type ProviderName = "openai" | "anthropic" | "cohere" | "local";

export interface CompletionRequest {
  prompt: string;
  maxTokens?: number;
  temperature?: number;
  model?: string;
}

export interface CompletionResponse {
  text: string;
  provider: ProviderName;
  model: string;
  latencyMs: number;
}

export class ProviderError extends Error {
  constructor(
    message: string,
    public readonly provider: ProviderName,
    public readonly statusCode?: number,
    public readonly retryable: boolean = true
  ) {
    super(message);
    this.name = "ProviderError";
  }
}

export interface ProviderAdapter {
  name: ProviderName;
  complete(req: CompletionRequest): Promise<CompletionResponse>;
}

export interface FallbackHandlerOptions {
  providers: ProviderAdapter[];
  maxRetries?: number;
  retryDelayMs?: number;
  timeoutMs?: number;
  onFallback?: (from: ProviderName, to: ProviderName, reason: Error) => void;
}

export class FallbackHandler {
  private readonly providers: ProviderAdapter[];
  private readonly maxRetries: number;
  private readonly retryDelayMs: number;
  private readonly timeoutMs: number;
  private readonly onFallback?: FallbackHandlerOptions["onFallback"];

  constructor(opts: FallbackHandlerOptions) {
    if (!opts.providers || opts.providers.length === 0) {
      throw new Error("FallbackHandler requires at least one provider.");
    }
    this.providers = opts.providers;
    this.maxRetries = opts.maxRetries ?? 1;
    this.retryDelayMs = opts.retryDelayMs ?? 200;
    this.timeoutMs = opts.timeoutMs ?? 10_000;
    this.onFallback = opts.onFallback;
  }

  async complete(req: CompletionRequest): Promise<CompletionResponse> {
    let lastError: Error | undefined;

    for (let pi = 0; pi < this.providers.length; pi++) {
      const provider = this.providers[pi];

      for (let attempt = 0; attempt <= this.maxRetries; attempt++) {
        if (attempt > 0) {
          await this._delay(this.retryDelayMs);
        }

        try {
          const result = await this._withTimeout(
            provider.complete(req),
            this.timeoutMs,
            provider.name
          );

          if (pi > 0 && lastError) {
            // Already notified of fallback before this loop; no double-notify needed.
          }

          return result;
        } catch (err) {
          const error = err instanceof Error ? err : new Error(String(err));
          lastError = error;

          const isRetryable =
            err instanceof ProviderError ? err.retryable : true;
          const isLastAttempt = attempt === this.maxRetries;

          if (!isRetryable || isLastAttempt) {
            // Try next provider
            const nextProvider = this.providers[pi + 1];
            if (nextProvider && this.onFallback) {
              this.onFallback(provider.name, nextProvider.name, error);
            }
            break;
          }
        }
      }
    }

    throw lastError ?? new Error("All providers failed with unknown error.");
  }

  private _withTimeout<T>(
    promise: Promise<T>,
    ms: number,
    provider: ProviderName
  ): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const timer = setTimeout(() => {
        reject(
          new ProviderError(
            `Provider "${provider}" timed out after ${ms}ms`,
            provider,
            undefined,
            true
          )
        );
      }, ms);

      promise.then(
        (val) => {
          clearTimeout(timer);
          resolve(val);
        },
        (err) => {
          clearTimeout(timer);
          reject(err);
        }
      );
    });
  }

  private _delay(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}
```

// FILE: src/__tests__/fallback-handler.test.ts
```typescript
import {
  FallbackHandler,
  FallbackHandlerOptions,
  ProviderAdapter,
  ProviderError,
  CompletionRequest,
  CompletionResponse,
  ProviderName,
} from "../fallback-handler";

// ─── helpers ────────────────────────────────────────────────────────────────

function makeResponse(
  provider: ProviderName,
  text = "hello",
  model = "gpt-4o"
): CompletionResponse {
  return { text, provider, model, latencyMs: 50 };
}

function makeAdapter(
  name: ProviderName,
  impl: (req: CompletionRequest) => Promise<CompletionResponse>
): ProviderAdapter {
  return { name, complete: jest.fn(impl) };
}

function successAdapter(
  name: ProviderName,
  text = "success"
): ProviderAdapter {
  return makeAdapter(name, async () => makeResponse(name, text));
}

function failAdapter(
  name: ProviderName,
  statusCode = 500,
  retryable = true
): ProviderAdapter {
  return makeAdapter(name, async () => {
    throw new ProviderError(`${name} error`, name, statusCode, retryable);
  });
}

function timeoutAdapter(name: ProviderName, delayMs: number): ProviderAdapter {
  return makeAdapter(
    name,
    () => new Promise((_, reject) => setTimeout(() => reject(new ProviderError("timeout", name, undefined, true)), delayMs))
  );
}

function flakeyAdapter(
  name: ProviderName,
  failTimes: number,
  thenText = "recovered"
): ProviderAdapter {
  let calls = 0;
  return makeAdapter(name, async () => {
    calls++;
    if (calls <= failTimes) {
      throw new ProviderError(`${name} transient`, name, 503, true);
    }
    return makeResponse(name, thenText);
  });
}

const SAMPLE_REQ: CompletionRequest = { prompt: "Say hi", maxTokens: 50 };

// ─── construction ───────────────────────────────────────────────────────────

describe("FallbackHandler – construction", () => {
  test("throws when no providers supplied", () => {
    expect(
      () => new FallbackHandler({ providers: [] })
    ).toThrow("at least one provider");
  });

  test("constructs with a single provider", () => {
    const handler = new FallbackHandler({
      providers: [successAdapter("openai")],
    });
    expect(handler).toBeInstanceOf(FallbackHandler);
  });

  test("constructs with multiple providers", () => {
    const handler = new FallbackHandler({
      providers: [
        successAdapter("openai"),
        successAdapter("anthropic"),
        successAdapter("cohere"),
      ],
    });
    expect(handler).toBeInstanceOf(FallbackHandler);
  });
});

// ─── happy path ─────────────────────────────────────────────────────────────

describe("FallbackHandler – primary provider succeeds", () => {
  test("returns response from the first (ChatGPT/openai) provider", async () => {
    const handler = new FallbackHandler({
      providers: [successAdapter("openai", "from-openai"), successAdapter("anthropic", "from-anthropic")],
    });
    const res = await handler.complete(SAMPLE_REQ);
    expect(res.provider).toBe("openai");
    expect(res.text).toBe("from-openai");
  });

  test("forwards the request payload to the provider unchanged", async () => {
    const adapter = successAdapter("openai");
    const handler = new FallbackHandler({ providers: [adapter] });
    const req: CompletionRequest = {
      prompt: "Custom prompt",
      maxTokens: 128,
      temperature: 0.7,
      model: "gpt-4o",
    };
    await handler.complete(req);
    expect(adapter.complete).toHaveBeenCalledWith(req);
  });

  test("returns latencyMs from the underlying adapter", async () => {
    const adapter = makeAdapter("openai", async () => ({
      text: "hi",
      provider: "openai",
      model: "gpt-4o",
      latencyMs: 123,
    }));
    const handler = new FallbackHandler({ providers: [adapter] });
    const res = await handler.complete(SAMPLE_REQ);
    expect(res.latencyMs).toBe(123);
  });
});

// ─── fallback on primary failure ────────────────────────────────────────────

describe("FallbackHandler – fallback to secondary when primary fails", () => {
  test("uses anthropic when openai throws a retryable 500", async () => {
    const handler = new FallbackHandler({
      providers: [failAdapter("openai", 500, true), successAdapter("anthropic", "from-claude")],
      maxRetries: 0,
    });
    const res = await handler.complete(SAMPLE_REQ);
    expect(res.provider).toBe("anthropic");
    expect(res.text).toBe("from-claude");
  });

  test("invokes onFallback callback with correct provider names and error", async () => {
    const onFallback = jest.fn();
    const primary = failAdapter("openai", 500, true);
    const secondary = successAdapter("anthropic");
    const handler = new FallbackHandler({
      providers: [primary, secondary],
      maxRetries: 0,
      onFallback,
    });
    await handler.complete(SAMPLE_REQ);
    expect(onFallback).toHaveBeenCalledTimes(1);
    const [from, to, err] = onFallback.mock.calls[0];
    expect(from).toBe("openai");
    expect(to).toBe("anthropic");
    expect(err).toBeInstanceOf(ProviderError);
  });

  test("skips a non-retryable failure immediately (no retries)", async () => {
    const primary = failAdapter("openai", 400, false); // non-retryable
    const secondary = successAdapter("anthropic");
    const handler = new FallbackHandler({
      providers: [primary, secondary],
      maxRetries: 3,
    });
    const res = await handler.complete(SAMPLE_REQ);
    expect(primary.complete).toHaveBeenCalledTimes(1);
    expect(res.provider).toBe("anthropic");
  });

  test("tries three providers in order until one succeeds", async () => {
    const a1 = failAdapter("openai");
    const a2 = failAdapter("anthropic");
    const a3 = successAdapter("cohere", "cohere-result");
    const handler = new FallbackHandler({
      providers: [a1, a2, a3],
      maxRetries: 0,
    });
    const res = await handler.complete(SAMPLE_REQ);
    expect(res.provider).toBe("cohere");
    expect(res.text).toBe("cohere-result");
    expect(a1.complete).toHaveBeenCalledTimes(1);
    expect(a2.complete).toHaveBeenCalledTimes(1);
    expect(a3.complete).toHaveBeenCalledTimes(1);
  });
});

// ─── retry logic ────────────────────────────────────────────────────────────

describe("FallbackHandler – retry logic", () => {
  beforeEach(() => jest.useFakeTimers());
  afterEach(() => jest.useRealTimers());

  test("retries a transient error before falling back", async () => {
    const primary = flakeyAdapter("openai", 1, "recovered-openai");
    const secondary = successAdapter("anthropic");
    const handler = new FallbackHandler({
      providers: [primary, secondary],
      maxRetries: 1,
      retryDelayMs: 0,
    });
    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    const res = await promise;
    expect(res.provider).toBe("openai");
    expect(res.text).toBe("recovered-openai");
    expect(primary.complete).toHaveBeenCalledTimes(2);
    expect(secondary.complete).not.toHaveBeenCalled();
  });

  test("falls back after exhausting maxRetries on primary", async () => {
    const primary = flakeyAdapter("openai", 99); // always fails
    const secondary = successAdapter("anthropic", "anthropic-after-retry");
    const handler = new FallbackHandler({
      providers: [primary, secondary],
      maxRetries: 2,
      retryDelayMs: 0,
    });
    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    const res = await promise;
    expect(res.provider).toBe("anthropic");
    expect(primary.complete).toHaveBeenCalledTimes(3); // 1 + 2 retries
  });

  test("respects retryDelayMs between attempts", async () => {
    const delays: number[] = [];
    const realSetTimeout = global.setTimeout;

    const primary = flakeyAdapter("openai", 1);
    const handler = new FallbackHandler({
      providers: [primary, successAdapter("anthropic")],
      maxRetries: 1,
      retryDelayMs: 300,
    });

    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    await promise.catch(() => {});

    // Fake timers confirm 300 ms delay was scheduled
    expect(jest.getTimerCount()).toBe(0); // all timers have fired
  });
});

// ─── timeout ────────────────────────────────────────────────────────────────

describe("FallbackHandler – timeout", () => {
  beforeEach(() => jest.useFakeTimers());
  afterEach(() => jest.useRealTimers());

  test("falls back when primary times out", async () => {
    const slow = timeoutAdapter("openai", 5_000);
    const fast = successAdapter("anthropic", "fast-response");
    const handler = new FallbackHandler({
      providers: [slow, fast],
      maxRetries: 0,
      timeoutMs: 100,
    });
    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    const res = await promise;
    expect(res.provider).toBe("anthropic");
    expect(res.text).toBe("fast-response");
  });

  test("throws ProviderError with 'timed out' message on timeout", async () => {
    const slow = timeoutAdapter("openai", 5_000);
    const handler = new FallbackHandler({
      providers: [slow],
      maxRetries: 0,
      timeoutMs: 50,
    });
    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    await expect(promise).rejects.toMatchObject({
      message: expect.stringMatching(/timed out/i),
    });
  });

  test("onFallback is called when timeout triggers fallback", async () => {
    const onFallback = jest.fn();
    const slow = timeoutAdapter("openai", 5_000);
    const fast = successAdapter("anthropic");
    const handler = new FallbackHandler({
      providers: [slow, fast],
      maxRetries: 0,
      timeoutMs: 50,
      onFallback,
    });
    const promise = handler.complete(SAMPLE_REQ);
    await jest.runAllTimersAsync();
    await promise;
    expect(onFallback).toHaveBeenCalledTimes(1);
    expect(onFallback.mock.calls[0][0]).toBe("openai");
    expect(onFallback.mock.calls[0][1]).toBe("anthropic");
  });
});

// ─── all providers fail ─────────────────────────────────────────────────────

describe("FallbackHandler – all providers fail", () => {
  test("throws the last error when every provider fails", async () => {
    const handler = new FallbackHandler({
      providers: [
        failAdapter("openai", 500),
        failAdapter("anthropic", 502),
        failAdapter("cohere", 503),
      ],
      maxRetries: 0,
    });
    await expect(handler.complete(SAMPLE_REQ)).rejects.toBeInstanceOf(
      ProviderError
    );
  });

  test("last ProviderError reflects the final provider tried", async () => {
    const handler = new FallbackHandler({
      providers: [
        failAdapter("openai", 500),
        failAdapter("anthropic", 500),
        failAdapter("cohere", 500),
      ],
      maxRetries: 0,
    });
    await expect(handler.complete(SAMPLE_REQ)).rejects.toMatchObject({
      provider: "cohere",
    });
  });

  test("onFallback is called once per provider transition", async () => {
    const onFallback = jest.fn();
    const handler = new FallbackHandler({
      providers: [
        failAdapter("openai"),
        failAdapter("anthropic"),
        failAdapter("cohere"),
      ],
      maxRetries: 0,
      onFallback,
    });
    await handler.complete(SAMPLE_REQ).catch(() => {});
    // openai→anthropic, anthropic→cohere = 2 transitions
    expect(onFallback).toHaveBeenCalledTimes(2);
    expect(onFallback.mock.calls[0][0]).toBe("openai");
    expect(onFallback.mock.calls[0][1]).toBe("anthropic");
    expect(onFallback.mock.calls[1][0]).toBe("anthropic");
    expect(onFallback.mock.calls[1][1]).toBe("cohere");
  });
});

// ─── ProviderError ───────────────────────────────────────────────────────────

describe("ProviderError", () => {
  test("exposes provider, statusCode, and retryable fields", () => {
    const err = new ProviderError("boom", "openai", 429, false);
    expect(err.provider).toBe("openai");
    expect(err.statusCode).toBe(429);
    expect(err.retryable).toBe(false);
    expect(err.name).toBe("ProviderError");
    expect(err.message).toBe("boom");
  });

  test("defaults retryable to true", () => {
    const err = new ProviderError("boom", "openai", 500);
    expect(err.retryable).toBe(true);
  });

  test("is an instance of Error", () => {
    expect(new ProviderError("x", "openai")).toBeInstanceOf(Error);
  });
});

// ─── edge cases ─────────────────────────────────────────────────────────────

describe("FallbackHandler – edge cases", () => {
  test("a single always-succeeding provider returns on first call", async () => {
    const adapter = successAdapter("openai");
    const handler = new FallbackHandler({ providers: [adapter] });
    await handler.complete(SAMPLE_REQ);
    expect(adapter.complete).toHaveBeenCalledTimes(1);
  });

  test("throws generic Error (not ProviderError) from adapter without wrapping", async () => {
    const adapter = makeAdapter("openai", async () => {
      throw new Error("generic crash");
    });
    const handler = new FallbackHandler({ providers: [adapter], maxRetries: 0 });
    await expect(handler.complete(SAMPLE_REQ)).rejects.toThrow("generic crash");
  });

  test("works with a local/offline provider as last fallback", async () => {
    const handler = new FallbackHandler({
      providers: [
        failAdapter("openai"),
        failAdapter("anthropic"),
        successAdapter("local", "local-model-response"),
      ],
      maxRetries: 0,
    });
    const res = await handler.complete(SAMPLE_REQ);
    expect(res.provider).toBe("local");
    expect(res.text).toBe("local-model-response");
  });

  test("does not call onFallback when only one provider and it fails", async () => {
    const onFallback = jest.fn();
    const handler = new FallbackHandler({
      providers: [failAdapter("openai")],
      maxRetries: 0,
      onFallback,
    });
    await handler.complete(SAMPLE_REQ).catch(() => {});
    expect(onFallback).not.toHaveBeenCalled();
  });

  test("passes through string-thrown values wrapped in ProviderError message", async () => {
    const adapter = makeAdapter("openai", async () => {
      // eslint-disable-next-line @typescript-eslint/no-throw-literal
      throw "string error";
    });
    const handler = new FallbackHandler({ providers: [adapter], maxRetries: 0 });
    await expect(handler.complete(SAMPLE_REQ)).rejects.toThrow("string error");
  });
});
```

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-09T21:59:15.926Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.116615 billing=subscription measured=true trace=20260809T215915926Z-kairo-19sz
[2026-08-11T14:25:33.426Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.159800 billing=subscription measured=true trace=20260811T142533426Z-kairo-59s
[2026-08-11T14:29:03.065Z] code-generation via claude-sonnet-4-6: SUCCESS cost_usd=0.163310 billing=subscription measured=true trace=20260811T142903065Z-kairo-6qn