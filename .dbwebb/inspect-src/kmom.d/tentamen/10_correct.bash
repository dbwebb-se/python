#!/usr/bin/env bash
cd me/tentamen/.dbwebb || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run correct script"
bash correct.bash
