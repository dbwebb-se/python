"""
Skriv ett program som beräknar sparande.
Input: startkapital, ränta och slutvärde
Output: antal år
"""

# Step 4 - add input and cast to float

# Input or assign
capital = float(input("Ange ditt startkapital: "))
interest = float(input("Ange din ränta i procent: "))
goal = float(input("Vilket slutvärde önskar du? "))

# Calculation, new_value = old_value * (1 + interest / 100)
no_of_years = 0
while capital < goal:
    new_capital = capital *  (1 + interest / 100)
    capital = new_capital
    no_of_years += 1
    print("Efter " + str(no_of_years) + " har du " + str(round(capital, 2)) + " kr på kontot.")

# Output
print("\nDu behöver spara i " + str(no_of_years) + " år.")
print("Då har du " + str(round(capital, 2)) + " kr på kontot.")
