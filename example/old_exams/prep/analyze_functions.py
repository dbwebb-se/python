"""
Module for analyze functions
"""
def vowels():
    """
    vowels
    """
    vowels_ = "aeiouy"
    text = read_file().lower()
    counter = 0
    for c in text:
        if c in vowels_:
            counter += 1
    return counter

def periods():
    """
    Persiods
    """
    return read_file().count(".")

def uppers():
    """
    Uppers
    """
    text = read_file()
    counter = 0
    for c in text:
        if c.isupper():
            counter += 1
    return counter

def read_file():
    """
    Read file
    """
    with open("manifesto.txt", "r") as fh:
        return fh.read()
