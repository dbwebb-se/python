"""
Skriv ett program som beräknar sparande.
Input: startkapital, ränta och slutvärde
Output: antal år
"""

# Step 3 - add calculation for several years. Since we do not know how many years we will iterate,
# we will use a while-loop. The counter no_of_years is set to 0 before the loop and increased at the
# end of the loop. A print is added in the loop for tracking the variables capital and no_of_years

# Input or assign
capital = 1000
interest = 5
goal = 1200

# Calculation, new_value = old_value * (1 + interest / 100)
no_of_years = 0
while capital < goal:
    new_capital = capital *  (1 + interest / 100)
    capital = new_capital
    no_of_years += 1
    print("Efter " + str(no_of_years) + " år har du " + str(round(capital, 2)) + " kr på kontot.")

# Output
print("\nDu behöver spara i " + str(no_of_years) + " år.")
print("Då har du " + str(round(capital, 2)) + " kr på kontot.")
