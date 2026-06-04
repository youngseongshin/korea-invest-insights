# kii-windows-env.ps1
# Dot-source this before running the blog publish / distribution scripts:
#   . .\scripts\kii-windows-env.ps1
#
# It sets every environment variable the OpenClaw publish pipeline and the
# post-publish distribution stage need on this Windows PC. Secrets themselves
# stay in Documents\OpenClaw\.secrets (see that folder's README.md).

$ErrorActionPreference = "Stop"

$RepoRoot     = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$OpenClawRoot = (Resolve-Path (Join-Path $RepoRoot "..")).Path
$Tools        = Join-Path $OpenClawRoot "openclaw-workspace\workspace\tools"
$Secrets      = Join-Path $OpenClawRoot ".secrets"

# Core paths
$env:OPENCLAW_ROOT             = $OpenClawRoot
$env:OPENCLAW_TOOLS            = $Tools
$env:KII_REPO_ROOT            = $RepoRoot
$env:KOREA_INVEST_INSIGHTS_ROOT = $RepoRoot
$env:KII_SCRIPTS             = Join-Path $RepoRoot "scripts"

# UTF-8 everywhere
$env:PYTHONUTF8        = "1"
$env:PYTHONIOENCODING  = "utf-8"

# Private config pointers (used only by live, non-dry-run channels)
$substackCfg  = Join-Path $Secrets "substack_config.json"
$communityCfg = Join-Path $Secrets "agent_community_config.json"
if (Test-Path $substackCfg)  { $env:OPENCLAW_SUBSTACK_CONFIG  = $substackCfg }
if (Test-Path $communityCfg) { $env:OPENCLAW_COMMUNITY_CONFIG = $communityCfg }

# Claude CLI (Botmadang community-summary generation)
$claude = (Get-Command claude -ErrorAction SilentlyContinue)
if ($claude) {
  $env:CLAUDE_BIN = $claude.Source
} else {
  foreach ($p in @("$env:APPDATA\npm\claude.cmd", "$env:LOCALAPPDATA\Programs\claude\claude.exe", "$HOME\.local\bin\claude.exe")) {
    if (Test-Path $p) { $env:CLAUDE_BIN = $p; break }
  }
}

Write-Host "[kii-env] OPENCLAW_TOOLS = $env:OPENCLAW_TOOLS"
Write-Host "[kii-env] KII_REPO_ROOT  = $env:KII_REPO_ROOT"
Write-Host "[kii-env] SUBSTACK_CONFIG = $(if ($env:OPENCLAW_SUBSTACK_CONFIG) { 'set' } else { 'MISSING (substack will skip/fail live)' })"
Write-Host "[kii-env] COMMUNITY_CONFIG = $(if ($env:OPENCLAW_COMMUNITY_CONFIG) { 'set' } else { 'MISSING (botmadang will skip/fail live)' })"
Write-Host "[kii-env] CLAUDE_BIN = $(if ($env:CLAUDE_BIN) { $env:CLAUDE_BIN } else { 'NOT FOUND (botmadang summary needs claude CLI or cache)' })"
