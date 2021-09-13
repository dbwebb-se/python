"""
Most wanted holder - Variable with a value we are looking for.
"""
smallest = 9999999999# wanted holder

while True:
    content = input("Enter a number: ")
    if content == "q":
        break
    else:
        number = int(content)
        if number < smallest:
            smallest = number
        print(smallest)
