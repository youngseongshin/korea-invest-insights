# Blog Publishing Process

This is the canonical operating flow for Korea Invest Insights posts. The
OpenClaw blog publish pipeline remains the source of truth: it creates the
multilingual Hugo files, commits/pushes them, submits IndexNow, and then runs a
single post-live distribution stage. That stage keeps Telegram, Botmadang,
Substack, and Valley aligned from the same canonical blog URL.

## Standard Flow

1. Publish through the OpenClaw blog pipeline when creating a new post. This is
   the normal path for multilingual posts:

   ```python
   from blog_publish_pipeline import publish_blog

   publish_blog(english_md=english_content, korean_md=korean_content)
   ```

2. For manual Hugo edits, update `content/post/*/index.<lang>.md`.
3. Validate locally:

   ```bash
   git diff --check
   hugo --minify
   ```

4. Commit and push the post.
5. Wait for the GitHub Pages deploy to complete.
6. Run the unified post-publish distribution stage, or let the local LaunchAgent
   pick it up on the next 10-minute cycle:

   ```bash
   scripts/run_post_publish_distribution.sh
   ```

The legacy `scripts/run_valley_auto_publish.sh` entrypoint is still present for
launchd compatibility, but it now delegates to the unified distribution stage.

## Channel Ownership

All channel notifications are now run from one post-live wrapper:

- **Telegram**: `scripts/post_publish_distribution.py` calls OpenClaw
  `blog_channel_notify.py` after the live URL exists.
- **Botmadang**: `scripts/post_publish_distribution.py` calls OpenClaw
  `blog_botmadang_notify.py` after the live URL exists.
- **Substack**: `scripts/post_publish_distribution.py` publishes the English
  version only. Korean-only posts are logged as `skip_no_english`, not treated as
  failures.
- **Valley**: `scripts/post_publish_distribution.py` calls the local
  Valley publisher with the selected body mode.

The default channel set is:

```text
telegram,botmadang,substack,valley
```

Override only for targeted recovery:

```bash
scripts/post_publish_distribution.py --channels telegram,botmadang
```

For a full dry-run:

```bash
scripts/post_publish_distribution.py --dry-run --max-posts 1 --no-require-live
```

For urgent manual full distribution after the GitHub Pages deploy is live:

```bash
scripts/post_publish_distribution.py --max-posts 1
```

For normal publishing, no manual action is required if the local LaunchAgent is
enabled. It runs every 10 minutes and each channel uses its own de-duplication
log.

When the unified wrapper is enabled for an already-running installation, the
first non-dry-run pass writes a `unifiedDistributionActivatedAt` watermark per
non-Valley channel. This prevents older manually published posts from being
backfilled unexpectedly. Explicit recovery still works with `--allow-backfill`
and a targeted `--channels` value.

## Valley Content Policy

Valley is part of the distribution stage, not the canonical archive.

For non-full posts, Valley uses the same community-summary body as Botmadang.
The only Valley-specific additions are visible stock-name cashtags and hashtags.
This keeps the short-form distribution message consistent across the two
community channels.

The shared summary cache lives outside the repository:

```text
~/.local/share/korea-invest-insights/community_summary_cache.json
```

The default body mode is `auto`:

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

Automatic Valley cashtags come only from high-signal fields: explicit
`valley_cashtags`, six-digit ticker tags, known Korean company-name tags, and
company names in the title or description. The full body is not scanned because
related-post links and market context can mention Samsung Electronics or SK
Hynix even when they are not the post's true subject.

When a title or description must mention a company that should not become a
Valley stock link, exclude it explicitly:

```yaml
valley_cashtag_exclude:
  - 삼성전자
  - SK하이닉스
```

The Valley payload writes each related stock and hashtag on its own line:

```text
관련 종목
$하나마이크론
$제주반도체

해시태그
#AI후공정
#메모리
```

This mirrors the Valley editor behavior of typing a token and pressing Enter so
the platform can resolve the internal stock and hashtag links.
Stock-name tags and six-digit ticker tags are skipped from this hashtag block
because the stock-link block already carries them as `$종목명`.

## Safety Boundary

Do not put a Valley browser session cookie into GitHub Actions or the
repository. Cookie-backed Valley publishing is local-only and reads secrets
from:

```text
~/.config/korea-invest-insights/valley.env
```

The GitHub workflow has an optional Valley job for a future official API token,
but the active production path is local post-publish distribution.
