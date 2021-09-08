"""
Skriv ett program som räknar på sparande. Programmet ska ta emot tre värden: 
start kapital, ränta och slutvärde.
Programmet ska sedan räkna ut hur många år pengarna ska 
stå på kontot innan vi har kommit upp i minst slutvärdet.

Värdet efter 1 år med ränta kan räknas ut som: 
new_value = old_value * (1 + interest / 100)

Exempel: värdena 1000 i startkapital, 1200 i slutvärde och 5% ränta anges.
Efter 1 år: 1000 * (1 + 5 / 100) = 1050
Efter 2 år: 1050 * (1 + 5 / 100) = 1102.5
Efter 3 år: 1102.5 * (1 + 5 / 100) = 1157.625
Efter 4 år: 1157.625 * (1 + 5 / 100) = 1215.50625 - Dvs 4 år på kontot.
"""

amount_of_mouney = int(input("How much money do you have? "))
interest = int(input("What is your expected interest? "))
goal = int(input("What is your goal value? "))

years = 0
while amount_of_mouney < goal:
    amount_of_mouney = amount_of_mouney * (1 + interest / 100)
    years += 1
    print("After", years, "years you have", round(amount_of_mouney, 5), "money")
