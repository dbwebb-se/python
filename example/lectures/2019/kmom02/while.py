while True:
    nr_of_stars = input("Enter number of stars: ")
    if nr_of_stars.isdigit():
        # for number in range(int(nr_of_stars)):
        print("*" * int(nr_of_stars))
    else:
        break
    print()
