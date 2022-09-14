"""
Calculate factorial up to a number from input
"""

# Solution with for-loop, try-except, truthiness and flow
try:
    number = int(input("Beräkna fakulteten för: "))
    
    if number > 0:
        factorial = 1 # start value of factorial

        for i in range(factorial, number + 1):
            factorial = factorial * i
            
        print("Svar: " + str(factorial))
    elif number == 0:
        print("Fakultet är bara definierat för n > 0 men man gör definitionen att 0! = 1")
    else:
        print("Fakultet är bara definierat för n > 0")
except ValueError:
    print("Ange ett positivt heltal")

# Solution with while-loop, try-except, truthiness and flow
# try:
#     number = int(input("Beräkna fakulteten för: "))
#     
#     if number > 0:
#         factorial = 1 # start value of factorial
# 
#         while number:
#             factorial *= number # the same os factorial = factorial * number
#             number -= 1
#             
#         print("Svar: " + str(factorial))
#     else:
#         print("Fakultet är bara definierat för n > 0 men man gör definitionen att 0! = 1")
# except ValueError:
#     print("Ange ett positivt heltal")
