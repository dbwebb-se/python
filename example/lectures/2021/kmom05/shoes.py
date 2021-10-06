"""
shoe assignment. calc average show size
"""
def get_data():
    """
    Get names and sizes from user
    """
    data = {}
    inp = input("Enter 'name, shoesize':")
    while inp != "done":
        name, size = inp.split(", ")
        data[name] = int(size)
        inp = input("Enter 'name, shoesize':")
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
