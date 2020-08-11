"""
Program calculating energy consumption and cost
by using the module energy_calculation
"""

import sandwich

blt_ingredients = ["ost", "bacon", "sallad", "majonnäs"]
blt_recipe = [
    "stek bacon i en stekpanna", "smöra en sida av brödskivan, börja sätta ihop sandwichen",
    "stek sandwichen med medelvärme i ca 3-5 minuter", "avsluta med att lägga på majonäsen"
]
grilled_cheese_ingredients = ["vitlökssmör", "riven ost"]
unknown_ingredients = ["sallad", "tonfiskröra"]

blt_ingredients_string = sandwich.format_sandwich_string(
    blt_ingredients,
    "En BLT innehåller"
)
blt_recipe_string = sandwich.format_sandwich_string(
    blt_recipe,
    "För den perfekta BLT-mackan skall dessa steg följas:"
)
grilled_cheese_ingredients_string = sandwich.format_sandwich_string(
    grilled_cheese_ingredients,
    "En Grilled Cheese innehåller"
)
unknown_ingredients_string = sandwich.format_sandwich_string(
    unknown_ingredients
)

print(blt_ingredients_string)
print(blt_recipe_string)
print(grilled_cheese_ingredients_string)
print(unknown_ingredients_string)
