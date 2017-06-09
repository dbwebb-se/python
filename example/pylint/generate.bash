#!/usr/bin/env bash

# Read pylint error codes to md-file.

echo "# Pylint error codes" > messages.md
echo "This file is based on Pylint version 1.6.5" >> messages.md
pylint --list-msgs | while read line ;
do
    if [[ $line == :* ]];then
        printf "## "
        echo "$line"|awk '{print $1}'
        echo "---"
        printf "#### "
        echo "$line"|awk '{$1=""; print $0}'
    else
        echo $line
    fi;
done >> messages.md
