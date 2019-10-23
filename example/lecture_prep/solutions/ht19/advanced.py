"""
Advanced python constructions
"""
# List comprehension
ll = []
for i in range(0, 10):
    ll.append(i)
print(ll)
ll = [i for i in range(0, 10)]
print(ll)
# Dict comrehension with and if-case
ll = {i:i*2 for i in range(0, 10) if i % 2}
print(ll)

# Generator with yield
def f():
    """
    Yield example
    """
    print("start")
    yield 1
    print("middle")
    yield 2
    print("middle 2")
    yield 3
    print("end")

# Loop over generator
for value in f():
    print(value)
# generator = f()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
