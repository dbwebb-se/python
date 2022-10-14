"""
shoe assignment. calc average show size
"""

def check_size(shoe_size):
    """
    Return the shoe size as an integer but raises an exception if it is too large or too small.
    Only values 32 <= shoe size <= 48 is allowed
    """
    number = int(shoe_size)
    if (number > 48):
        raise ValueError("The shoe size is too large")
    if (number < 32):
        raise ValueError("The shoe size is too small")
    return number

def get_data():
    """
    Get names and sizes from user
    """
    data = {}
    choice = input("Enter 'name, shoesize':")
    while choice != "done":
        try:
            name, size = choice.split(", ")
            data[name] = check_size(size)
        except ValueError:
            print("You must enter a number for shoe size")
        choice = input("Enter 'name, shoesize':")
    return data

def print_data(data):
    """
    calc average and print data
    """
    tot = 0
    for name, size in data.items():
        print(f"{name}: {size}")
        tot += size
    print(f"average size is {tot/len(data)}")

if __name__ == "__main__":
    name_size = get_data()
    print_data(name_size)

    raise SystemExit("program exited")
