#!/usr/bin/env bash
set -euo pipefail

echo "Run the program!"

# Activate venv if exists
if [ -d ".venv" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate
fi

python -m pip install -r requirements.txt
python src/main.py
