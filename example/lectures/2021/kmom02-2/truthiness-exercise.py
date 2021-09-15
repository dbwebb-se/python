"""
Check if password validates
"""

password = input("Input a password: ")

validated_password = False

if password:
    if len(password) <= 10:
        for letter in password:
            if letter.isdigit():
                validated_password = True

if validated_password:
    print("Wohooo we have a validated password")
else:
    print("Buhuhuu the password did not validate")
