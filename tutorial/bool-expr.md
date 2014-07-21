Boolean expression
==============================
Examples in Python 3


```python
"""
Basic comparisons
"""
# Equals
x, y = 4, 4
print(x, "equals", y, "=", x == y)

x, y = "five", "five"
print(x, "equals", y, "=", x == y)


# Not equal
x, y = 4, 5
print(x, "does not equal", y, "=", x != y)

# Larger than
x, y = 10, 2
print(x, "is larger than", y, "=", x > y)

# Smaller than
x, y = 10, 2
print(x, "is smaller than", y, "=", x < y)

# Larger than or equal to
x, y = 10, 10
print(x, "is larger or equal to", y, "=", x >= y)

# Smaller than or equal to
x, y = 2, 10
print(x, "is smaller or equal to", y, "=", x <= y)


"""
Is and is not
"""
# Is - compares identity, not value
x = y = 4
print(x, "is", y, "=", x is y)

x = 4, 2
y = 4, 2
print(x, "is", y, "=", x is y)

print(x, "is not", y, "=", x is not y)


"""
In
"""
x = [1,2,3]
y = 2
print(y, "is in", x, "=", y in x)

print(y, "is not in", x, "=", y not in x)


```


Reference and read more
------------------------------

[Comparisons - reference](https://docs.python.org/3/reference/expressions.html#not-in)

[Comparisons - library](https://docs.python.org/3/library/stdtypes.html#comparisons)


Revision history
------------------------------

2014-07-16 (sylvanas) PA1 First try.
