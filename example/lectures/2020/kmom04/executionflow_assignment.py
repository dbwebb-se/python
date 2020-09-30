"""
Assignment 3
"""
def f1(numbers):
    """append"""
    numbers.append(4)

def f2(numbers):
    """append"""
    numbers.append(2)
    f4(numbers)

def f3(numbers):
    """append"""
    numbers.append(1)
    f2(numbers)
    f1(numbers)

def f4(numbers):
    """append"""
    numbers.append(3)

def main():
    """ star program """
    numbers = [] 
    f3(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
