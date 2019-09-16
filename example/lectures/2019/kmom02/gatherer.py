count = 0
total = 0
number = 0

while number != -999:
    number = int(input("Enter a number, -999 to quit: "))
    if number != -999:
        total += number
        count += 1

if count:
    print("Average", total / count)
