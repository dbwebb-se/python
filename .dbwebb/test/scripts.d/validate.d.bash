#!/usr/bin/env bash

for opt in $ARGUMENTS; do
    case $opt in
        "--no-validate" )
            skip=true
            ;;
    esac
done;

if [ -z $skip ]; then
    header_text="Validation: \"dbwebb validate $TESTSUITE\":"
    VALIDATE_STATUS="$(dbwebb validate $TESTSUITE)"

else
    header_text="Skipped validate .."
fi



doLog $? "$header_text

${VALIDATE_STATUS}
"