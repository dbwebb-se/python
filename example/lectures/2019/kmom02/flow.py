"""
Prints factorial for all numbers 2 to the input number
"""

while True:
    choice = input("Skriv en siffra eller 'done' för avslut: ")
    if choice == "done":
        break
    else:
        try:
            chosen_number = int(choice)
        except ValueError:
            print("Skriv en siffra")
            continue

        for number in range(2, chosen_number + 1):
            total = 1
            factorial_string = str(number) + "! = "
            while number > 0:
                total *= number
                if number > 1:
                    factorial_string += str(number) + " * "
                else:
                    factorial_string += str(number)
                number -= 1

            print(factorial_string + " = " + str(total))
