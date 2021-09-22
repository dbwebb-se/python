"""
conversion functions
"""
def km_to_miles(km):
    """ calc km to miles """
    return km * 0.621371


def c_to_f(celsius):
    """ convert celsius to farenheit"""
    return celsius * (9/5) + 32

if __name__ == "__main__":
    print(km_to_miles(10))
    print(c_to_f(10))
