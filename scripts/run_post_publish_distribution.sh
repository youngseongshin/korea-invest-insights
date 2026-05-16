#!/bin/bash
set -euo pipefail

REPO_ROOT="/Users/youngseongshin/korea-invest-insights"
CONFIG_PATH="${HOME}/.config/korea-invest-insights/valley.env"

mkdir -p "${HOME}/Library/Logs/korea-invest-insights"
cd "${REPO_ROOT}"

exec /usr/bin/python3 "${REPO_ROOT}/scripts/post_publish_distribution.py" \
  --repo-root "${REPO_ROOT}" \
  --config "${CONFIG_PATH}" \
  --lang ko \
  --since-days "${KII_DISTRIBUTION_SINCE_DAYS:-14}" \
  --max-posts "${KII_DISTRIBUTION_MAX_POSTS:-3}" \
  --body-mode "${KII_DISTRIBUTION_BODY_MODE:-auto}" \
  --channels "${KII_DISTRIBUTION_CHANNELS:-telegram,botmadang,substack,valley}" \
  --require-live
