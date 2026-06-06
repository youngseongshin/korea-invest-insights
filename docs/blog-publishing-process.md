# Blog Publishing Process

This is the canonical operating flow for Korea Invest Insights posts. The
OpenClaw blog publish pipeline remains the source of truth: it creates the
multilingual Hugo files, commits/pushes them, submits IndexNow, and then runs a
single post-live distribution stage. That stage keeps Telegram, Botmadang, and
Substack aligned from the same canonical blog URL. Valley remains available as
an explicit opt-in channel, but it is not part of the default flow while Valley
posting is paused.

## Standard Flow

Default operator rule:

- When the user asks for a blog post, treat the request as a full publish task
  unless they explicitly say otherwise.
- The full publish task includes multilingual generation, Hugo validation,
  commit/push, live URL confirmation, and targeted post-publish distribution.
- Korean-only manual posts are allowed only as an explicit exception. Otherwise,
  create the English version and translated language files before distribution
  so Substack can run instead of recording `skip_no_english`.
- The post-publish distribution script now enforces the complete multilingual
  set. A new post cannot be sent to Telegram, Botmadang, Substack, or Valley
  until these seven files exist: `index.ko.md`, `index.en.md`, `index.es.md`,
  `index.vi.md`, `index.fr.md`, `index.ja.md`, and `index.zh.md`.

Source-fidelity rule for detailed research attachments:

- Treat a detailed attached report as a **source manuscript to restructure**,
  not as a short memo to summarize. The Korean post should preserve the original
  report's analytical density unless the user explicitly asks for a brief post.
- Keep the source report's major sections, tables, scenario grids, valuation
  arithmetic, catalysts, invalidation conditions, red-team arguments, and
  `[Fact] / [Inference] / [Speculation] / [Blocked]` distinctions when they are
  present. Convert them into blog-friendly headings and prose, but do not drop
  them merely to make the post shorter.
- If the source includes multiple analytical angles, publish them as separate
  sections rather than collapsing them into one conclusion. A good post can be
  long when the input is a full report.
- Shorten only duplicated wording, raw collection notes, execution logs,
  malformed fragments, or details that are clearly outside the requested topic.
  If a potentially important detail is omitted, make that omission intentional
  and explain it briefly in the working notes or final report.
- For translations, preserve the same core structure as the Korean version.
  Translations may be slightly tighter for readability, but they should not
  remove central evidence, tables, risk checks, or investment conclusions.

1. Publish through the OpenClaw blog pipeline when creating a new post. This is
   the normal path for multilingual posts:

   ```python
   from blog_publish_pipeline import publish_blog

   publish_blog(english_md=english_content, korean_md=korean_content)
   ```

2. For manual Hugo edits, update `content/post/*/index.<lang>.md`. If a new
   post is created manually, add the complete multilingual file set before
   the post-publish distribution stage:

   ```text
   index.ko.md
   index.en.md
   index.es.md
   index.vi.md
   index.fr.md
   index.ja.md
   index.zh.md
   ```
3. Validate locally:

   ```bash
   git diff --check
   hugo --minify
   ```

4. Commit and push the post.
5. Wait for the GitHub Pages deploy to complete.
6. Run the unified post-publish distribution stage after the GitHub Pages URL is
   live. For Codex/manual blog publishing tasks, this is mandatory unless the
   user explicitly says not to run follow-up distribution. This stage refuses
   to run if any required translation file is missing:

   ```bash
   scripts/post_publish_distribution.py --slug <post-slug> --max-posts 1
   ```

   The local LaunchAgent can still catch missed posts on its 10-minute cycle,
   but it is a backup, not a substitute for the active publishing task.

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
  failures. That skip is retryable: if `index.en.md` is added later, the
  Substack channel may publish the post on the next targeted run.
- **Valley**: paused by default after the abnormal-access warning. The code path
  remains available for explicit recovery, but do not include it in default
  follow-up distribution until the user resumes Valley posting.

The default channel set is:

```text
telegram,botmadang,substack
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
scripts/post_publish_distribution.py --slug <post-slug> --max-posts 1
```

For normal background recovery, no manual action is required if the local
LaunchAgent is enabled. It runs every 10 minutes and each channel uses its own
de-duplication log. During an active Codex publishing task, however, run the
targeted `--slug` command directly and report the channel results.

When the unified wrapper is enabled for an already-running installation, the
first non-dry-run pass writes a `unifiedDistributionActivatedAt` watermark per
non-Valley channel. This prevents older manually published posts from being
backfilled unexpectedly. Explicit recovery still works with `--allow-backfill`
and a targeted `--channels` value.

Distribution eligibility is based on the Git add time of the language-specific
post file, not the file modification time. Editing an existing article should
therefore deploy the blog change silently without re-sending Telegram,
Botmadang, Substack, or Valley notifications. If the Git add time is unavailable,
the scripts fall back to the frontmatter `date`, then to file modification time.

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
