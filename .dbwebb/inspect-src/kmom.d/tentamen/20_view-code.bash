#!/usr/bin/env bash
cd me/tentamen/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "View exam.py"
cat exam.py

read -p "Press to view savingscentral.py" answer

cat savingscentral.py

read -p "Press to view stockbank.py" answer

cat stockbank.py


# cat analyze_functions.py

