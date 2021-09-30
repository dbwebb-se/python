#!/usr/bin/env bash
#

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. "$BASE_DIR/../../functions.bash"

unset -f doLog

function doLog {
    printf '%s\n' "$2"
}

get_python_command
export COURSE_REPO_BASE="${BASE_DIR}/../../../../"
export PYTHON_EXECUTER="$py"
export EXAMINER_RUNNER="examiner.run_tests"
export TESTSUITE=$1
export ARGUMENTS="--extra"
export -f doLog


execute_with_timeout 10 60 bash .dbwebb/test/scripts.d/examiner.d.bash
