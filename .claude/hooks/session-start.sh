#!/bin/bash
# Ensures document tooling for Form B work exists in fresh cloud containers. Idempotent, quiet.
set -u
missing=()
for m in docx openpyxl matplotlib; do python3 -c "import $m" 2>/dev/null || missing+=("$m"); done
if [ ${#missing[@]} -gt 0 ]; then
  pkgs=("${missing[@]/docx/python-docx}")
  pip install -q "${pkgs[@]}" >/dev/null 2>&1 || true
fi
for b in pandoc soffice pdftoppm; do command -v "$b" >/dev/null 2>&1 || echo "session-start: $b not found" >&2; done
exit 0
