"""
Gatherer - Variable that gathers data or values from inputs.
"""
number = 0 # most recent holder
total = 0 # gatherer
counter = 0 # stepper/counter
while number != -999:
    try:
        number1 = int(input("Enter a number, -999 to quit: "))
    except ValueError:
        print("Inte ett heltal")
        continue

    if number != -999:
        counter += 1
        total += number

print("Average: ", total/counter)
