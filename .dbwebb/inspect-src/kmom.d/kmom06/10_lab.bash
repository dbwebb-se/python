#!/usr/bin/env bash
cd me/kmom06/lab6/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run lab"
python3 answer.py