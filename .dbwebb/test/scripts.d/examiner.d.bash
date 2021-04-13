#!/usr/bin/env bash

fail=0

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
TEST_TARGET=$(find "${DIR}/../suite.d" -name ${TESTSUITE} -and -type d)
if [ -z ${TEST_TARGET} ]
then
    printf "${COURSE} + ${TESTSUITE} is not a valid target.\n"
    exit 1
fi


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