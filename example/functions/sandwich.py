"""
Functions used to format strings from lists.
"""

def create_sandwich_string(ingredients, presentation="Prova vår sandwich som innehåller"):
    """
    Takes a presentation string and concatenates it with a list
    that is comma separated, last element has an "och" before insted of ",".
    """
    number_of_ingredients = len(ingredients)
    if number_of_ingredients == 1:
        return "{} {}.".format(presentation, ingredients[0])

    return "{presentation} {comma_sepearated_elements} och {last_element}.".format(
        presentation=presentation,
        comma_sepearated_elements=", ".join(ingredients[:-1]),
        last_element=ingredients[-1]
    )

if __name__ == "__main__":
    print("Testar vår nya modul:")
    print(create_sandwich_string(["ost"]) == "Prova vår sandwich som innehåller ost.")
    print("name: " + __name__)
