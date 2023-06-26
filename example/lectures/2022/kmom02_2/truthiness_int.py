"""
Examples of truthiness with integers and floats
"""

# Number 0 is False but all the other numbers are True
number_zero = bool(0)
number_true = bool(10)
print(f"\n0 is {number_zero} and 10 is {number_true}\n")

# Negative numbers are not 0 and are True
number_neg = bool(-10)
print(f"-10 is {number_neg}\n")

# Number 0 is False but all the other numbers are True, work the same with float
number_zero = bool(0.00)
number_true = bool(10.123)
print(f"0.00 is {number_zero} and 10.123 is {number_true}\n")

# Use this with if-statements
value = 3.14
if value:
    print(f"{value} is True\n")

value = 0
if value:
    print(f"{value} is True\n")
else:
    print(f"{value} is False\n")
