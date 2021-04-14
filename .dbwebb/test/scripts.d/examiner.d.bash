#!/usr/bin/env bash

. ".dbwebb/test/functions.bash"

fail=0

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_TARGET=$(find "${DIR}/../suite.d" -name ${TESTSUITE} -and -type d)
TEST_STATUS="$(${PYTHON_EXECUTER} ${EXAMINER_RUNNER} --what=${TEST_TARGET} ${ARGUMENTS})" || fail=1
OUTPUT="
${TEST_STATUS:1}
"

if [[ "$TEST_STATUS" == *"ERROR section:"* || "$TEST_STATUS" == *"FAIL section:"* ]]; then
    fail=1
fi



doLog $fail "Unittests for $TESTSUITE
${OUTPUT}
"