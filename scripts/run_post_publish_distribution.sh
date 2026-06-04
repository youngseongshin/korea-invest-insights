#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CONFIG_PATH="${HOME}/.config/korea-invest-insights/valley.env"

mkdir -p "${HOME}/Library/Logs/korea-invest-insights" "${HOME}/.local/share/korea-invest-insights"
cd "${REPO_ROOT}"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

export KII_REPO_ROOT="${REPO_ROOT}"
export KOREA_INVEST_INSIGHTS_ROOT="${REPO_ROOT}"
export PYTHONUTF8="${PYTHONUTF8:-1}"
export PYTHONIOENCODING="${PYTHONIOENCODING:-utf-8}"

exec "${PYTHON_BIN}" "${REPO_ROOT}/scripts/post_publish_distribution.py" \
  --repo-root "${REPO_ROOT}" \
  --config "${CONFIG_PATH}" \
  --lang ko \
  --since-days "${KII_DISTRIBUTION_SINCE_DAYS:-14}" \
  --max-posts "${KII_DISTRIBUTION_MAX_POSTS:-3}" \
  --body-mode "${KII_DISTRIBUTION_BODY_MODE:-auto}" \
  --channels "${KII_DISTRIBUTION_CHANNELS:-telegram,botmadang,substack}" \
  --require-live
