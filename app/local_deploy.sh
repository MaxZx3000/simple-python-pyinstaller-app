#!/usr/bin/env sh

set -x
python -m uvicorn main:app --host 0.0.0.0 --port 3000 &
set +x