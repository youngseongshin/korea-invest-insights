# Post Recommendations

The Hugo site can render a lightweight reader recommendation button under each
post. It is disabled by default unless a recommendation API endpoint is
configured at build time.

## Frontend behavior

- The widget appears only on `post` pages.
- All translations of the same leaf-bundle post share one key:
  `post:<bundle-slug>`.
- The browser stores a random local voter ID in `localStorage`.
- One browser can recommend a post once. The server also deduplicates using a
  salted SHA-256 hash of `post key + voter id`.
- No IP address, email, or login identity is stored by the provided worker.

## Enabling the widget

Deploy the worker in `workers/recommendations`, then set this GitHub Actions
secret:

```text
HUGO_RECOMMENDATIONS_API=https://koreainvestinsights.com/api/recommendations
```

The Hugo build reads that environment variable and automatically renders the
widget. If the secret is empty, no button is rendered, so the live site does not
show a broken API call.

## Cloudflare D1 setup

From `workers/recommendations`:

```bash
wrangler d1 create korea-invest-insights-recommendations
cp wrangler.toml.example wrangler.toml
# Fill database_id in wrangler.toml.
wrangler d1 execute korea-invest-insights-recommendations --file=./schema.sql
wrangler secret put VOTE_SALT
wrangler deploy
```

Recommended Worker route:

```text
koreainvestinsights.com/api/recommendations
```

After the route is live, set `HUGO_RECOMMENDATIONS_API` and redeploy the Hugo
site.
