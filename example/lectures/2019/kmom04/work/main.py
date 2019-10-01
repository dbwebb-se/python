"""
Main program that calls a lot of functions
"""
import shoes
from clothes import jeans, rain_coat as rc, suit
def galosh():
    """
    Function that prints about something in between
    """
    print("Clothes or shoes, thats the question")


def main():
    """
    Starting point of program
    """
    print("I will now print information about shoes and clothes:")
    print()

    jeans()
    shoes.sneakers()
    rc()
    shoes.high_heels()
    galosh()
    shoes.slippers()
    suit()

if __name__ == "__main__":
    main()
