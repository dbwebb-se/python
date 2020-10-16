#!/usr/bin/env bash
cd me/tentamen || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Do manual stuff, if needed (write e/f to exit)?"
bash
