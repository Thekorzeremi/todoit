#!/bin/bash
if [ -f app.pid ]; then
  PID=$(cat app.pid)
  kill $PID
  rm app.pid
  echo "Service arrêté (PID: $PID)"
else
  echo "Pas de PID trouvé"
fi