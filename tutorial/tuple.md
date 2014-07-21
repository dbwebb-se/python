tuple
==============================
Examples in Python 3


```python
"""
Creating tuples
"""
a = 1, 2
print(a)

b = ("apple", 3)
print(b)

c = 1, 2, 3
print(c)

# Nested
d = ((1,2), (1,0), (2,4))
print(d)


"""
Using tuples to assing multiple values
"""
x, y = 42, 64
print(x)
print(y)

x, y = b
print(x)
print(y)


"""
Accessing tuples
"""
print(a[1])

print(b[0])

print(c[2])

print(d[0])
print(d[0][1])


"""
Comparing tuples
"""
print((0,1) < (0,2))
print((1,0,30) < (1,1,3))


"""
Using dict and tuple
"""
# Counting
my_str = "Hello world!"
counts = dict()
for char in my_str:
    counts[char] = counts.get(char, 0) + 1
print(counts)

# sort the list by value
lst = list()
for key, value in counts.items():
    lst.append((value, key))
print(lst)
lst.sort(reverse=True)
print(lst)


"""
Tuples as keys
"""
my_dict = dict()
my_dict[1,0] = "apple"
my_dict[3,4] = "snake"
print(my_dict)


```


Reference and read more
------------------------------

[Library - Tuples](https://docs.python.org/3/library/stdtypes.html?highlight=dict#tuples)

[Tutorial - Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html?highlight=tuple#tuples-and-sequences)


Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
