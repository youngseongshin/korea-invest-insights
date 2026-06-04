# Windows Blog Publishing Runbook

## Source Files

- `docs/blog-publishing-process.md`: canonical publish and post-live distribution flow.
- `scripts/post_publish_distribution.py`: unified post-live distribution for Telegram, Botmadang, Substack, and opt-in Valley.
- `scripts/run_post_publish_distribution.ps1`: Windows runner for the post-live stage.
- `scripts/blog_publish_windows.py`: Windows runner for the OpenClaw blog publish pipeline.
- `../openclaw-workspace/workspace/tools/blog_publish_pipeline.py`: multilingual Hugo post pipeline.
- `../openclaw-workspace/workspace/tools/blog_channel_notify.py`: Telegram channel notifier.
- `../openclaw-workspace/workspace/tools/blog_botmadang_notify.py`: Botmadang notifier.
- `../openclaw-workspace/workspace/tools/substack_publisher.py`: Substack publisher.
- `../openclaw-workspace/workspace/tools/substack_notes.py`: Substack Notes follow-up.

## Windows Environment

The runners set these automatically when launched from this repository:

```powershell
$env:KII_REPO_ROOT = "C:\Users\신영성\Documents\OpenClaw\korea-invest-insights"
$env:OPENCLAW_TOOLS = "C:\Users\신영성\Documents\OpenClaw\openclaw-workspace\workspace\tools"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
```

Optional private configuration paths:

```powershell
$env:OPENCLAW_SUBSTACK_CONFIG = "C:\Users\신영성\Documents\OpenClaw\.secrets\substack_config.json"
$env:OPENCLAW_COMMUNITY_CONFIG = "C:\Users\신영성\Documents\OpenClaw\.secrets\agent_community_config.json"
$env:KII_VALLEY_ENV = "C:\Users\신영성\.config\korea-invest-insights\valley.env"
```

Do not commit these private files.

## Post-Live Distribution

Dry-run for a specific live slug:

```powershell
.\scripts\run_post_publish_distribution.ps1 `
  -Slug "samsung-electro-mechanics-100tn-murata-hyundai-market-cap-2026-05-26" `
  -DryRun `
  -NoRequireLive
```

After GitHub Pages deploy is live:

```powershell
.\scripts\run_post_publish_distribution.ps1 `
  -Slug "<post-slug>"
```

Default channels are `telegram,botmadang,substack`. Valley remains paused unless explicitly requested and `VALLEY_ACCESS_OVERRIDE=true` is set.

## Blog Publish Pipeline

Conservative dry-run with English and Korean source markdown:

```powershell
python .\scripts\blog_publish_windows.py `
  --english-md C:\path\to\index.en.md `
  --korean-md C:\path\to\index.ko.md `
  --skip-translate `
  --dry-run
```

Live publish defaults to writing Hugo files, committing, pushing, and submitting IndexNow. On Windows, the runner skips vault, Substack, Telegram, Botmadang, DM, and Valley unless an `--include-*` flag is provided.

```powershell
python .\scripts\blog_publish_windows.py `
  --english-md C:\path\to\index.en.md `
  --korean-md C:\path\to\index.ko.md `
  --skip-translate `
  --include-substack `
  --include-channel `
  --include-botmadang
```

## Safety Notes

- Run targeted `-Slug` distribution during active publishing. Untargeted backfill scans all historical posts and is slower.
- Valley cookie-backed posting is suspended by policy and should not be resumed without explicit approval.
- Substack and Botmadang require private local config files. Missing config causes those channels to fail or skip; credentials are not read by dry-runs.
- The local Obsidian vault is still a bare git mirror on this PC, so vault sync should remain skipped until the vault checkout issue is fixed.
