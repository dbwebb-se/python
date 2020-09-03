"""
Calculates remaining money after buying candy

Skriv ett program där du använder funktionen input() för att ta emot två värden allowance och cost_of_candy. Dra sedan cost_of_candy från allowance. Programmet ska sedan skriva ut hur mycket man har kvar efter att ha handlat godis tillsammans med strängen " kr".
"""



allowance = input("Vad är din månadspeng? ")

cost_of_candy = input("Hur mycket har du handlat godis för? ")

money_left = int(allowance) - int(cost_of_candy)

print("Du har kvar " + str(money_left) + " kr")



# allowance = int(input("Vad är din månadspeng? "))
# 
# cost_of_candy = int(input("Hur mycket har du handlat godis för? "))
# 
# money_left = str(allowance - cost_of_candy)
# 
# print("Du har kvar " + money_left + " kr")
