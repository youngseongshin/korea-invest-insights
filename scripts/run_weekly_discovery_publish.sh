#!/bin/bash
# Weekly discovery → public blog DRAFT generator (draft-first; registry M-20260530-03).
#
# Produces a gate-protected draft:true post from 격자's Saturday 주간 발굴 결산.
# It NEVER auto-publishes or distributes: drafts are skipped by
# post_publish_distribution.py, so no public leak is possible from this runner.
# Go-live (set draft:false → commit/push → distribute) is a separate, human-
# approved stage — see the ticket for the activation steps.
set -euo pipefail

REPO_ROOT="/Users/youngseongshin/korea-invest-insights"
LOG="${HOME}/Library/Logs/korea-invest-insights/weekly_discovery_publish.log"
mkdir -p "$(dirname "$LOG")"
cd "${REPO_ROOT}"

{
  echo ""
  echo "=== [$(TZ=Asia/Seoul date '+%F %T %Z')] weekly_discovery_publish (draft mode) start ==="
  set +e
  /usr/bin/python3 "${REPO_ROOT}/scripts/weekly_discovery_publish.py" --write-draft
  RC=$?
  set -e
  echo "=== [$(TZ=Asia/Seoul date '+%F %T %Z')] weekly_discovery_publish exit=${RC} ==="
  exit "${RC}"
} >> "${LOG}" 2>&1
