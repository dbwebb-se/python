#!/usr/bin/env bash
cd me/tentamen/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View exam.py"
cat exam.py

read -p "Press to view analyze_functions.py" answer

# cat analyze_functions.py

