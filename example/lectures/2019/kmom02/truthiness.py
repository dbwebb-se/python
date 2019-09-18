"""
What is True and what is False and how do we compare values?
"""

value1 = 0
value2 = 0
for i in range(1000):
    value1 += i
for i in range(1000):
    value2 += i
print(id(value1))
print(id(value2))
print(value1, "är lika med", value2, value1 == value2)
print(value1, "is", value2, value1 is value2)

# value = None
# if value is None:
#     print("Value är inte en sträng")
# elif value:
#     print("Icke tom sträng")
# else:
#     value += "Inte längre tom"
#     print("EN tom sträng")
# print(value)
