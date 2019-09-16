smallest = 99999

while True:
    content = input("A number: ")
    if content == "q":
        break
    else:
        number = int(content)
        if number < smallest:
            smallest = number

        print(smallest)
