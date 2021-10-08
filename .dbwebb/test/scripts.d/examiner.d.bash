#!/usr/bin/env bash
. "$COURSE_REPO_BASE/.dbwebb/test/functions.bash"

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"


printf "$HEADER

Unittests for $TESTSUITE:
$SEPARATOR

" | tee -a "$LOG"



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEST_TARGET=$(find "${DIR}/../suite.d" -name "${TESTSUITE}" -and -type d)

bash -c "set -o pipefail && cd "${DIR}/.." && ${PYTHON_EXECUTER} -m ${EXAMINER_RUNNER} --what="${TEST_TARGET}" ${ARGUMENTS} 2>&1 | tee -a "$LOG" "
status=$?

printf "
$FOOTER
$SEPARATOR
" | tee -a "$LOG"

exit $status
