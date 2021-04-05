#!/usr/bin/env bash

# For the `dbwebb test` kommand - Dbwebb-cli version v2.8.4

# Setting up
python3 --version >/dev/null 2>&1 && py=python3 || py=python

# Setting a base path
SCRIPT_PATH=`realpath $0`
DBWEBB_TEST_DIR=`dirname $SCRIPT_PATH`
LOG_PATH="${DBWEBB_TEST_DIR}/.test-log"

# What kmom / assignment to test
CURRENT_DIR=$(pwd | awk -F/ '{print $NF}')
WHAT=${4:-$CURRENT_DIR}
ARGUMENTS="${@:5}"

if [[ $WHAT == -* ]]
then
    ARGUMENTS="${@:4}"
    WHAT=$CURRENT_DIR
fi

PYTHON_TESTS_PATH=$(find ${DBWEBB_TEST_DIR} -name ${WHAT} -and -type d)

if [ -z ${PYTHON_TESTS_PATH} ]
then
    echo "${WHAT} is not a valid test directory"
    exit 1
fi

test_status="$(${py} ${DBWEBB_TEST_DIR}/examiner/run_tests.py --what=${PYTHON_TESTS_PATH} ${ARGUMENTS} &> "$LOG_PATH")"

# Picks a subpart of log file
NOT_FIRSTS="$(cat "$LOG_PATH" | tail -n +2)" # start on line 2

# Output log file
output_log () {
    echo
    echo "====================================="
    echo "DBWEBB TEST - ${WHAT}"
    echo "====================================="
    echo "$NOT_FIRSTS"
}



# Clean, removes files
clean_up () {
    rm "$LOG_PATH"
}



# Outputs log file from Python test script
output_log


# Clean up
clean_up
exit 0
