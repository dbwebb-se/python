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
