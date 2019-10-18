"""
Tuple example
"""
LENGTH = 0
WORD = 1
def create_tuple(word):
    """
    Make word to tuple with its length
    """
    return (len(word), word)

def sort_print(words):
    """
    sort and print word in len order
    """
    tuples = []
    for word in words:
        tuples.append(create_tuple(word))
    tuples.sort()
    pretty_print(tuples)

def pretty_print(tuples):
    """
    Make a pretty print
    """
    for word in tuples:
        print(word[WORD], "has length", word[LENGTH])
if __name__ == "__main__":
    sort_print(["ko", "gris", "elefant", "lejon", "hund"])
