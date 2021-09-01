"""
Allowance uppgift
"""
allowance = int(input("Vad är din månadspeng? "))
cost_of_candy = int(input("Hur mycket handlar du godis för? "))

left_of_allowance = allowance - cost_of_candy

print(str(left_of_allowance) + " kr")
