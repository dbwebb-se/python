#!/usr/bin/env bash
cd me/kmom03/marvin2 || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run Marvin2"
python3 marvin.py

read -p "Press to view marvin.py" answer
cat marvin.py
