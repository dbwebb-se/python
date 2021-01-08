#!/usr/bin/env bash
cd me/kmom05/marvin4/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run Marvin3"
python3 main.py

read -p "Press to view main.py" answer
cat main.py

read -p "Press to view emission_functions.py" answer
cat emission_functions.py
