"""
Hur mutable datatyper funkar som argument
"""
import pprint
movies_part1 = [
    "Spider-Man: Far From Home",
    "Dora and the Lost City of Gold",
    "John Wick: Chapter 3 - Parabellum",
    "Zombieland: Double Tap",
    "Captain Marvel",
    "Star Wars: The Rise of Skywalker"
]

def add_part(movies):
    """
    Lägg till "part 2" på varje sträng i listan
    """
    #movies[0] += " part 2"
    #movies_part2 = []
    for index, _ in enumerate(movies):
        # movies_part2.append(movie + " part 2")
        movies[index] += " part2"
    pprint.pprint(movies)
    # return movies

add_part(movies_part1)
# new_list = add_part(movies_part1)
pprint.pprint(movies_part1)
