#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script showing definition and usage of functions in python.
For the article Funktioner, parametrar och returvärden version 2.
"""

blt_ingredients = ["ost", "bacon", "sallad", "majonnäs"]
blt_recipe = [
    "stek bacon i en stekpanna", "smöra en sida av brödskivan, börja sätta ihop sandwichen",
    "stek sandwichen med medelvärme i ca 3-5 minuter", "avsluta med att lägga på majonäsen"
]

blt_ingredients_string = ", ".join(blt_ingredients[:-1]) + " och " + blt_ingredients[-1]
blt_recipe_string = ", ".join(blt_recipe[:-1]) + " och " + blt_recipe[-1]

print("En BLT innehåller " + blt_ingredients_string + ".")
print("För den perfekta BLT-mackan skall dessa steg följas: " + blt_recipe_string + ".")



def print_sandwich_string(ingredients, presentation):
    """
    Formats ingredience and recipe lists in a representable string.
    """
    formated_string = ", ".join(ingredients[:-1]) + " och " + ingredients[-1] + "."
    print(presentation + formated_string)

print_sandwich_string(blt_ingredients, "En BLT innehåller ")
print_sandwich_string(blt_recipe, "För den perfekta BLT-mackan skall dessa steg följas: ")

grilled_cheese_ingredients = ["vitlökssmör", "riven ost"]
print_sandwich_string(grilled_cheese_ingredients, "En Grilled Cheese innehåller ")



def print_sandwich(ingredients, presentation="Prova vår nya sandwich som innehåller "):
    """
    Formats ingredience and recipe lists in a representable string.
    """
    formated_string = ", ".join(ingredients[:-1]) + " och " + ingredients[-1] + "."
    print(presentation + formated_string)

print_sandwich(blt_ingredients, "En BLT innehåller ")

unknown_ingredients = ["sallad", "tonfiskröra"]
print_sandwich(unknown_ingredients)



def create_sandwich_string(ingredients, presentation="Prova vår sandwich som innehåller "):
    """
    Formats ingredience and recipe lists in a representable string.
    """
    number_of_ingredients = len(ingredients)
    if number_of_ingredients == 1:
        result = presentation + ingredients[0] + "."
        return result

    formated_string = ", ".join(ingredients[:-1]) + " och " + ingredients[-1] + "."
    result = presentation + formated_string
    return result

blt_ingredients_string = create_sandwich_string(blt_ingredients, "En BLT innehåller ")
print(blt_ingredients_string)



def formatted_sandwich_string(ingredients, presentation="Prova vår sandwich som innehåller"):
    """
    Formats ingredience and recipe lists in a representable string.
    """
    number_of_ingredients = len(ingredients)
    if number_of_ingredients == 1:
        return f"{presentation} {ingredients[0]}."

    return f"{presentation} {', '.join(ingredients[:-1])} och {ingredients[-1]}."

blt_ingredients_string = formatted_sandwich_string(blt_ingredients, "En BLT innehåller")
print(blt_ingredients_string)
