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

## Local Manual Flow

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

## Local Auto-Publish Flow

The preferred production path is a local LaunchAgent. It checks the local Hugo
content every 10 minutes, verifies that the canonical Korean URL is live on
`koreainvestinsights.com`, and then publishes only posts that do not exist in
the local de-duplication log.

Create a local secret file. This file is intentionally outside the repository:

```bash
mkdir -p ~/.config/korea-invest-insights
chmod 700 ~/.config/korea-invest-insights
cat > ~/.config/korea-invest-insights/valley.env <<'EOF'
VALLEY_AUTO_PUBLISH=true
VALLEY_COOKIE=...
VALLEY_POST_CATEGORY_ID=...
EOF
chmod 600 ~/.config/korea-invest-insights/valley.env
```

`VALLEY_COOKIE` should be the authenticated Valley browser cookie string. Do not
commit it. To discover the category id:

```bash
VALLEY_COOKIE='...' scripts/valley_crosspost.py --mode categories
```

Run a dry-run before enabling launchd:

```bash
scripts/valley_auto_publish.py --dry-run
```

Install the LaunchAgent:

```bash
mkdir -p ~/Library/LaunchAgents ~/Library/Logs/korea-invest-insights
cp ops/launchd/com.koreainvestinsights.valley-auto-publish.plist \
  ~/Library/LaunchAgents/
plutil -lint ~/Library/LaunchAgents/com.koreainvestinsights.valley-auto-publish.plist
launchctl bootstrap "gui/$(id -u)" \
  ~/Library/LaunchAgents/com.koreainvestinsights.valley-auto-publish.plist
launchctl enable "gui/$(id -u)/com.koreainvestinsights.valley-auto-publish"
launchctl kickstart -k "gui/$(id -u)/com.koreainvestinsights.valley-auto-publish"
```

Logs:

```text
~/Library/Logs/korea-invest-insights/valley_auto_publish.log
~/Library/Logs/korea-invest-insights/valley_auto_publish.error.log
```

Disable it:

```bash
launchctl bootout "gui/$(id -u)" \
  ~/Library/LaunchAgents/com.koreainvestinsights.valley-auto-publish.plist
rm ~/Library/LaunchAgents/com.koreainvestinsights.valley-auto-publish.plist
```

Safety rules:

- missing `valley.env` means the job skips cleanly
- `VALLEY_AUTO_PUBLISH` must be `true`
- `VALLEY_POST_CATEGORY_ID` is required for public publishing
- on first activation, the job writes a local watermark and does not backfill
  old posts
- only Korean posts after that watermark and from the last 14 days are
  considered
- the canonical blog URL must return HTTP 2xx/3xx before publishing
- the same canonical URL is never published twice unless the log is manually
  edited

Watermark state is stored at:

```text
~/.local/share/korea-invest-insights/valley_auto_publish_state.json
```

If you explicitly want to backfill recent posts, run the script manually with
`--allow-backfill` or set `VALLEY_BACKFILL=true` for one run only.

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
2. **Local Research OS path**: use
   `com.koreainvestinsights.valley-auto-publish` to publish Korean teaser posts
   from the local Mac after the blog URL is live.

Until Valley has an official token, keep GitHub auto-publish disabled unless an
official `VALLEY_API_TOKEN` is configured. Local automation is the safer default
for cookie-backed publishing.
