# Correct.bash script used for autocorrecting programming exams.


# Verbose check
VERBOSE=true

# Text file use by students
COPY_FILE="phil.txt"

# If available use python3 else python
python3 --version >/dev/null 2>&1 && py=python3 || py=python



# get path to .dbwebb folder
DBWEBB_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
PROJ_PATH="$DBWEBB_PATH/.."
LOG_PATH="$DBWEBB_PATH/log"



# Copy value-of-time file to .dbwebb for correction
cp "$PROJ_PATH/$COPY_FILE" "$DBWEBB_PATH"



test_status="$(cd "$DBWEBB_PATH" && ${py} test_dbwebb.py &> "$LOG_PATH")"



# Picks subparts of log file
ALL_LINES="$(cat "$LOG_PATH" | head -6)"
FIRST_LINE="$(cat "$LOG_PATH" | head -1)"
SECOND_LINE="$(cat "$LOG_PATH" | head -2 | tail -1)"
REST="$(cat "$LOG_PATH" | head -6 | tail -4)"



# Resets points
POINTS=0



# Output log file
output_log () {
    echo
    echo "====================================="
    echo "TEST SCRIPT OUTPUT"
    echo "====================================="
    cat "$LOG_PATH"
}



# Clean, removes files
clean_up () {
    rm "$DBWEBB_PATH/$COPY_FILE"
    rm "$LOG_PATH"
}



# Checks if all files and modules are there
if [[ $FIRST_LINE = *"... ok"* ]]; then
    echo "Alla moduler och filer finns."
fi



# Checks for completion of first assignment
if [[ $SECOND_LINE = *"... ok"* ]]; then
    echo "Du har löst uppgiften och är godkänd."
else
    echo "Du har inte löst uppgiften och är därför underkänd."
    output_log
    exit 1
fi



# Outputs log file from Python test script
output_log



# Clean up
clean_up
exit 0
