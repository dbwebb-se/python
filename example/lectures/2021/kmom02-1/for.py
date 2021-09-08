"""
Examples of for-loops
"""
for i, letter in enumerate("python snake"):
    print(letter, "has the position ", i)

string = ""
for number in "python":
    string = str(number) + string
print(string)

ROWS = 4
COLS = 4
for nr in range(ROWS):
    for nr2 in range(COLS):
        print("*", end="")
    print()
