#!/bin/bash
export PYTHONPATH="$(dirname "$(realpath "$0")")"
nohup python3 app.py > app.log 2>&1 &
echo $! > app.pid
echo "Service démarré (PID: $(cat app.pid))"