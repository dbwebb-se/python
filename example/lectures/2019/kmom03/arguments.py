"""
Pets module
"""

def pets(species="cat", name="Kim", number_of_legs=4):
    """
    Prints about pets
    """
    output = "My pet is a {species} it's called {name} it has {legs} legs"
    print(output.format(
        species=species,
        name=name,
        legs=number_of_legs
    ))

pets("dog", "Buster", 4)
pets(species="parakit", number_of_legs=2)
pets()
