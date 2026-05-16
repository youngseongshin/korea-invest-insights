#!/bin/bash
set -euo pipefail

REPO_ROOT="/Users/youngseongshin/korea-invest-insights"
CONFIG_PATH="${HOME}/.config/korea-invest-insights/valley.env"

mkdir -p "${HOME}/Library/Logs/korea-invest-insights"
cd "${REPO_ROOT}"

exec /usr/bin/python3 "${REPO_ROOT}/scripts/post_publish_distribution.py" \
  --repo-root "${REPO_ROOT}" \
  --config "${CONFIG_PATH}" \
  --channels valley,telegram,botmadang,substack \
  --lang ko \
  --since-days 14 \
  --max-posts 3 \
  --body-mode auto \
  --require-live
