"""
Skriv ett program som beräknar sparande.
Input: startkapital, ränta och slutvärde
Output: antal år
"""

# Step last - the whole solution

# Input or assign
capital = float(input("Ange ditt startkapital: "))
interest = float(input("Ange din ränta i procent: "))
goal = float(input("Vilket slutvärde önskar du? "))

# Calculation, new_value = old_value * (1 + interest / 100)1000
no_of_years = 0
while capital < goal:
    capital = capital *  (1 + interest / 100)
    no_of_years += 1

# Output
print("\nDu behöver spara i " + str(no_of_years) + " år.")
print("Då har du " + str(round(capital, 2)) + " kr på kontot.")
