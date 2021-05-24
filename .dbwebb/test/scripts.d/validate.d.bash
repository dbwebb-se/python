#!/usr/bin/env bash

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"


write()
{
  doLog $1 "$HEADER

$2

$FOOTER
"
}

for opt in $ARGUMENTS; do
    case $opt in
        "--no-validate" )
            skip=true
            ;;
        "--docker" )
            make_validate=true
    esac
done;

if [ $make_validate ]
then
    header_text="Validation: \"dbwebb validate $TESTSUITE\" DOCKER:":
    VALIDATE_STATUS="$(make validate what=${TESTSUITE})"
    write "$?" "$header_text
$VALIDATE_STATUS"
elif [ -z $skip ]
then
    header_text="Validation: \"dbwebb validate $TESTSUITE\":"
    VALIDATE_STATUS="$(dbwebb validate $TESTSUITE)"

write "$?" "$header_text
$VALIDATE_STATUS"

else
  header_text="Skipped validate .."

  write "$?" "$header_text
$VALIDATE_STATUS"
fi