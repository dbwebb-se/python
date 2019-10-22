"""
tuple assignment
"""
def search_movies(movies):
    """
    Search for a movie
    """
    s = input("What to search for: ")
    found_movies = []
    for movie in movies:
        if s in movie:
            found_movies.append(movie)
    found_movies.sort()
    print(found_movies)

if __name__ == "__main__":
    all_movies = [
        ("Baby Driver", "2017", "Edgar Wright"),
        ("Scott Pilgrim vs. the world", "2010", "Edgar Wright"),
        ("Thor: Ragnarok", "2017", "Taika Waititi"),
        ("What we do in the shadows", "2014", "Taika Waititi"),
        ("Tucker and Dale vs Evil", "2010", "Eli Craig"),
    ]
    search_movies(all_movies)
