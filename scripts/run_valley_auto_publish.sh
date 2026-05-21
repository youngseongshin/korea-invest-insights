#!/bin/bash
set -euo pipefail

# Valley access is suspended after an abnormal-access warning from Valley.
# Keep the entrypoint as a clean no-op so a loaded legacy LaunchAgent cannot
# accidentally hit Valley or the unified distribution stage.
echo "{\"status\":\"skipped\",\"reason\":\"Valley access suspended after abnormal-access warning\"}"
exit 0
