"""
Calculate factorial up to an input
"""
try:
    number = int(input("Skriv in en siffra: "))
    
    if number > 0:
        factorial = 1

        while number:
            factorial *= number
            number -= 1
            
        print(factorial)
    else:
        print("Fakultet är bara definierat för n > 0")
except ValueError:
    print("Du skrev inte i en siffra")
