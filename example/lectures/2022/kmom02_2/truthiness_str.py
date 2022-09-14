"""
Examples of truthiness with string
"""

# Empty strings "" are False and all strings with content are True
empty_str = ""
name = "Marie"

# Test with if-statements
if name:
    print(f"{name} is True\n")

if empty_str:
    print(f"The empty string {empty_str} is False and this will not be printed.\n")
else:
    print(f"The empty string {empty_str} is False.\n")

# Test with while-loop:
while name:
    name = name[:-1] # Remove the last character in the string name
    print(f"name is now {name}")
print(f"End of while-loop. This is what is left of name {name}\n")

# Do you see an pattern!? All empty datastructures are False!

# Together with and, or and not. Assign name to Marie again since name was emptied in the while-loop
name = "Marie"
another_name = "Andreas"
if name and another_name:
    print("Both strings are True\n")

if name or empty_str:
    print("One of them is True\n")

if name and empty_str:
    print("This row will not be entered\n")
else:
    print("This is False because empty_str is False\n")

if not empty_str:
    print(f"The empty string {empty_str} is False\n")
    