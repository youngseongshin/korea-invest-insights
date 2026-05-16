# Blog Publishing Process

This is the canonical operating flow for Korea Invest Insights posts. The
OpenClaw blog publish pipeline remains the source of truth: it creates the
multilingual Hugo files, commits/pushes them, submits IndexNow, publishes the
English Substack copy, sends Telegram alerts, and posts to Botmadang. Valley is
an additional local-only step at the end of that existing pipeline.

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
6. Valley is handled either by the OpenClaw pipeline's final step or by the
   local Valley-only LaunchAgent on the next cycle:

   ```bash
   scripts/run_valley_auto_publish.sh
   ```

Do not use the Valley LaunchAgent to send Telegram, Botmadang, or Substack. Those
belong to the canonical OpenClaw publish pipeline.

## Channel Ownership

Channel ownership is intentionally split:

- **Substack**: OpenClaw `blog_publish_pipeline.py`, English version only.
- **Telegram**: OpenClaw `blog_publish_pipeline.py`, after the live URL exists.
- **Botmadang**: OpenClaw `blog_publish_pipeline.py`, after the live URL exists.
- **Valley**: added at the end of `blog_publish_pipeline.py`; the local
  LaunchAgent is a Valley-only safety net for posts that were committed manually.

`scripts/post_publish_distribution.py` is kept only as a thin Valley wrapper for
legacy launchd compatibility. It supports `--channels valley` only.

For a Valley dry-run:

```bash
scripts/valley_auto_publish.py --dry-run
```

For urgent manual Valley publishing after the GitHub Pages deploy is live:

```bash
scripts/valley_auto_publish.py --max-posts 1
```

For normal publishing, no manual Valley action is required if the local
LaunchAgent is enabled. It runs every 10 minutes and uses the Valley
de-duplication log.

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
