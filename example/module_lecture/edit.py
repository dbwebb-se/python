"""
Edit content in file
"""
def menu():
    """
    Print menu for program
    """
    print("""
a: Lägg till formatrad
s: Radera innehåll
q: quit
    """)

def add():
    """
    Add to file
    """
    line = input("Skriv en formatrad: ")
    with open("data.txt", "a") as fd:
        fd.write(line)

def remove():
    """
    remove from file
    """
    line = input("Vill du verkligen ta bort allt: ")
    if line == "ja":
        with open("data.txt", "w") as fd:
            fd.write("")

def main():
    """
    Starting point of program
    """
    while True:
        menu()
        choice = input("Gör ett val: ")
        if choice == "q":
            break
        elif choice == "a":
            add()
        elif choice == "d":
            remove()
        else:
            print("Not an option!")


if __name__ == "__main__":
    main()
