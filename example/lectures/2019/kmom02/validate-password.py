"""
Validate a password
"""
passwd = input("Enter a password: ")
size = True

if not passwd:
    size = False
if len(passwd) > 10:
    size = False
if size:
    found_digit = False
    for char in passwd:
        if char.isdigit():
            found_digit = True
            break
    found_lower = False
    for char in passwd:
        if char.islower():
            found_lower = True
            break

    found_upper = False
    for char in passwd:
        if char.isupper():
            found_upper = True
            break
    if not found_digit or not found_lower or not found_upper:
        print("Your password need a digit, upper and lower")
        exit()
else:
    print("Your password has incorrect size")
    exit()
print("You have a valid password")
