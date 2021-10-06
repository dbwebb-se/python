"""
Program that allows for searching in movies
"""
def search_movies(query):
    """
    Searches for movies
    """
    all_movies = (
        ("Baby Driver", "2017", "Edgar Wright"),
        ("Scott Pilgrim vs. the world", "2010", "Edgar Wright"),
        ("Thor: Ragnarok", "2017",  "Taika Waititi"),
        ("What we do in the shadows", "2014", "Taika Waititi"),
        ("Tucker and Dale vs Evil", "2010", "Eli Craig"),
    )

    result_movies = []
    for movie in all_movies:
        title, year, director = movie
        if query  in (title, year, director):
            result_movies.append(movie)

    print()
    print("Results: ")
    for title, year, director in sorted(result_movies):
        print(title + " " + year + " " + director)

if __name__ == "__main__":
    query_str = input("What do you want to search for: ")
    search_movies(query_str)
