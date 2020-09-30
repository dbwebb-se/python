"""
Example of arguments, default arguments and named arguments
"""
def pets(species, name="Kim", number_of_legs=4):
    """
    Prints about pets
    """
    print(
        "My pet is a {species} and it is called {name} it has {number_of_legs} legs".format(
            species=species,
            name=name,
            number_of_legs=number_of_legs
        )
    )

pets("dog", "Buster", 4)
pets("dog")
pets(species="cat", name="Martin", number_of_legs=5)
