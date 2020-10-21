# Correct.bash script used for autocorrecting programming exams.


check_python_version () {
    command=$1
    VERSION=$(${command} -V 2>&1 | cut -d\  -f 2) # python 2 prints version to stderr
    VERSION=(${VERSION//./ }) # make an version parts array 
    if [[ ${VERSION[0]} -lt 3 ]] || [[ ${VERSION[0]} -eq 3 && ${VERSION[1]} -lt 5 ]] ; then
        return 1
    fi
    return 0
}

get_python_command () {
    for cmd in python3 python py py3
    do
        check_python_version $cmd
        if [[ $? -eq 0 ]] ; then
            py=$cmd
            return 0
        fi
    done
    echo "Can't find valid Python command. Python 3.5+ needed!"
    echo "Have tried with python3, python, py and py3"
    exit 1
}


# Find working python command, sets to variable "py"
get_python_command



# Verbose check
VERBOSE=true

# Text file use by students
COPY_FILE="manifesto.txt"
OUTPUT_FILE="output.txt"



# get path to .dbwebb folder
DBWEBB_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
PROJ_PATH="$DBWEBB_PATH/.."
LOG_PATH="$DBWEBB_PATH/log"



# Copy value-of-time file to .dbwebb for correction
cp "$PROJ_PATH/$COPY_FILE" "$DBWEBB_PATH"



test_status="$(cd "$DBWEBB_PATH" && ${py} -m examiner.run_tests &> "$LOG_PATH")"



# Picks subparts of log file
NOT_FIRSTS="$(cat "$LOG_PATH" | tail -n +2)" # start on line 2
FIRST_LINE="$(cat "$LOG_PATH" | head -1)"



# Resets points
POINTS=0



# Output log file
output_log () {
    echo
    echo "====================================="
    echo "TEST SCRIPT OUTPUT"
    echo "====================================="
    echo "$NOT_FIRSTS"
}



# Clean, removes files
clean_up () {
    rm "$DBWEBB_PATH/$COPY_FILE"
    rm "$LOG_PATH"
    rm "$DBWEBB_PATH/$OUTPUT_FILE"
}



first_assignment="$(echo $FIRST_LINE | cut -c1)"
other_assignments="$(echo $FIRST_LINE | cut -c3-)"

# Outputs whether an assignment is solved or not.
if [[ $first_assignment = "1" ]]; then
    echo "Du har löst uppgift 1."
    POINTS=$((POINTS+20))
else
    echo "Du har inte löst uppgift 1."
fi

ASSIGNMENT=1
for result in $other_assignments; do
    let ASSIGNMENT+=1
    if [[ $result = "1" ]]; then
        echo "Du har löst uppgift $ASSIGNMENT."
        POINTS=$((POINTS+10))
    else
        echo "Du har inte löst uppgift $ASSIGNMENT."
    fi
done



# Sets grade message based on POINTS
if [[ $POINTS -gt 19 ]]; then
    echo "Du har $POINTS poäng och är godkänd på den individuella examinationen."
    EXIT_STATUS=0
else
    echo "Du har $POINTS poäng. Detta är mindre än 20 och du är inte godkänd på den individuella examinationen."
    EXIT_STATUS=1
fi



# Outputs log file from Python test script
output_log



# Clean up
clean_up
exit $EXIT_STATUS
