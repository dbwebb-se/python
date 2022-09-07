"""
Example with for-statement
"""

# Input or assign
message = "Python är det bästa programmeringsspråket!"

# Task
new_message = ""

# Sämre lösning
# for character in message:
#     if character == ' ':
#         pass
#     else:
#         new_message += character

for character in message:
    if character != ' ':
        new_message += character



# Output
print(new_message)
