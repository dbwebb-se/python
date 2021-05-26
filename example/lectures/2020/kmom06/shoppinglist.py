"""
Add items to a shoppinglist
"""
def read_file(filename):
    """
    Read content from file
    """
    try:
        with open(filename, "r") as fd:
            return fd.read()
    except FileNotFoundError:
        print("You are missing the file")
    return



def write_to_file(filename, content, mode):
    """
    write to file, mode should be "a" or "w"
    """
    with open(filename, mode) as fd:
        fd.write(content)



def main():
    """
    Meny for program
    """
    filename = "shopping.txt"
    while True:
        inp = input("Enter things to buy or shop: ")
        if inp == "shop":
            print(read_file(filename))
            write_to_file(filename, "", "w")
        else:
            write_to_file(filename, inp+"\n", "a")



if __name__ == "__main__":
    main()
