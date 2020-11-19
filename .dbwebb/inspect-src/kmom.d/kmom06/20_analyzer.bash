#!/usr/bin/env bash
cd me/kmom06/analyzer || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run correct"
bash .dbwebb/correct.bash

read -p "Press to view main.py" answer
cat main.py

read -p "Press to view analyzer.py" answer
cat analyzer.py

read -p "Press to view menu.py" answer
cat menu.py

read -p "Press to view test_exam.py" answer
cat .dbwebb/test_exam.py