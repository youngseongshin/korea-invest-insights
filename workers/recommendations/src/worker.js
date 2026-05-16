const DEFAULT_ALLOWED_ORIGINS = [
  "https://koreainvestinsights.com",
  "https://www.koreainvestinsights.com",
  "http://localhost:1313",
];

function json(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      ...headers,
    },
  });
}

function corsHeaders(request, env) {
  const origin = request.headers.get("Origin") || "";
  const allowed = (env.ALLOWED_ORIGINS || DEFAULT_ALLOWED_ORIGINS.join(","))
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);

  if (!allowed.includes(origin)) return {};

  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Accept",
    "Vary": "Origin",
  };
}

function validateKey(key) {
  if (typeof key !== "string") return "";
  const normalized = key.trim();
  if (normalized.length < 3 || normalized.length > 220) return "";
  if (!/^[a-zA-Z0-9:_./-]+$/.test(normalized)) return "";
  return normalized;
}

async function sha256Hex(input) {
  const encoded = new TextEncoder().encode(input);
  const hash = await crypto.subtle.digest("SHA-256", encoded);
  return Array.from(new Uint8Array(hash), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function getCount(db, key) {
  const row = await db
    .prepare("SELECT count FROM recommendations WHERE post_key = ?")
    .bind(key)
    .first();

  return row ? Number(row.count || 0) : 0;
}

async function handleGet(request, env, headers) {
  const url = new URL(request.url);
  const key = validateKey(url.searchParams.get("key"));
  if (!key) return json({ ok: false, error: "invalid_key" }, 400, headers);

  const count = await getCount(env.DB, key);
  return json({ ok: true, key, count }, 200, headers);
}

async function handlePost(request, env, headers) {
  let payload;
  try {
    payload = await request.json();
  } catch (_) {
    return json({ ok: false, error: "invalid_json" }, 400, headers);
  }

  const key = validateKey(payload && payload.key);
  const voter = typeof payload?.voter === "string" ? payload.voter.trim() : "";

  if (!key) return json({ ok: false, error: "invalid_key" }, 400, headers);
  if (voter.length < 8 || voter.length > 160) {
    return json({ ok: false, error: "invalid_voter" }, 400, headers);
  }

  const salt = env.VOTE_SALT || "";
  const voterHash = await sha256Hex(`${key}:${voter}:${salt}`);

  const voteInsert = await env.DB
    .prepare("INSERT OR IGNORE INTO recommendation_votes (post_key, voter_hash) VALUES (?, ?)")
    .bind(key, voterHash)
    .run();

  const counted = Number(voteInsert.meta?.changes || 0) > 0;

  if (counted) {
    await env.DB
      .prepare(
        `INSERT INTO recommendations (post_key, count, updated_at)
         VALUES (?, 1, CURRENT_TIMESTAMP)
         ON CONFLICT(post_key)
         DO UPDATE SET count = count + 1, updated_at = CURRENT_TIMESTAMP`
      )
      .bind(key)
      .run();
  }

  const count = await getCount(env.DB, key);
  return json({ ok: true, key, count, counted }, 200, headers);
}

export default {
  async fetch(request, env) {
    const headers = corsHeaders(request, env);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers });
    }

    if (!env.DB) {
      return json({ ok: false, error: "missing_d1_binding" }, 500, headers);
    }

    try {
      if (request.method === "GET") return handleGet(request, env, headers);
      if (request.method === "POST") return handlePost(request, env, headers);
      return json({ ok: false, error: "method_not_allowed" }, 405, headers);
    } catch (error) {
      return json(
        {
          ok: false,
          error: "internal_error",
          message: error instanceof Error ? error.message : "Unknown error",
        },
        500,
        headers
      );
    }
  },
};
