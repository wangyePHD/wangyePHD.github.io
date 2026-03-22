#!/usr/bin/env bash
# ./journal-publish.sh [提交说明]
set -e
cd "$(dirname "$0")"

test -d .venv || python3 -m venv .venv
.venv/bin/pip install -q -r journal/requirements.txt
.venv/bin/python journal/build_from_md.py

git add -A
if git diff --cached --quiet; then exit 0; fi
git commit -m "${1:-chore: update journal}"
git push
