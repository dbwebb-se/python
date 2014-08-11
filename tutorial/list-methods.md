list - basics
==============================
Examples in Python 3


```python
"""
Append
"""
x = [1,2,3]
x.append("42")
print(x)


"""
Insert
"""
# Rememer that the index starts at 0
x.insert(0, "first")
print(x)

x.insert(3, "first")
print(x)


"""
Remove and pop
"""
x.remove("first")
print(x)        # Only removes the first found

y = x.pop()
print(x)
print(y)


"""
Find and count
"""
i = x.index("first")
print(i)
print(x[i])

x.append("42")
x.append("42")
print(x)
c = x.count("42")
print("\"42\" found", c, "times")


"""
Sort and reverse
"""
x.reverse()
print(x)

# Can't sort when there are ints and strings in the same list

x = [3,7,2,4,5]
x.sort()
print(x)

x = ["d", "b", "a", "c"]
x.sort()
print(x)



```


Reference and read more
------------------------------

[Tutorial - More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
