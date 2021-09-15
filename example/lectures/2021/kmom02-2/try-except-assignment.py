"""
Skriv ett program som tar emot input från användaren. Beroende på inputens data typ gör en av två saker:

En sträng: Konkatenera ihop med tidigare stränger.
En siffra: Skriv ut den konkatenerade strängen det antal gånger, som siffran är.
"""

inp = ""
string = ""
while inp != "done":
    inp = input("Enter string or number: ")
    try:
        print(string * int(inp))
    except ValueError:
        string += inp
print(string)
