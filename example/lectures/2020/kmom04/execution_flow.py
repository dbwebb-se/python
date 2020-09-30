"""
Example of execution flow and global variables
"""

""" numbers = ""
def f1():
    # 3
    global numbers
    numbers += "3"

def f2():
    global numbers
    f3()
    numbers += "2"
    f1()

def f3():
    global numbers
    numbers += "1"
    

f2() """


def f1(numbers):
    """append"""
    numbers.append("3")

def f2(numbers):
    """append"""
    f3(numbers)
    numbers.append("2")
    f1(numbers)

def f3(numbers):
    """append"""
    numbers.append("1")


def main():
    """
    Start everyting, needed to not get validation errors.
    """
    numbers = []
    f2(numbers)
    print(numbers)

if __name__ == "__main__":
    main()
