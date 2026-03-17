#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-fs}"

if [[ "$MODE" == "image" ]]; then
  echo "[Pipeline Guardian] Scanning container image..."
  trivy image \
    --severity HIGH,CRITICAL \
    --exit-code 1 \
    --format json \
    --output reports/trivy-image.json \
    pipeline-guardian:latest
else
  echo "[Pipeline Guardian] Scanning dependencies..."
  trivy fs \
    --severity HIGH,CRITICAL \
    --exit-code 1 \
    --format json \
    --output reports/trivy-deps.json \
    .
fi
