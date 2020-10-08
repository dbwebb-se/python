# Correct.bash script used for autocorrecting programming exams.



# Verbose check
VERBOSE=true

# Text file use by students
COPY_FILE="value-of-time.txt"

# If available use python3 else python
python3 --version >/dev/null 2>&1 && py=python3 || py=python



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
exit 0
