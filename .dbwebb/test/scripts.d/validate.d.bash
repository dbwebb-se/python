#!/usr/bin/env bash

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"

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

doLog $? "$HEADER

Validation: \"dbwebb validate $TESTSUITE\":
${VALIDATE_STATUS}

$FOOTER
"

else
doLog 0 "Skipped validate ..

${VALIDATE_STATUS}
"
fi