#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://localhost:8080}"

echo "Waiting for app at $URL ..."
for i in {1..30}; do
  if curl -fs "$URL/api/health" > /dev/null; then
    echo "Health check passed."
    break
  fi
  if [ "$i" -eq 30 ]; then
    echo "App did not become healthy in time." >&2
    exit 1
  fi
  sleep 3
done

echo "Testing create + list (exercises the MySQL path) ..."
curl -fs -X POST "$URL/api/expenses" \
  -H "Content-Type: application/json" \
  -d '{"title":"smoke","amount":1.0,"category":"Test"}' > /dev/null

curl -fs "$URL/api/expenses" | grep -q "smoke"
echo "Smoke test passed."
