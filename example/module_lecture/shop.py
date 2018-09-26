def add(choice):
    with open("shopping_list.txt", "a") as fd:
        fd.write(choice + "\n")

def remove():
    with open("shopping_list.txt", "w") as fd:
        fd.write("")

def print_shopping_list():
    with open("shopping_list.txt", "r") as fd:
        print(fd.read())

    remove()

def main():
    while True:
        choice = input("Skriv en vara, avsluta med shop: ")
        if choice == "shop":
            print_shopping_list()
            break
        else:
            add(choice)

if __name__ == "__main__":
    main()
