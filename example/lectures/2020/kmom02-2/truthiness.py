"""
What is True and what is False and how do we compare values?
"""

value = 0
value2 = 0
for i in range(1000):
    value += i
for i in range(1000):
    value2 += i
print(id(value))
print(id(value2))
print(value, "equals", value, "==", value==value2)
print(value, "equals", value2, "is", value is value2)

# value = None
# if value is None:
#     print("Value är inte en sträng")
# elif value:
#     print("Icke tom sträng")
# else:
#     value += "Inte längre tom"
#     print("EN tom sträng")
# print(value)
