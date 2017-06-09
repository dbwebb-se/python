#!/usr/bin/env bash

# Read pylint error codes to a md-file.

echo "# Pylint error codes" > messages.md

pylint --list-msgs | while read line ;
do
    if [[ $line == :* ]];then
        printf "## "
        echo "$line"|awk '{print $1}'
        echo "---"
        printf "#### "
        echo "$line"|awk '{print $2}'
    else
        echo $line
    fi;
done >> messages.md
