"""
Calculate factorial for every number between 2 and user input.
"""
while True:
    chosen = input("Enter a number or done to exit: ")

    if chosen != "done":
        try:
            chosen_number = int(chosen)
        except ValueError:
            print("Enter a number!!!!")
            continue

        for number in range(2, chosen_number+1):
            total = 1
            factorial_string = str(number) + "!="
            while number > 0:
                total *= number
                if number > 1:
                    factorial_string += str(number) + " * "
                else:
                    factorial_string += str(number)
                number -= 1
            print(f"{factorial_string} = {total}")
    else:
        exit()
