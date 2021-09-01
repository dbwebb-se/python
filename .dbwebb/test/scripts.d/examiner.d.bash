#!/usr/bin/env bash
. "$COURSE_REPO_BASE/.dbwebb/test/functions.bash"

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"

fail=0

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_TARGET=$(find "${DIR}/../suite.d" -name "${TESTSUITE}" -and -type d)
TEST_STATUS="$(cd "${DIR}/.." && ${PYTHON_EXECUTER} -m ${EXAMINER_RUNNER} --what="${TEST_TARGET}" ${ARGUMENTS})" || fail=1
OUTPUT="${TEST_STATUS}
"

if [[ "$TEST_STATUS" == *"ERROR section:"* || "$TEST_STATUS" == *"FAIL section:"* ]]; then
    fail=1
fi



doLog $fail "$HEADER

Unittests for $TESTSUITE:
${OUTPUT}
$FOOTER
"
