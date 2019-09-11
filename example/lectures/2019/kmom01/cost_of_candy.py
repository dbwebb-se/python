"""
Calculates the remainder after splurging
on candy
"""

allowance = input("What is your allowance? ")
cost_of_candy = input("How much candy did you buy? ")

remainder = round(float(allowance) - float(cost_of_candy), 2)

print("You have " + str(remainder) + " kr left")
