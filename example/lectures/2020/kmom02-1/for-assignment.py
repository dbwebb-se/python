"""
Skriv ett program som med hjälp av en for-loop plockar bort
alla mellanslag från strängen "Python är det bästa programmeringsspråket!"

När programmet är klart ska 
strängen bli "Pythonärdetbästaprogrammeringsspråket!"

Tips. mellanslag är en egen karaktär, " ", vi kan jämföra mot.
"""
    
string = "Python är det bästa programmeringsspråket!"
msg = ""
for char in string:
    if char != " ":
        msg += char
print(msg)


# mindre bra lösning
msg = ""
for char in string:
    if char == " ":
        pass
    else:
        msg += char
    print(msg)
