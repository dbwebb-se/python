'''
Uppgift 1
'''

# Input, get allowance and cost_of_candy
# https://docs.python.org/3.10/library/functions.html?highlight=built%20functions 
allowance = int(input("Vad är din månadspeng? "))
cost_of_candy = int(input("Hur mycket handlar du godis för? "))

# Calculation
left_of_allowance = allowance - cost_of_candy

# Output, print out what is left of allowance
print("Du har " + str(left_of_allowance) + " kr kvar av din månadspeng.")
