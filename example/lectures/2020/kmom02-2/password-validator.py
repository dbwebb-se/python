"""
Ett giltig lösenord uppfyller följande krav:
    Innehåller minst en karaktärer.
    Innehåller max 10 karaktärerer.
    Innehåller minst ett heltal. Tips använd funktionen isdigit()
"""
password = input("Skriv in ditt lösenord: ")

is_valid = False
if password and len(password) < 11:
    for char in password:
        if char.isdigit():
            is_valid = True
            break
if is_valid:
    print("Your password is valid!")
else:
    print("Your password is NOT valid!")
