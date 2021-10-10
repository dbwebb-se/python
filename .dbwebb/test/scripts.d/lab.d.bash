#!/usr/bin/env bash

HEADER="scripts.d/$( basename -- "$0" ) start"
FOOTER="scripts.d/$( basename -- "$0" ) end"

contains_lab() {
    local counter=0

    for i in ${temp_arr[@]}
    do
        if [[ "$i" == "$TESTSUITE" ]]; then
            echo "1"
            return
        fi
    done

    echo "0"
    return
}


printf "$HEADER
" | tee -a "$LOG"



DBWEBB_MAP="$COURSE_REPO_BASE/.dbwebb.map"
lab_array="$(cat $DBWEBB_MAP | awk '/[\/]lab[1-9]/')"
file_to_exec="answer.py"

LAB_VERSION="$(cat $COURSE_REPO_BASE/.dbwebb/lab.version)"
source "$COURSE_REPO_BASE/.dbwebb.course"

for lab in $lab_array; do
    temp_arr=(${lab//\// })
    res="$(contains_lab)"

    if [[ $res == "1" ]]; then
        lab_file="${COURSE_REPO_BASE}/${lab}/${file_to_exec}"

        lab_link="https://lab.dbwebb.se/?course=$DBW_COURSE&lab=$(basename $lab)&version=$LAB_VERSION&acronym=$ACRONYM&doGenerate=Submit"

        printf "
Executing $lab/$file_to_exec ...
" | tee -a "$LOG"

        if [[ ! -f "$lab_file" ]]; then
            printf "Error, lab is not created.
" | tee -a "$LOG"
            status=1
        else
            bash -c "set -o pipefail && cd "$COURSE_REPO_BASE/$lab" &&  ${PYTHON_EXECUTER} -u "${lab_file}"  2>&1  | tee -a "$LOG" "
            status=$?
        fi
    fi
done;

printf "
Link to lab: $lab_link
$FOOTER
$SEPARATOR
" | tee -a "$LOG"


if [[ $status == 0 ]]; then
    exit 0
else
    exit 1
fi
