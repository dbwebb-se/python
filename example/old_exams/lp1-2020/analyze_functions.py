"""
Module
"""

def title(data):
    """
    find non-matching titles
    """
    for row in data:
        cells = row.split(",")

        if cells[1] != cells[2]:
            print(cells[1], end=":")
            get_with_key(cells[0], 1)

def year(data):
    """
    year input
    """
    i_year = input("What i_year? ")
    for row in data:
        cells = row.split(",")

        if cells[3] == i_year:
            print(cells[2], end=":")
            get_with_key(cells[0], -1)

def get_with_key(key, column):
    """
    get column value with key
    """
    with open("title.ratings.csv") as fd:
        rows = fd.read().split("\n")
        for row in rows:
            cells = row.split(",")
            if cells[0] == key:
                print(cells[column])
