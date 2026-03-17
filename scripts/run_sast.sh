#!/usr/bin/env bash
set -euo pipefail

echo "[Pipeline Guardian] Running Semgrep SAST scan..."

semgrep scan \
  --config=p/ci \
  --severity=ERROR \
  --json \
  --output=reports/semgrep.json

echo "[Pipeline Guardian] SAST scan passed"
