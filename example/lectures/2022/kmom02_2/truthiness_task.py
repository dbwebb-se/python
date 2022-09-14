"""
Check if password validates
"""
# Input
password = input("\nInput a password: ")

# Assign, assume that the password is faulty
result = "The password does not validate!"

# Validate password
if password: # check if the password contains at least one character, that is not empty
    if len(password) <= 10: # check if the length of the password is lesser or equal to 10
        for letter in password: # check if the password contains at least one integer
            if letter.isdigit():
                result = "Yes, the password validates!"
                break # not needed since the result will be the same with or without break

# Output
print(result)

# Another solution with a flag, validated_password and if-statement
# validated_password = False

# if password:
#     if len(password) <= 10:
#         for letter in password:
#             if letter.isdigit():
#                 validated_password = True

# if validated_password:
#     print("Wohooo we have a validated password")
# else:
#     print("Buhuhuu the password did not validate")
