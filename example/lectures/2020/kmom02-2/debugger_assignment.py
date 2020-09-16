"""
Find out what this program does.
Start debugger with "python3 -m pdb debugger_assignment.py"
or "import pdb" and "pdb.set_trace()" in the code and start program as usuall.

Try running the program with both numbers
"""
number = "072-354 02 11"
# number = "073-456 12 9a"
correct = False
if len(number) == 13 and number[3] == "-" and number[7] == " " and number[10] == " ":
    if number[0:3] in "070 072 073 076 079":
        n = number[4:].replace(" ", "")
        for c in n:
            if not c.isdigit():
                print("Your number isnt valid")
                exit()
        print("It is a valid phone number")
        exit()
print("Your number isn't valid")
