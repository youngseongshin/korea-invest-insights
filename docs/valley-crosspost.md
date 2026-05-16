# Valley Space Cross-Post Workflow

This repository can prepare a Korea Invest Insights post for Valley Space and,
when local credentials are available, create a Valley draft.

## Current Integration Boundary

Valley currently uses session-backed web app endpoints under:

- `https://api.valley.town/post/drafts`
- `https://api.valley.town/post/posts`
- `https://api.valley.town/post/categories`

No documented public publishing token was found during inspection. Because of
that, do **not** place a Valley browser session cookie in GitHub Actions. Use the
workflow locally until Valley provides an official API token.

## Recommended Flow

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
   `VALLEY_API_TOKEN` in a post-deploy job.
2. **Local Research OS path**: a local scheduled job reads the live feed, creates
   Valley drafts with the local Valley session, and sends a Telegram reminder for
   manual review.

Until Valley has an official token, the local draft-first flow is the safer
default.
