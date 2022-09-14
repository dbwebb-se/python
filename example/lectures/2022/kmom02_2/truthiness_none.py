"""
Examples of truthiness with None and is
"""

# In the comparison the boolean value of the variable is tested. Python is casting name like bool(name)

# None equals (==) test, == tests the content, the value of the object in the memory
# value = None
# if value == None:
#     print(f"\nNone is {value} and == is comparing the value IN the memory\n")
#
# This example gives you validation error:
# C0121: Comparison 'value == None' should be 'value is None' (singleton-comparison)

# None 'is' test, 'is' tests whether two variables point to the same object in the memory.
value = None
if value is None:
    print(f"\nNone is {value} and 'is' is comparing places in the memory\n")

# NOTE USE 'is' with None

# More examples with 'is'
# Two variables are created on different places (addresses) in the memory with exactly the same content (values)
value_1 = 0
value_2 = 0
for i in range(100):
    value_1 += i

for i in range(100):
    value_2 += i

print("\nPrint tests with value_1 and value_2")
print("Content of variables")
print(value_1)
print(value_2)
print("Addresses in the memory")
print(id(value_1))
print(id(value_2))
print(value_1, "equals", value_2, "=", value_1==value_2) # compare content
print(value_1, "is", value_2, "is", value_1 is value_2) # compare memory address

value_2 = value_1
print("\nAssign value_1 to value_2. Now they point to the same memory address")
print(value_1, "equals", value_2, "=", value_1==value_2) # compare content
print(value_1, "is", value_2, "is", value_1 is value_2) # compare memory address
