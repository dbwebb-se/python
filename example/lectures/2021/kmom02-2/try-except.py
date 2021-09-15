"""
try except exempel
"""
number = 10

try:
    number2 = int(input("Skriv in en siffra: "))
except ValueError:
    print("number2 är inte en siffra, fy!")

try:
    x = number / number2
    print(x)
except ZeroDivisionError:
    print("number2 är 0, inte OK!")
print("Hej")
