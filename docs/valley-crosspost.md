# Valley Space Cross-Post Workflow

This repository can prepare a Korea Invest Insights post for Valley Space and,
when credentials are available, publish a teaser post back to Valley.

## Current Integration Boundary

Valley currently uses session-backed web app endpoints under:

- `https://api.valley.town/post/drafts`
- `https://api.valley.town/post/posts`
- `https://api.valley.town/post/categories`

No documented public publishing token was found during inspection. Because of
that, do **not** place a Valley browser session cookie in GitHub Actions. The
GitHub Actions path below is designed for an official Valley token if Valley
provides one.

## Automatic Public Publishing

The GitHub Pages deploy workflow contains an optional `valley-publish` job. It
runs only when all of the following are true:

- the workflow was triggered by a push to `main`
- the run is the first attempt, not a manual rerun
- repository variable `VALLEY_AUTO_PUBLISH` is set to `true`
- repository secret `VALLEY_API_TOKEN` exists
- repository secret `VALLEY_POST_CATEGORY_ID` exists
- the push added one or more Korean post files matching
  `content/post/*/index.ko.md`

Only newly added Korean posts are published. Edits to old posts, theme changes,
workflow changes, and reruns are skipped so the same article is not repeatedly
posted to Valley.

The published Valley article is a teaser, not a full mirror:

- description
- canonical Korea Invest Insights URL
- key summary bullets

That keeps the full article canonical on Korea Invest Insights while still
creating a Valley entry for discovery.

## GitHub Configuration

Set the repository variable:

```text
VALLEY_AUTO_PUBLISH=true
```

Set the repository secrets:

```text
VALLEY_API_TOKEN=...
VALLEY_POST_CATEGORY_ID=...
```

If Valley does not provide an official token, keep GitHub auto-publish disabled
and use the local command below.

## Local Flow

1. Publish the Hugo site as usual.
2. Run a local preview for the latest Korean post:

   ```bash
   scripts/valley_crosspost.py --latest --lang ko
   ```

3. If the preview looks right, create a Valley draft locally:

   ```bash
   VALLEY_COOKIE='...' scripts/valley_crosspost.py --latest --lang ko --mode draft
   ```

4. Review and publish the draft inside Valley.

The script writes a local de-duplication log to:

```text
~/.local/share/korea-invest-insights/valley_crosspost_log.json
```

## Category Discovery

To list Valley categories for the logged-in account:

```bash
VALLEY_COOKIE='...' scripts/valley_crosspost.py --mode categories
```

If you later choose to publish directly through the API, pass the category id:

```bash
VALLEY_COOKIE='...' \
VALLEY_POST_CATEGORY_ID='...' \
scripts/valley_crosspost.py --latest --lang ko --mode publish --confirm-publish
```

Direct publish is intentionally guarded by `--confirm-publish`.

## Content Format

By default, the script sends a teaser rather than the full article:

- description
- canonical Korea Invest Insights URL
- key summary bullets

This avoids creating a full duplicate copy of the article on Valley. To send the
full Markdown text instead:

```bash
scripts/valley_crosspost.py --latest --lang ko --body-mode full
```

## Production Recommendation

For durable automation, prefer one of these two paths:

1. **Official Valley token path**: when Valley provides a publishing token, use
   `VALLEY_API_TOKEN` in the post-deploy `valley-publish` job.
2. **Local Research OS path**: a local scheduled job reads the live feed, creates
   Valley drafts with the local Valley session, and sends a Telegram reminder for
   manual review.

Until Valley has an official token, keep GitHub auto-publish disabled and use a
local publish command if automatic public posting is still required.
