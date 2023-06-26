"""
Module for calculations
"""

def cel_to_fahr(degrees):
    """
    Converts from Celsius to Fahrenheit and returns degrees in Fahrenheit
    """
    return degrees * (9/5) + 32

def km_to_miles(distance):
    """
    Converts from km to miles and returns the distance in miles
    """
    d = distance * 0.621371
    return d

if __name__ == "__main__":
    print(cel_to_fahr(13))
    print(km_to_miles(141))
