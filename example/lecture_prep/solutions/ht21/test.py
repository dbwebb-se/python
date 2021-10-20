"""
Hur generatorer och yield fungerar
"""
def f():
    """
    En generator
    """
    print("inne i funktion")
    # print("inne 1")
    # yield 1
    # print("inne 2")
    # yield "hej"
    # print("inne 3")
    # yield 3
    # print("inne 4")
    # yield 4
    for v in [1,3,5,6,87,8,8]:
        yield str(v)

generator = f()
for value in generator:
    print("ute" + value)
# print(generator)
# print(
#     next(generator)
# )
# print(
#     next(generator)
# )
# print(
#     next(generator)
# )
# print(
#     next(generator)
# )
