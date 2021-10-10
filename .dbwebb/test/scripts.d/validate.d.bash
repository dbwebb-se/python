#!/usr/bin/env bash

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"



printf "$HEADER

Validation: \"dbwebb validate $TESTSUITE\":
" | tee -a "$LOG"



for opt in $ARGUMENTS; do
    case $opt in
        "--no-validate" )
            skip=true
            ;;
        "--docker" )
            make_validate=true
    esac
done;



if [[ "$skip" ]]; then
      printf "Skipped validate ..
" | tee -a "$LOG"
else
  if [[ "$make_validate" ]]; then
      make validate what=$TESTSUITE
      status=$?
  else
      dbwebb validate $TESTSUITE
      status=$?
  fi
fi

printf "
$FOOTER
$SEPARATOR
" | tee -a "$LOG"


exit $status
