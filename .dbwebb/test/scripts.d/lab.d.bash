#!/usr/bin/env bash

fail=0

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


DBWEBB_MAP="$COURSE_REPO_BASE/.dbwebb.map"
lab_array="$(cat $DBWEBB_MAP | awk '/[\/]lab[0-9]/')"

exec_file="answer.py"

for lab in $lab_array; do
    temp_arr=(${lab//\// })
    res="$(contains_lab)"

    if [[ $res == "1" ]]; then
        output+="
Executing $lab/$exec_file ...
"
        cd $COURSE_REPO_BASE/$lab
        output+="$(${PYTHON_EXECUTER} ${COURSE_REPO_BASE}/${lab}/${exec_file})
" || fail=1
    fi
done;


if [[ "$output" == *"Grade: Thou Did Not Pass."* ]]; then
    fail=1
fi

doLog $fail "Lab results:
$output
"