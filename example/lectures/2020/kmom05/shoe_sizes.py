"""
Dictionary assignment
"""
from operator import itemgetter

def gather_data():
    """
    Gather names and show sizes in dictionary
    """
    done = False
    data = {}
    while not done:
        try:
            name, shoesize = tuple(input("Enter name and shoesize, sperated by space: ").split(" "))
            data[name] = shoesize
        except ValueError:
            done = True

    return data

def sort_data(data):
    """
    Sort and print dictionary on shoesize
    """
    avg = 0
    for name, shoesize in sorted(data.items(), key=itemgetter(1)):
        print(f"{name}:{shoesize}")
        avg += int(shoesize)
    print(avg/len(data))


def main():
    """
    Start of program
    """
    name_size = gather_data()
    sort_data(name_size)

if __name__ == "__main__":
    main()
