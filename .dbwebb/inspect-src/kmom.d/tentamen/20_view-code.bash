#!/usr/bin/env bash
cd me/tentamen/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View exam.py"
cat exam.py
