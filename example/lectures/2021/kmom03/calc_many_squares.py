"""
Show module, if name main and return
"""
from module import calc_square

def calc_many_square():
    """
    Calc squar for many numbers
    """
    for number in range(4):
        print(calc_square(number, number+1))

if __name__ == "__main__":
    calc_many_square()
