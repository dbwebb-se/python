"""
Main program that calls a lot of functions
"""
import shoes
from clothes import jeans
from clothes import rain_coat
from clothes import suit

def main():
    """
    Starting point of program
    """
    print("I will now print information about shoes and clothes:")
    print()

    jeans()
    shoes.sneakers()
    rain_coat()
    shoes.high_heels()
    shoes.galosh()
    shoes.slippers()
    suit()

print(__name__)

if __name__ == "__main__":
    main()
