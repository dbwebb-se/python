"""
The difficult way to calculate 7^2
"""

def calc_square(a, b):
    """
    (a+b)^2
    """
    square = a**2 + b**2 + 2*a*b
    return square

def calc_many_squares():
    """
    Squares it for many numbers
    """
    for i in range(3):
        result = calc_square(i, i+1)
        print(result)
    return result

calc_many_squares()
