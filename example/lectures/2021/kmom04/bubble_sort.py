"""
Bubble sort implementation
"""

def bubble_sort(items):
    """
    Sorts list
    """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    print(items)
    
if __name__ == "__main__":
    numbers_list = [8, 12, 48, 3, 15, 6463, 19]

    bubble_sort(numbers_list)
