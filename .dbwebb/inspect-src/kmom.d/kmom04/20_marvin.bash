#!/usr/bin/env bash
cd me/kmom04/marvin3/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run Marvin3"
python3 main.py

read -p "Press to view main.py" answer
cat main.py

read -p "Press to view marvin.py" answer
cat marvin.py
