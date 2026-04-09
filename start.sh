#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ ! -f manage.py ]]; then
  echo "Error: manage.py not found in $SCRIPT_DIR"
  exit 1
fi

VENV_DIR="$SCRIPT_DIR/venv"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "No virtual environment found. Creating one at: $VENV_DIR"
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

if ! python -c "import django" >/dev/null 2>&1; then
  echo "Django is not installed in the virtual environment."
  if [[ -f requirements.txt ]]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
  else
    echo "No requirements.txt found. Installing Django..."
    pip install django
  fi
fi

HOST_PORT="${1:-127.0.0.1:8000}"
echo "Starting Django server at http://$HOST_PORT/"
exec python manage.py runserver "$HOST_PORT"
