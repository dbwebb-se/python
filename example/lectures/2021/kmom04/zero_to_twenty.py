"""
Checks if numbers are in list and swaps
"""
from random import randint

def zero_to_twenty(items, random_one, random_two):
    """
    gets two random numbers
    checks if they are in list
    """
    index_one = -1
    index_two = -1
    
    try:
        index_one = items.index(random_one)
    except ValueError:
        print(str(random_one) + " finns inte i listan")
        
    try:
        index_two = items.index(random_two)
    except ValueError:
        print(str(random_two) + " finns inte i listan")

    if index_one >= 0 and index_two >= 0:
        tmp = items[index_one]
        items[index_one] = items[index_two]
        items[index_two] = tmp
        
        print(items)

if __name__ == "__main__":
    numbers_list = [8, 12, 7, 3, 15, 4, 19]
    
    zero_to_twenty(numbers_list, randint(0, 20), randint(0, 20))
