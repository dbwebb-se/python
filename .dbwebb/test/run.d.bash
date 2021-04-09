#!/usr/bin/env bash
#
# Execute all scripts in a subdirectory
#
# Arguments:
#  course_dir           Absolute path to the basedir of the course repo.
#  course               Nickname of the course.
#  acronym              Acronym of the user executing the script.
#  test_suite           Name of the testsuite to execute.
#  <optional args>      Optional arguments
#

# Usage
if (( $# < 3 )); then
    printf "Usage: %s <course_dir> <course> <acronym> <test_suite> <optional args...>\n" \
        "$( basename -- "$0" )"
    exit 1
fi


# Handles optional agruments and if no "suit" is given.
tmp_test_suit="$4"
tmp_arguments="${@:5}"
if [[ -z "$tmp_test_suit" || $tmp_test_suit == -* ]]; then
    tmp_test_suit=$(pwd | awk -F/ '{print $NF}')
    tmp_arguments="${@:4}"
fi


# Prepare configuration
python3 --version >/dev/null 2>&1 && py=python3 || py=pytho
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export EXAMINER_RUNNER="${DIR}/examiner/run_tests.py"
export COURSE_REPO_BASE="$1"
export COURSE="$2"
export ACRONYM="$3"
export TESTSUITE="$tmp_test_suit"
export ARGUMENTS="$tmp_arguments"



TEST_TARGET=$(find "${DIR}/suite.d" -name ${TESTSUITE} -and -type d)
if [ -z ${TEST_TARGET} ]
then
    printf "${COURSE} + ${TESTSUITE} is not a valid target.\n"
    exit 1
fi


# Prepare the logdir and logfile
LOG_DIR="$COURSE_REPO_BASE/.log/test"
[[ -d $LOG_DIR ]] || install -d "$LOG_DIR"
export LOG="$( realpath "$COURSE_REPO_BASE/.log/test/$TESTSUITE" )"


# Runs the test stuits
TEST_STATUS="$(${py} ${EXAMINER_RUNNER} --what=${TEST_TARGET} ${ARGUMENTS} &> "$LOG")"
LOG_OUTPUT="$(cat "$LOG" | tail -n +2)"


print_results () {
    echo
    echo "====================================="
    echo "DBWEBB TEST - ${TESTSUITE}"
    echo "====================================="
    echo "$LOG_OUTPUT"
}


print_results
exit 0