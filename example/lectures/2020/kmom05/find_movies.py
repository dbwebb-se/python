"""
Tuple assignment
"""
def find(search, movies):
    """
    Search tuple for value
    """
    match = []
    for movie in movies:
        if search in movie:
            match.append(movie)
    return match

def search_movies(movies):
    """
    Search for movies
    """
    search = input("Enter something to search for: ")
    matches = find(search, movies)
    sorted_matches = sorted(matches)
    print(sorted_matches)


if __name__ == "__main__":
    movies_tuple = (
        ("Baby Driver", "2017", "Edgar Wright"),
        ("Scott Pilgrim vs. the world", "2010", "Edgar Wright"),
        ("Thor: Ragnarok", "2017", "Taika Waititi"),
        ("What we do in the shadows", "2014", "Taika Waititi"),
        ("Tucker and Dale vs Evil", "2010", "Eli Craig"),
    )
    search_movies(movies_tuple)
