# Korea Invest Insights — Windows Quick Start (this PC)

One-page operator guide for running the **already-defined** blog publish +
post-process pipeline on this Windows PC. Full detail lives in
[`windows-blog-publishing.md`](windows-blog-publishing.md) and
[`blog-publishing-process.md`](blog-publishing-process.md).

## Layout on this PC
- Blog repo:    `C:\Users\신영성\Documents\OpenClaw\korea-invest-insights`
- OpenClaw tools: `...\OpenClaw\openclaw-workspace\workspace\tools`
- Secrets:      `...\OpenClaw\.secrets`  (see its `README.md`)
- Hugo:         `C:\Users\신영성\AppData\Local\Programs\Hugo\bin\hugo` (installed)
- Python:       3.13 (all pipeline modules import OK)
- Git push:     authenticated via Git Credential Manager (no token needed)

## Step 0 — load the environment (each new PowerShell)
```powershell
cd C:\Users\신영성\Documents\OpenClaw\korea-invest-insights
. .\scripts\kii-windows-env.ps1
```
This prints whether Substack/Botmadang config and the Claude CLI are present.

## Step 1 — write & publish a post (Hugo + commit + push + IndexNow)
```powershell
# Dry-run first (no writes):
python .\scripts\blog_publish_windows.py --english-md <path>\index.en.md --korean-md <path>\index.ko.md --dry-run

# Live: writes 7-language Hugo files, commits, pushes, submits IndexNow.
python .\scripts\blog_publish_windows.py --english-md <path>\index.en.md --korean-md <path>\index.ko.md
```
Pushing to `main` triggers the GitHub Pages deploy workflow automatically.
On Windows, channels (Substack/Telegram/Botmadang/Valley) are **skipped** unless
you add `--include-substack --include-channel --include-botmadang`. Prefer to run
distribution as a separate post-live step (Step 3) so you can confirm the URL is live.

## Step 2 — wait for the live URL
After the push, wait for the GitHub Pages deploy to finish, then confirm
`https://koreainvestinsights.com/ko/post/<slug>/` returns 200.

## Step 3 — post-publish distribution (Telegram + Botmadang + Substack)

Distribution now requires all seven language files in the post bundle:
`index.ko.md`, `index.en.md`, `index.es.md`, `index.vi.md`, `index.fr.md`,
`index.ja.md`, and `index.zh.md`. If any are missing, translate first and then
retry this step.

```powershell
# Dry-run for a slug (safe, no sends, no creds read):
.\scripts\run_post_publish_distribution.ps1 -Slug "<slug>" -DryRun -NoRequireLive

# Live, after the URL is up:
.\scripts\run_post_publish_distribution.ps1 -Slug "<slug>"
```
Default channels: `telegram,botmadang,substack`. Valley is paused by policy.

## Status of channels on this PC
- **Blog publish + GitHub Pages + IndexNow** — ready, no extra secrets.
- **Telegram** (`@korea_invest_insights`) — ready (bot token embedded in tool source).
- **Substack** — needs `.secrets\substack_config.json` (subdomain + connect.sid cookie).
- **Botmadang** — needs `.secrets\agent_community_config.json` (api_key) **and** the
  Claude CLI on PATH or `CLAUDE_BIN` set (used to generate the community summary),
  or a pre-existing summary cache.
- **Valley** — suspended since 2026-05-21; do not re-enable without explicit approval.

## Verified on 2026-06-04
- pipeline + channel module imports: OK
- `blog_publish_windows.py --dry-run`: OK (0 errors)
- `run_post_publish_distribution.ps1 -DryRun`: OK (telegram/botmadang/substack all `would_*`)
- `hugo --minify`: builds the full site
