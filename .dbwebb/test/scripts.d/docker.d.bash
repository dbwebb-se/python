#!/usr/bin/env bash
#
# Docker script for dbwebb test - Python.
#

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. "$BASE_DIR/../functions.bash"

VERSION="v1.0.0 (2021-05-20)"

# Messages
MSG_FAILED="\033[0;37;41mFAILED\033[0m"
MSG_OK="\033[0;30;42mOK\033[0m"
MSG_DONE="\033[1;37;40mDONE\033[0m"
MSG_WARNING="\033[43mWARNING\033[0m"

# ---------------------------- Functions ------------------

#
# Press enter to continue
#
pressEnterToContinue()
{
    local void

    if [[ ! $YES ]]; then
        printf "\nPress enter to continue..."
        read void
    fi
}



#
# Read input from user supporting a default value for reponse.
#
# @arg1 string the message to display.
# @arg2 string the default value.
#
input()
{
    read -r -p "$1: "
    echo "${REPLY:-$2}"
}



#
# Show helptext to exaplin usage of command
#
show_help()
{
    local txt=(
"Work with docker test."
"Usage: docker-test.bash [command]"
""
"Command:"
"  target           The kmom to test."
"  acronym          The students acronym"

"Options:"
"  --download, -d   Downloads the code from studserver, uses local files as default"
    )
    printf "%s\n" "${txt[@]}"

    exit 0
}


#
# Fail, die and present error message.
#
# @arg1 string the message to display.
# @arg2 string exit status (default 1).
#
die()
{
    local message="$1"
    local status="${2:1}"

    printf '%s' "$MSG_FAILED $message\n" >&2
    exit "$status"
}



#
# Set correct settings of the remote student files, populary called "potatoe".
#
# @arg1 string the acronym.
#
potatoe()
{
    local acronym
    local course="$COURSE"

    if [[ $2 = "false" ]]; then
        course=
    fi

    acronym=$( input "Uppdatera rättigheterna för denna student?" "$1" )
    dbwebb run "sudo /usr/local/sbin/setpre-dbwebb-kurser.bash $acronym $course"
}




#
# Find the course repo file.
#
function findCourseRepoFile
{
    dir="$( pwd )/."
    while [ "$dir" != "/" ]; do
        dir=$( dirname "$dir" )
        found="$( find "$dir" -maxdepth 1 -name $DBW_COURSE_FILE_NAME )"
        if [ "$found" ]; then
            DBW_COURSE_DIR="$( dirname "$found" )"
            break
        fi
    done
}



#
# Get the name of the course as $DBW_COURSE
#
function sourceCourseRepoFile
{
    DBW_COURSE_FILE="$DBW_COURSE_DIR/$DBW_COURSE_FILE_NAME"
    if [ -f "$DBW_COURSE_FILE" ]; then
        source "$DBW_COURSE_FILE"
    fi
}



# ---------------------------- Bootstrap ------------------
# What is the directory of the current course repo, find recursivly up the tree
DBW_COURSE_FILE_NAME=".dbwebb.course"
findCourseRepoFile
[[ $DBW_COURSE_DIR ]] || die "You must run this command within a valid course repo."
DIR="$DBW_COURSE_DIR"

# Get the name of the course as $DBW_COURSE
sourceCourseRepoFile
[[ $DBW_COURSE ]] || die "Your course repo does not seem to have a valid or correct '$DBW_COURSE_FILE_NAME'."
COURSE="$DBW_COURSE"


# Save INSPECT_PID to be able to kill it
DOCKER_TEST_PID=


# Where to store the logfiles
DEFAULT_LOG_BASE_DIR="$DIR/.log/test"
LOG_BASE_DIR="$DEFAULT_LOG_BASE_DIR/docker"
install -d -m 0777 "$LOG_BASE_DIR"

LOGFILE="$LOG_BASE_DIR/main.ansi"
LOGFILE_TEST="$LOG_BASE_DIR/test-results.ansi"
LOGFILE_TEST_EXTRA="$LOG_BASE_DIR/test-extra.ansi"
LOGFILE_ERROR="$LOG_BASE_DIR/errors.ansi"



# OS specific default settings
OS_TERMINAL=""

if [[ "$OSTYPE" == "linux-gnu" ]]; then   # Linux, use defaults
    OS_TERMINAL="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then   # Mac OSX
    OS_TERMINAL="macOS"
elif [[ "$OSTYPE" == "cygwin" ]]; then    # Cygwin
    OS_TERMINAL="cygwin"
fi



#
# Write a header with descriptive text.
#
header()
{
    printf "\n======= %-25s =======\n" "$1"

    if [[ $2 ]]; then
        printf "%s\n" "$2"
    fi
}



#
# Echo feedback text  to log and add to clipboard
#
initLogfile()
{
    local acronym="$1"
    local what="$2"

    header "TESTING ASSIGNMENT" | tee "$LOGFILE"

    printf "%s\n%s %s %s\n%s\ndbwebb test %s\n" "$( date )" "$COURSE" "$1" "$2" "$3" "$VERSION" | tee -a "$LOGFILE"
}



#
# Download student files and do potatoe if needed
#
downloadPotato()
{
    local acronym="$1"
    header "Download (and potato)" "Doing a silent download, potatoe if needed." | tee -a "$LOGFILE"

    if ! dbwebb --force --yes download me $acronym > /dev/null; then
        printf "\n\033[32;01m---> Doing a Potato\033[0m\n\033[0;30;43mACTION NEEDED...\033[0m\n"
        potatoe $acronym
        if ! dbwebb --force --yes --silent download me $acronym; then
            printf "\n\033[0;30;41mFAILED!\033[0m Doing a full potatoe, as a last resort...\n"
            potatoe $acronym "false"
            if ! dbwebb --force --yes --silent download me $acronym; then
                printf "\n\033[0;30;41mFAILED!\033[0m Doing a full potatoe, as a last resort...\n"
                exit 1
            fi
        fi
    fi
}



#
# Handles all optional arguments
#
handle_options()
{
    for opt in "$@"; do
        case $opt in
            "--download" | "-d" )
                initDescription="download, docker"
                if ! downloadPotato "$acronym"; then
                    pressEnterToContinue
                    continue
                fi
            ;;

            "--help" | "-h") show_help;;
        esac
    done
}




prepare_and_run_examiner_extra()
{
    DOCKER_COMMAND="docker-compose run --rm cli"
    TEST_COMMAND="bash .dbwebb/test/scripts.d/helpers/docker-correct-extra.d.bash ${1}"
    if [ $OS_TERMINAL == "linux" ]; then
        setsid $DOCKER_COMMAND $TEST_COMMAND > "$LOGFILE_TEST_EXTRA"
        DOCKER_TEST_PID="$!"
    else
        $DOCKER_COMMAND $TEST_COMMAND > "$LOGFILE_TEST_EXTRA"
        DOCKER_TEST_PID="$!"
    fi
}


killDockerTestPid()
{
    if [[ ! -z $DOCKER_TEST_PID ]]; then
        kill -9 $DOCKER_TEST_PID > /dev/null 2>&1
        DOCKER_TEST_PID=
    fi
}

#
# Tests the assignment inside docker.
# Runs the test command with no validation as it does not work inside docker.
# - Using `make validate` separately instead.
#
doDockerDbwebbTestAndValidate()
{

    DOCKER_COMMAND="docker-compose run --rm cli"
    TEST_COMMAND="dbwebb test $1 $2 --docker"
    shift 2

    if [ $OS_TERMINAL == "linux" ]; then
        setsid $DOCKER_COMMAND $TEST_COMMAND $* > "$LOGFILE_TEST" 2> "$LOGFILE_ERROR"
        DOCKER_TEST_PID="$!"
    else
        $DOCKER_COMMAND $TEST_COMMAND $* > "$LOGFILE_TEST" 2> "$LOGFILE_ERROR"
        DOCKER_TEST_PID="$!"
    fi
}




#
# Main function
#
main()
{
    #exit 0
    local acronym="$2"
    local kmom="$1"
    initDescription="local, docker"

    handle_options "$@"
    initLogfile "$acronym" "$kmom" "$initDescription"

    # if [[ ! -z $DOCKER_TEST_PID ]]; then
    #     kill -9 $DOCKER_TEST_PID > /dev/null 2>&1
    #     DOCKER_TEST_PID=
    # fi

    killDockerTestPid
    doDockerDbwebbTestAndValidate $*

    killDockerTestPid
    prepare_and_run_examiner_extra $1


    OK_OR_FAIL_MESSAGES=$(grep -A 999 'Test summary' "$LOGFILE_TEST")
    result_arr=(${OK_OR_FAIL_MESSAGES//$'\n'/ })

    for i in "${!result_arr[@]}"; do
        CURRENT_INDEX="${result_arr[$i]}"
        case "$CURRENT_INDEX" in
            *"FAILED"* )
                STATUS="FAILED" ;;
        esac
    done

    echo "

============================================================
Results for extra assignments:
"| cat  - "$LOGFILE_TEST_EXTRA" > /tmp/out && mv /tmp/out "$LOGFILE_TEST_EXTRA"
printf '%s\n' "============================================================" >> $LOGFILE_TEST_EXTRA

    #no_colors=$(cat "$LOGFILE_TEST" "$LOGFILE_TEST_EXTRA" "$LOGFILE_ERROR" | sed 's/\x1B\[[0-9;]\{1,\}[A-Za-z]//g')
    colors=$(cat "$LOGFILE_TEST" "$LOGFILE_TEST_EXTRA" "$LOGFILE_ERROR")
    printf '\n%s\n' "$colors" | tee -a "$LOGFILE"

    [[ $STATUS == "FAILED" ]] && exit 1
    exit 0
}

main $*
