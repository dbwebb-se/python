"""
Examples of for-loops
"""

print("\nIterera från och med 0 till 5, skriv ut siffran")
for i in range(5):
    print(i)

print("\nIterera från och med 5 till 16, i steg om 3, skriv ut siffran")
for i in range(5, 16, 3):
    print(i)

print("\nIterera över tecknena i strängen, skriv ut varje tecken")
for character in "python":
    print(character)

# enumerate när du vill ha en räknare med
print("\nIterera över tecknena i strängen, skriv ut varje tecken med dess position")
for i, character in enumerate("python snake"):
    print(character, "has the position ", i)

print("\nIterera över tecknena i strängen och vänd håll på strängen")
string = ""
for character in "python":
    string = str(character) + string
    print("string = ", string, ", la till tecknet ", character, " i början av strängen.")
print(string)

print("\nIterera med en yttre och en inre for-loop, nestlade loopar")
ROWS = 4
COLS = 3
for row_no in range(ROWS):
    for col_no in range(COLS):
        print("*", end="")
    print()
