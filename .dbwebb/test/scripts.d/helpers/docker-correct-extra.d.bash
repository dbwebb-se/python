#!/usr/bin/env bash
#

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. "$BASE_DIR/../../functions.bash"


get_python_command
export COURSE_REPO_BASE="${BASE_DIR}/../../../../"
export PYTHON_EXECUTER="$py"
export EXAMINER_RUNNER="examiner.run_tests"
export TESTSUITE=$1
export ARGUMENTS="--extra"
export LOG="$COURSE_REPO_BASE/.log/test/docker/test-extra.ansi"


execute_with_timeout 7 60 bash .dbwebb/test/scripts.d/examiner.d.bash
