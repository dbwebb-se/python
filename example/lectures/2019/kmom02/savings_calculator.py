"""
Calculate interset on savings
"""
# Skriv ett program som räknar på sparande.
# ta emot tre värden: start kapital, ränta och slutvärde.
start = float(input("Enter starting capital: "))
rate = float(input("Enter interest rate: "))
end_value = float(input("Enter end value: "))
# räkna ut hur många år pengarna ska stå på kontot innan vi har kommit upp i minst slutvärdet.
new_value = start
year = 0
while new_value < end_value:
    new_value = new_value * (1 + rate / 100)
    print(new_value)
    year += 1
print("It takes", year, "years to go from", start, "to", round(new_value, 2))
# Värdet efter 1 år med ränta kan räknas ut som:
#     new_value = old_value * (1 + interest / 100)
