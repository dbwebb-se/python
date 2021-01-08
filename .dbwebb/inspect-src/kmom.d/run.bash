#!/usr/bin/env bash
#
# Execute all scripts in a subdirectory
#

# Usage
if (( $# != 3 )); then
    printf "Usage: run.bash <kmom_number> <acronym> <log_docker>\n"
    exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export KMOM="$1"
export COURSE_REPO="$PWD"
export ACRONYM="$2"
export LOG="$( realpath $DIR/../../../$3 )"
(( $? == 0 )) || exit 2

if [[ ! -d "$DIR/$KMOM" ]]; then
    printf "No such directory '%s'\n" "$DIR/$KMOM"
    exit 1
fi

MSG_OK="\033[0;30;42mOK\033[0m"
MSG_DONE="\033[1;37;40mDONE\033[0m"
export MSG_WARNING="\033[43mWARNING\033[0m"
export MSG_FAILED="\033[0;37;41mFAILED\033[0m"



#
# Print a header
#
function header {
    printf "\033[32;01m>>> -------------- %-20s -------------------------\033[0m\n" "$1"
}

#
# Print information text
#
function text {
    printf "$@"
}

#
# Log to summary
#
function doLog {
    if (( $1 )); then
        echo "[-] $2" >> "$LOG"
    else
        echo "[+] $2" >> "$LOG"
    fi

    exit $1
}

export -f doLog

printf "\n"
header "Start"
printf "Running scripts in '%s'.\n" "$DIR/$KMOM"

summary=
if ! compgen -G "$DIR/$KMOM/??*_*.bash" > /dev/null; then
    printf "\n$MSG_DONE No script to execute.\n"
    exit 0
fi

for file in $DIR/$KMOM/??*_*.bash; do
    output=
    target=$( basename "$file" )
    echo && header "$target"

    bash "$file"
    if (( $? )); then
        output="$MSG_FAILED $target\n"
    else
        output="$MSG_OK $target\n"
    fi
    printf "$output"
    summary="$summary$output"
done

printf "\n$MSG_DONE All scripts were executed.\n"
header "Summary"
printf "$summary"
