#!/bin/bash
set -euo pipefail

# Backward-compatible entrypoint for the existing LaunchAgent.
# The legacy Valley-only job now runs the unified post-publish distribution
# stage so Telegram, Botmadang, Substack, and Valley stay in sync.
exec /Users/youngseongshin/korea-invest-insights/scripts/run_post_publish_distribution.sh
