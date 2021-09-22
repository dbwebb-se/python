"""
argument, parameters and default values
"""
def pets(species, name="Kim", number_of_legs=4):
    """
    Print pet information
    """
    print(f"My pet is a {species}, it is called {name} and has {number_of_legs} legs.")

pets("dog", "buster",  2)
pets("dog", "buster")
pets("cat")
pets("cat", "Emil")
pets("snake", number_of_legs=0)
