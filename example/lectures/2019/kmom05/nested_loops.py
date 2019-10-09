"""
Sum nested loops
"""
list1 = [1, 2, 3, 4]
list2 = [1, 2, [6, 7, 8], 5, 7, 9]
list3 = [[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2]

def sum_list(numbers):
    """
    Traverse list and sum values
    """
    total = 0
    print(numbers)
    for value in numbers:
        if isinstance(value, list):
            print(value)
            child_sum = 0
            for child_value in value:
                child_sum += child_value
            print("Child sum", child_sum)
            total += child_sum
        else:
            total += value
    print("Total", total)
# sum_list(list1)
# sum_list(list2)
sum_list(list3)
