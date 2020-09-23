"""
Skapa en lista och fyll den men valfria siffror mellan 0 och 20.
Använd sen random modulen för att slumpa fram två tal mellan 0 och 20.

Använd .index() funktionen på din lista för att kolla om talen finns som värden i listan.
Om de gör det byt plats på dem, annars skriv ut vilket/vilka av talen som inte finns i listan.
"""
import random
l = [0,15,1,6,8,2,4,7]

number = random.randint(0,10)
number2 = random.randint(0,10)
print(l)
found = False
try:
    i1 = l.index(number)
except ValueError:
    print(number, "finns inte i listan")
    found = True
try:
    i2 = l.index(number2)
except ValueError:
    print(number2, "finns inte i listan")
    found = True

if not found:
    tmp = l[i1]
    l[i1] = l[i2]
    l[i2] = tmp
