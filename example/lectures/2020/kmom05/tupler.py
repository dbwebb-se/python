"""
Tuple example
"""
from operator import itemgetter

def create_tuple(string):
    """
    Create tuple with word and word len
    """
    return string, len(string)


def sort_by_length(words):
    """
    sort and print words base on length
    """
    tuples = []
    for string in words:
        tuples.append(create_tuple(string))
    print(tuples)
    tuples.sort(key=itemgetter(1))
    print(tuples)



if __name__ == "__main__":
    strings = ["ko", "get", "elefant", "hund", "orm"]
    sort_by_length(strings)
