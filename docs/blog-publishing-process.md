# Blog Publishing Process

This is the canonical operating flow for Korea Invest Insights posts. The
OpenClaw blog publish pipeline remains the source of truth: it creates the
English and Korean Hugo files, commits/pushes them, submits IndexNow, and then
runs the post-live stage. In that stage the English post goes to Substack first,
from a logged-in built-in browser, with a Substack Note. Telegram, Botmadang and
LinkedIn follow from the same canonical blog URL. Valley remains available as
an explicit opt-in channel, but it is not part of the default flow while Valley
posting is paused.

Owner directive 2026-10-23 (Registry M-20261023-25):

- Substack English publication is the top priority of the post-live stage. It
  runs before every other channel, through the browser path in
  [Substack operations](#substack-operations), with figures, tables and
  footnotes intact, and it ends with a Note.
- The blog publishes English and Korean only. Spanish, Vietnamese, French,
  Japanese and Chinese are on hold. Do not create those files for new posts.
  Existing translations stay live.
- Every other rule, editing pass and post-process in this document is unchanged.

## Standard Flow

Default operator rule:

- When the user asks for a blog post, treat the request as a full publish task
  unless they explicitly say otherwise.
- The full publish task includes the English and Korean versions, Hugo
  validation, commit/push, live URL confirmation, Substack English publication
  with a Note, and targeted post-publish distribution.
- Korean-only manual posts are allowed only as an explicit exception. Otherwise,
  create the English version before distribution so Substack can run instead of
  recording `skip_no_english`.
- The post-publish distribution script enforces the publishing set. A new post
  cannot be sent to any channel until `index.ko.md` and `index.en.md` exist.

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
- For the English version, preserve the same core structure as the Korean
  version. It may be slightly tighter for readability, but it should not
  remove central evidence, tables, risk checks, or investment conclusions.

Korean writing quality defaults:

- Treat Korean readability as a publish blocker for every `index.ko.md`, not as
  a cosmetic pass after publishing.
- Use the writing rhythm of the live [YS-VC blog](https://www.ys-vc.com/blog)
  as the default Korean reference: calm `합니다` prose, a concrete opening,
  short paragraphs, and section headings that state the answer. This borrows
  the writing style only. Korea Invest Insights still keeps its listed-stock
  analysis, valuation, scenarios, and investment judgment.
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

### Easy Korean house style

The target is not a shorter or less rigorous report. The target is a report
that a reader can follow on the first pass.

- Open with the event, number, or tension that made the post worth writing.
  Within the first three short paragraphs, tell the reader what happened, why
  it matters, and what judgment the article will test. Do not begin with the
  writing process, a table of contents, or a generic market introduction.
- Use one paragraph for one claim. Two to four sentences is the normal range.
  A long report may have many paragraphs; it should not have dense walls of
  text. Split a paragraph when it changes from fact to interpretation, from one
  company to another, or from upside to risk.
- Make section headings carry information. Prefer `전력 대기열이 서버보다
  오래 걸립니다` to `현황 분석`, and `수요는 사라진 것이 아니라 2027년으로
  밀렸습니다` to `반도체 영향`. Avoid process-only headings such as `총정리`,
  `비교 분석`, `살펴보기`, and `매칭 매트릭스`.
- Prefer ordinary Korean verbs and concrete nouns. Write `기업가치` before
  `밸류에이션`, `가격 협상력` before `프라이싱 파워`, and `무효 조건` before
  `invalidation`. If an English market term is needed, explain it in Korean at
  first use and use the shorter Korean expression afterward.
- Use a familiar analogy only when it removes real abstraction. One clear
  analogy, followed immediately by the data and its limits, is better than a
  chain of metaphors.
- Introduce a table or figure with the question it answers. Follow it with one
  plain sentence explaining what changes for the investor. A table is evidence,
  not a substitute for prose.
- Keep the distinction between fact, inference, speculation, and blocked
  evidence, but do not mechanically prefix every paragraph. Use explicit
  labels for disputed or uncertain claims; elsewhere write natural sentences
  such as `공시로 확인된 것은 여기까지입니다` or `이 대목은 추정입니다`.
- Keep the title concrete and answer-shaped. A good title names the company,
  event, or bottleneck and makes one claim. Avoid report labels, vague question
  titles, and titles built around a numbered list.
- Keep the opening summary to three to five conclusions. Each item should say
  both what happened and why it matters. Do not repeat the same summary again
  in a final conclusion.

Run three editing passes before validation:

1. **Structure pass**: check the opening, argument order, and answer-shaped
   headings.
2. **Plain-language pass**: shorten long paragraphs, split overloaded
   sentences, and replace avoidable jargon.
3. **Evidence pass**: confirm that numbers, source attribution, scenarios,
   counterarguments, valuation arithmetic, and invalidation conditions survived
   the readability edit.

1. Publish through the OpenClaw blog pipeline when creating a new post. This is
   the normal path for English and Korean posts:

   ```python
   from blog_publish_pipeline import publish_blog

   publish_blog(english_md=english_content, korean_md=korean_content)
   ```

2. For manual Hugo edits, update `content/post/*/index.<lang>.md`. If a new
   post is created manually, add both files before the post-live stage:

   ```text
   index.ko.md
   index.en.md
   ```

   Do not add `index.es.md`, `index.vi.md`, `index.fr.md`, `index.ja.md` or
   `index.zh.md` to new posts while those languages are on hold.
3. Validate locally:

   ```bash
   scripts/check_korean_post_style.py content/post/<post-slug>/index.ko.md
   git diff --check
   hugo --minify
   ```

4. Commit and push the post.
5. Wait for the GitHub Pages deploy to complete.
6. Publish the English post on Substack first, after the GitHub Pages URL is
   live. Use the browser path in [Substack operations](#substack-operations):
   log in from the Claude Code or Codex built-in browser, convert, verify,
   publish, post the Note, and record the receipt. This is the top-priority
   post-live step.
7. Run the unified post-publish distribution stage. For Codex/manual blog
   publishing tasks, this is mandatory unless the user explicitly says not to
   run follow-up distribution. It refuses to run if `index.ko.md` or
   `index.en.md` is missing. It checks the Substack receipt first and stops the
   other channels when the receipt is missing:

   ```bash
   scripts/post_publish_distribution.py --slug <post-slug> --max-posts 1
   ```

   To run the other channels without Substack, the user must say so; then pass
   `--channels telegram,botmadang,linkedin`. No LaunchAgent backup for this
   stage is installed (checked 2026-10-23). If one is installed again, it also
   waits for the Substack receipt.

The legacy `scripts/run_valley_auto_publish.sh` entrypoint is still present for
launchd compatibility, but it now delegates to the unified distribution stage.

## Channel Ownership

All channel notifications are now run from one post-live wrapper:

- **Telegram**: `scripts/post_publish_distribution.py` calls OpenClaw
  `blog_channel_notify.py` after the live URL exists.
- **Botmadang**: `scripts/post_publish_distribution.py` calls OpenClaw
  `blog_botmadang_notify.py` after the live URL exists.
- **Substack**: the English version only, published first from the built-in
  browser (see [Substack operations](#substack-operations)).
  `scripts/post_publish_distribution.py` runs this channel first in `browser`
  mode: it does not publish, it checks the receipt that
  `scripts/substack_record_browser_publish.py` writes. Without a receipt it
  reports `pending_browser_publish` and marks the other channels
  `blocked_by_substack`. `--substack-mode api` runs the old cookie publisher
  for a short plain-text post only. Korean-only posts are logged as
  `skip_no_english`, not treated as failures. That skip is retryable: if
  `index.en.md` is added later, the Substack channel runs again.
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

The default channel set, in run order, is:

```text
substack,telegram,botmadang,linkedin
```

### Substack operations

Since 2026-10-23 the browser path below is the standard Substack route for every
English post. It keeps figures, tables and footnotes, and it ends with a Note.
The cookie API path (`substack_publisher.py` in the Gyeokja workspace tools) is
off by default: it converts only plain markdown (no images, no footnotes, tables
become pipe-joined lines), and its stored cookie fails the publish gate. The
unattended daily job (`blog_publish_pipeline.py`) therefore creates no Substack
draft; it logs `[SUBSTACK] 브라우저 발행 대기`. `KII_SUBSTACK_API=1` turns the
cookie path back on, and it then runs only after the publish gate passes.

#### Browser path (standard)

Who does what:

- The agent works in the Claude Code built-in browser (browser pane with
  `javascript_tool`) or the Codex built-in browser. Use a browser whose page can
  run JavaScript in the logged-in Substack tab.
- The user logs in. The agent never types a password or a sign-in code, never
  reads cookies, and never reads a browser credential store. When a login screen
  appears, ask the user to log in and wait.
- `send:true` emails every subscriber. The user's request to publish the post
  covers it; for a fix of a published post use `send:false`.

Before you start, commit and push the post and wait until the GitHub Pages URL is
live. The pane denies local-network access, so the script pulls the markdown from
raw GitHub and the SVGs from the live site, which are public and CORS-open.

1. Open `https://koreainvestinsights.substack.com/publish/post/<draftId>`. Reuse an
   existing draft or create an empty one from the dashboard. If a login screen
   appears, ask the user to log in.
2. Paste `scripts/substack_pane_push.js` into the page once. Run
   `window.__kiiRun({slug, draft, dry:true})` and read `window.__kii`:
   `summary` (blocks, images, footnotes, unusedDefs) must match the post
   (figures + tables, footnote definitions), and `lint` must be empty.
3. Run `window.__kiiRun({slug, draft})` without `dry`. Poll `window.__kii` until
   `step` is `done`; never await the run. The converter turns SVG figures and
   `![alt](/path.svg|png)` images into PNG, markdown tables into PNG (Substack has
   no table node), `[^key]` into native footnotes, handles a missing cover, links
   only the languages that exist (now English and Korean) and aborts on leftover
   markdown.
4. Run `await window.__kiiVerify({draft})`. It rereads the saved draft and fails
   when the image or footnote count differs from the run summary, when an image
   was not uploaded, or when literal markdown or HTML is left in the text or an
   HTML entity (such as `&amp;`) is left in image alt text. Do not publish
   unless `ok` is `true`.
5. Reload the draft and look at it: the first figure, one table image, the
   footnote block and the language footer. The run summary survives the reload in
   `sessionStorage`, so `__kiiVerify` still works after you paste the script again.
6. Run `await window.__kiiPublish({draft})`. It refuses a title that is already in
   the public archive under another post id, refuses `send:true` on a post that
   is already published, publishes, and returns `{slug, url, emailed}`. Open the
   returned URL once and check the first figure and a footnote link.
7. Open any `https://substack.com/` page (same login), paste the script again and
   run `await window.__kiiNote({title, desc, url})` with the post title, the
   frontmatter description and the URL from step 6. It posts the Note with the same
   text `substack_notes.py` builds and returns `noteUrl`. The
   `notes/new?body=` deep link no longer opens a composer.
8. Record the receipt:

   ```bash
   scripts/substack_record_browser_publish.py --slug <slug> \
     --substack-url <url> --draft-id <draftId> --note-url <noteUrl>
   ```

   It checks that the Substack URL answers 200 and writes the entry
   `post_publish_distribution.py` waits for (`--emailed no` for a web-only
   publish, `--no-note "<reason>"` only for an explicit exception,
   `--check --slug <slug>` to read it back).
9. Run `scripts/post_publish_distribution.py --slug <slug> --max-posts 1` for the
   other channels.

Fixing, unpublishing and deleting (same logged-in page, verified 2026-10-22):

- Fix a published post: rerun step 3 on the same draft id (or `PUT /api/v1/drafts/<id>`
  with the new `draft_body`), check it with step 4, then
  `await window.__kiiPublish({draft, send:false})`. Post date, slug, comments and the
  email record stay. The plain URL can serve the old body from cache for a few minutes.
- Unpublish: `POST /api/v1/drafts/<id>/unpublish` returns the post to a draft and the
  URL answers 404. Delete a draft: `DELETE /api/v1/drafts/<id>`.
- Delete a Note: `DELETE https://substack.com/api/v1/comment/<noteId>` from a
  `substack.com` page.
- Unpublishing breaks the link in an email already sent, so prefer fixing the original.

Known limits:

- Text inside table images is small on a phone (a tap zooms). A footnote inside a
  table becomes a superscript number in the image, not a body anchor.
- Gmail clips emails over 102KB; the footnote block at the end is clipped first.

#### Cookie API path (opt-in, plain text only)

Auth facts, observed 2026-10-10 and 2026-10-22:

- The publisher reads an HttpOnly `connect.sid` cookie from
  `state/profiles/gyeokja/legacy-workspace/data/substack_config.json` (outside Git).
  No script can read that cookie from a browser.
- Reads and draft creation work with an old cookie. Publish returns
  `403 reauthentication_required` ("sign out and sign back in") when the session needs a
  fresh sign-in. The April cookie returned it on 2026-10-22 while a fresh browser session
  passed. How long a fresh session keeps passing is unknown: a re-login on 2026-10-10
  allowed one publish, and runs failed again by 10-13.
- `scripts/substack_gate.py` tells the cases apart without side effects: a publish call on
  a draft id that cannot exist returns 404 when the gate passes and 403
  `reauthentication_required` when it does not. `substack_set_cookie.py --check` runs it
  on the stored cookie. Read calls pass in both cases and prove nothing.
- `post_publish_distribution.py --substack-mode api` checks the gate before it creates a
  draft and exits 4 when it fails. Any other failure exits 3. Neither is logged as
  published. With `KII_SUBSTACK_API=1`, `blog_publish_pipeline.py` checks the same gate
  before it creates a draft. Before 2026-10-22 failed runs left orphan drafts (eight daily
  drafts piled up between 10-08 and 10-20).

To refresh the cookie, sign in to Substack in a browser, copy the session cookie
(DevTools -> Application -> Cookies -> substack.com -> `connect.sid` or `substack.sid`),
then run `python3 scripts/substack_set_cookie.py --clipboard`. It writes the cookie only
after the publish gate passes. The HttpOnly cookie cannot be read by an agent, and an
agent must not read it from a browser store.

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
