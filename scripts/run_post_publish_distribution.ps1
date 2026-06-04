param(
  [Alias("?", "h")]
  [switch]$Help,
  [string]$Slug = "",
  [string]$Channels = $env:KII_DISTRIBUTION_CHANNELS,
  [int]$SinceDays = $(if ($env:KII_DISTRIBUTION_SINCE_DAYS) { [int]$env:KII_DISTRIBUTION_SINCE_DAYS } else { 14 }),
  [int]$MaxPosts = $(if ($env:KII_DISTRIBUTION_MAX_POSTS) { [int]$env:KII_DISTRIBUTION_MAX_POSTS } else { 3 }),
  [string]$BodyMode = $(if ($env:KII_DISTRIBUTION_BODY_MODE) { $env:KII_DISTRIBUTION_BODY_MODE } else { "auto" }),
  [switch]$DryRun,
  [switch]$NoRequireLive,
  [switch]$AllowBackfill
)

$ErrorActionPreference = "Stop"

if ($Help) {
  @"
Usage:
  .\scripts\run_post_publish_distribution.ps1 -Slug <post-slug> [-DryRun] [-NoRequireLive]

Options:
  -Slug <post-slug>       Target one post. Recommended for active publishing.
  -Channels <list>        Default: telegram,botmadang,substack.
  -DryRun                 Preview channel actions without sending.
  -NoRequireLive          Skip live URL check for local testing.
  -AllowBackfill          Permit non-targeted historical backfill.
"@ | Write-Output
  exit 0
}

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$OpenClawRoot = (Resolve-Path (Join-Path $RepoRoot "..")).Path
$WorkspaceTools = Join-Path $OpenClawRoot "openclaw-workspace\workspace\tools"
$ConfigPath = Join-Path $HOME ".config\korea-invest-insights\valley.env"

if (-not $Channels) {
  $Channels = "telegram,botmadang,substack"
}

if (-not $env:OPENCLAW_TOOLS -and (Test-Path $WorkspaceTools)) {
  $env:OPENCLAW_TOOLS = $WorkspaceTools
}
$env:KII_REPO_ROOT = $RepoRoot
$env:KOREA_INVEST_INSIGHTS_ROOT = $RepoRoot
$env:KII_SCRIPTS = Join-Path $RepoRoot "scripts"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$argsList = @(
  (Join-Path $RepoRoot "scripts\post_publish_distribution.py"),
  "--repo-root", $RepoRoot,
  "--config", $ConfigPath,
  "--lang", "ko",
  "--since-days", "$SinceDays",
  "--max-posts", "$MaxPosts",
  "--body-mode", $BodyMode,
  "--channels", $Channels
)

if ($Slug) {
  $argsList += @("--slug", $Slug)
}
if ($DryRun) {
  $argsList += "--dry-run"
}
if ($NoRequireLive) {
  $argsList += "--no-require-live"
} else {
  $argsList += "--require-live"
}
if ($AllowBackfill) {
  $argsList += "--allow-backfill"
}

python @argsList
exit $LASTEXITCODE
