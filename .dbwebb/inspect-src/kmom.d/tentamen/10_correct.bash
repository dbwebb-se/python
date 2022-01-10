#!/usr/bin/env bash
cd me/tentamen/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run correct script"
dbwebb test tentamen --no-validate

# cant upload from inside docker so we run manual validate
cd ../../ && make validate what=me/tentamen

read -p "Press to view code" answer
