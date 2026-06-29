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

Korean writing quality defaults:

- Treat Korean readability as a publish blocker for every `index.ko.md`, not as
  a cosmetic pass after publishing.
- Avoid the em dash character `—` in Korean posts. Rewrite with a comma, colon,
  parentheses, or a separate sentence.
- Avoid raw Markdown bold markers such as `**...**` in Korean source. They can
  leak as literal text in downstream surfaces or mixed HTML blocks. Prefer
  `<strong>...</strong>` only when emphasis is truly useful, or remove the
  emphasis.
- Do not use raw `**` in frontmatter, tables, callouts, HTML snippets, Telegram
  messages, Substack blurbs, LinkedIn copy, or other external summaries.
- Remove AI-slop wording before publish: translationese, stiff English word
  order, repeated formulaic phrases, unnatural Korean nouns/verbs, and
  over-polished but vague sentences. Keep analytical density, but make the
  Korean sound like a human investment memo.
- Prefer natural Korean expressions. Keep English market terms only when they
  are standard for the intended reader, and explain them once if the term is
  doing analytical work.
- Read the title, TL;DR, and highlighted callouts aloud before publishing. If
  they sound like directly translated English, rewrite them.

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
   scripts/check_korean_post_style.py content/post/<post-slug>/index.ko.md
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
- **LinkedIn**: manual-approval only publishing to the configured
  **personal LinkedIn profile**. On publish, `post_publish_distribution.py`
  only STAGES the post (composed title + teaser + canonical URL) into a pending
  queue. It must not post or approve automatically as part of routine blog
  post-process. The user reviews and approves manually with
  `scripts/linkedin_approve.py`, which posts via the LinkedIn Posts API
  (`scripts/linkedin_notify.py`). It is a default staging channel but optional:
  if no token is configured it silently skips, and it never blocks the other
  channels. One-time setup below.

  ```bash
  scripts/linkedin_approve.py --list   # see what is queued
  scripts/linkedin_approve.py          # review + approve each (y/N)
  scripts/linkedin_approve.py --slug <slug>   # approve one
  ```

  Do not run automatic approval from normal publishing tasks:
  `scripts/linkedin_approve.py --all --yes`,
  `scripts/linkedin_approve.py --slug <slug> --yes`, and
  `linkedin-share approve --yes` are blocked by default. A one-off manual
  exception requires `KII_LINKEDIN_ALLOW_AUTO_APPROVE=1`.

  The same capability is available system-wide as a reusable asset for any task
  (`linkedin-share` on PATH → `~/.openclaw/workspace/tools/linkedin_share.py`),
  sharing the same token and approval queue:

  ```bash
  linkedin-share post  "comment" --link https://...   # explicit one-off post only
  linkedin-share stage "draft"   --link https://...   # queue for approval
  linkedin-share list ; linkedin-share approve         # interactive approval
  ```

  See the vault note `90_meta/linkedin-share-capability.md`.
- **Valley**: paused by default after the abnormal-access warning. The code path
  remains available for explicit recovery, but do not include it in default
  follow-up distribution until the user resumes Valley posting.

The default channel set is:

```text
telegram,botmadang,substack,linkedin
```

### LinkedIn one-time setup

LinkedIn posting needs a member access token (`w_member_social`), but automatic
posting is disabled by policy. The token and app credentials live ONLY in a
local secrets file, never in the repo or GitHub Actions:

```text
~/.config/korea-invest-insights/linkedin.env
```

Steps (the user authorizes in their own browser; the tooling never handles the
password):

1. On developer.linkedin.com: create an app, add the products "Share on
   LinkedIn" and "Sign In with LinkedIn using OpenID Connect", and add the
   redirect URL `http://localhost:8473/callback`.
2. Put the app Client ID/Secret in `linkedin.env`
   (`LINKEDIN_CLIENT_ID=...`, `LINKEDIN_CLIENT_SECRET=...`).
3. Run `python3 scripts/linkedin_oauth_setup.py`, click "Allow" in the browser.
   It writes the access token, refresh token, expiry and member URN into
   `linkedin.env`.
4. Test: `scripts/post_publish_distribution.py --slug <slug> --channels linkedin --max-posts 1`.

The member token is valid ~60 days; a refresh token (if the app is approved for
it) renews silently for ~1 year, otherwise re-run the setup script when posting
starts failing with an auth error.

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
