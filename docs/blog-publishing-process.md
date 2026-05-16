# Blog Publishing Process

This is the canonical operating flow for Korea Invest Insights posts. GitHub
Pages remains the source of truth for publishing. External channels are a
post-publish distribution stage, so they run only after the canonical blog URL
is live.

## Standard Flow

1. Write or update the post in `content/post/*/index.<lang>.md`.
2. Validate locally:

   ```bash
   git diff --check
   hugo --minify
   ```

3. Commit and push the post.
4. Wait for the GitHub Pages deploy to complete.
5. Run the local distribution stage, or let launchd run it on the next cycle:

   ```bash
   scripts/post_publish_distribution.py
   ```

The distribution command includes Valley Space, Telegram channel alerts,
Botmadang finance posts, and Substack for posts that have an English version.

## Distribution Stage

`scripts/post_publish_distribution.py` calls the local distribution adapters
with the same safe defaults used by launchd:

- Korean posts only
- last 14 days only
- maximum 3 posts per run
- `--body-mode auto`
- canonical URL must already be live
- local per-channel de-duplication logs prevent repeat posts

Channel behavior:

- `valley`: publishes Korean posts to Valley using the local Valley session or
  API token.
- `telegram`: sends a public Telegram channel alert through the legacy
  OpenClaw notifier.
- `botmadang`: posts a short Korean finance-community summary to Botmadang.
- `substack`: publishes only when `index.en.md` exists; Korean-only posts are
  recorded as skipped so the job does not retry forever.

For a dry-run:

```bash
scripts/post_publish_distribution.py --dry-run
```

For urgent manual publishing after the GitHub Pages deploy is live:

```bash
scripts/post_publish_distribution.py --channels valley,telegram,botmadang,substack
```

For normal publishing, no manual action is required if the local LaunchAgent is
enabled. The LaunchAgent runs every 10 minutes and uses the same per-channel
de-duplication logs.

## Valley Content Policy

Valley is part of the distribution stage, not the canonical archive. The
default body mode is `auto`:

- evergreen company, sector, stock, Why Korea, and analyst-report articles use
  teaser format
- shorter market, macro, and daily intelligence articles may publish full text
- long or table-heavy posts stay teaser format

Override per post when needed:

```yaml
valley_body_mode: full
```

or:

```yaml
valley_body_mode: teaser
```

Valley stock-link signals are handled with a short `관련 종목` block. Override
the inferred names when needed:

```yaml
valley_cashtags:
  - 삼성전자
  - SK하이닉스
```

## Safety Boundary

Do not put a Valley browser session cookie into GitHub Actions or the
repository. Cookie-backed Valley publishing is local-only and reads secrets
from:

```text
~/.config/korea-invest-insights/valley.env
```

The GitHub workflow has an optional Valley job for a future official API token,
but the active production path is local post-publish distribution.
