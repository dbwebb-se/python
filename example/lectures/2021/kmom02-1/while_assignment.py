"""
Skriv ett program som med hjälp av en while-loop tar emot
siffror från användaren.
Programmet ska avslutas när något annat än en siffra skrivs in.
 
För varje siffra användaren skriver in,
skriv ut den mängden av stjärnor (*) till skärmen.
"""
# bättre lösning
# not_number = False
# while not not_number:
#     inp = input("Enter int or something: ")
#     if inp.isdigit():
#         number = int(inp)
#         for i in range(number):
#             print("*", end="")
#         print()
#     else:
#         not_number = True
 
# bäst lösning
# not_number = False
# while not not_number:
#    inp = input("Enter int or something: ")
#    if inp.isdigit():
#        number = int(inp)
#        print("*" * number)
#    else:
#        not_number = True
# # 
# # # minst bra
# while True:
#     inp = input("Enter int or something: ")
#     if inp.isdigit():
#         number = int(inp)
#         for i in range(number):
#             print("*", end="")
#         print()
#     else:
#         break

# nya bästa, tack jawnta
stars = input("Enter a number: ")
while stars.isdigit():
    print("*" * int(stars))
    stars = input("Enter a number: ")
