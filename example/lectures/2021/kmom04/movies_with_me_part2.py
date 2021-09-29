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

def add_many(goers, people):
    """
    Extend list with many goers at same time
    """
    people = people.replace("extend:", "")
    people_list = people.split(",")
    goers.extend(people_list)

def find_index(goers, name):
    """
    Print index for user in list
    """
    name = name.replace("index ", "")
    try:
        print(f"{name} har index {goers.index(name)}")
    except ValueError:
        print(f"{name} finns inte i listan {goers}")


def add_movie_goers():
    """
    Add movie goers to list
    """
    movie_goers = []
    while True:
        name_or_done = input("Write a name you want to bring to the movies (done to exit): ")
        
        if name_or_done == "done":
            break
        elif name_or_done.startswith("extend:"):
            add_many(movie_goers, name_or_done)
        elif name_or_done.startswith("index "):
            find_index(movie_goers, name_or_done)
        else:
            movie_goers.append(name_or_done)
        print(movie_goers)
    output_movie_goers(movie_goers)
    output_movie_goers(movie_goers[::2])
    output_movie_goers(movie_goers[-3:])
    output_movie_goers(movie_goers[2:4])

if __name__ == "__main__":
    add_movie_goers()
