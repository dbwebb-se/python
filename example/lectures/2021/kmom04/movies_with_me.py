"""
Come to the movies with me
"""

def output_movie_goers(goers):
    """
    Prints nice list of people going to the movies
    """
    print()
    for goer in goers:
        print(goer)

def add_movie_goers():
    """
    Add movie goers
    """
    movie_goers = []
    while True:
        name_or_done = input("Write a name you want to bring to the movies (done to exit): ")
        
        if name_or_done == "done":
            break
        else:
            movie_goers.append(name_or_done)
            
    output_movie_goers(movie_goers)
    output_movie_goers(movie_goers[::2])
    output_movie_goers(movie_goers[-3:])
    output_movie_goers(movie_goers[2:4])

if __name__ == "__main__":
    add_movie_goers()
