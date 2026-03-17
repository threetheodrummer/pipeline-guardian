#!/usr/bin/env bash
set -euo pipefail

echo "[Pipeline Guardian] Running OWASP ZAP baseline scan..."

docker run --rm \
  --network host \
  -v "$(pwd)/reports:/zap/wrk" \
  owasp/zap2docker-stable zap-baseline.py \
  -t http://localhost:8080 \
  -r zap-report.html \
  -J zap-report.json \
  -x zap-report.xml

echo "[Pipeline Guardian] ZAP scan completed"
