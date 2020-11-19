#!/usr/bin/env bash
cd me/tentamen/.dbwebb || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run correct script"
bash correct.bash

# Till nästa gång, lägg till hash jämförelse här istället
read -p "Press to view test.exam.py. Only check that is wasnt changed..." answer

cat test_exam.py
