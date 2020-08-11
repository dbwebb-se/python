"""
Function used in the example.
"""

def format_sandwich_string(ingredients, presentation="Prova vår sandwich som innehåller"):
    """
    Formats ingredience and recipe lists in a representable string.
    """
    number_of_ingredients = len(ingredients)
    if number_of_ingredients == 1:
        return "{} {}.".format(presentation, ingredients[0])

    return "{presentation} {comma_sepearated_elements} och {last_element}.".format(
        presentation=presentation,
        comma_sepearated_elements=", ".join(ingredients[:-1]),
        last_element=ingredients[-1]
    )
