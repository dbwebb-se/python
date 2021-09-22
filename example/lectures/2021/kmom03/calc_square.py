"""
Calc a weird square
"""
def calc_square(a, b):
    """
    Kvadreringsregeln
    """
    square = a**2 + b**2 + 2*a*b
    return square
# result = calc_square(2, 4)
print(calc_square(2, 4))
