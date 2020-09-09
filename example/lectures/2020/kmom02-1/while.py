"""
Example of while-loop
"""
total_sum = 0
while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        continue

    total_sum += number
    print("new sum is", total_sum)
    if total_sum > 21:
        break

print(total_sum)
