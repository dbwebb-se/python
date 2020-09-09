"""
Example of if-case
"""
nr_of_apples = 15
nr_of_pears = 3

correct = False
if nr_of_apples > 10:
    print("Lots of apples")
    if nr_of_pears > 5:
        correct = True
        print("Lots of apples and pears")
elif nr_of_apples > 5:
    print("lots of apples")
else:
    print("Not many fruits")
    

print(correct)
print("After if")
