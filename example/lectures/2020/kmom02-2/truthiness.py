"""
What is True and what is False and how do we compare values?
"""

value = 0
value1 = 0
for i in range(1000):
    value += i
for i in range(1000):
    value1 += i
print(id(value1))
print(id(value2))
print(value, "equals", value1, "==", value==value1)
print(value, "equals", value1, "is", value is value1)

# value = None
# if value is None:
#     print("Value är inte en sträng")
# elif value:
#     print("Icke tom sträng")
# else:
#     value += "Inte längre tom"
#     print("EN tom sträng")
# print(value)
