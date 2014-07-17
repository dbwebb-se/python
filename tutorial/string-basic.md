Strings - basics
==============================
Examples in Python 3


```python
"""
Concatenate
"""
x = "Hello" "World"
print(x)

x = "Hello" + "World"
print(x)

x = "Hello"
x += "World"
print(x)

x = "Hello"
y = "World"
print(x + y)


"""
Repeat
"""
x = "Hello" * 3
print(x)


"""
Access string characters
Remember that index start at 0 and end at lenght-1
"""
x = "Hello"

print(x[0])
print(x[1])

print(x[-1])

for c in x:
	print(c)


"""
String slicing
"""
x = "Hello"

# From start until n
print(x[:3])

# From n until end
print(x[2:])

# From n1 to n2
print(x[2:4])


"""
Use slice to replace part of string
"""
x = "World"
y = x[:3] + "d"
print(y)


"""
Use slice to switch string order
"""
x = "World Hello"
y = x[6:] + x[:6]
print(y)


```


Reference and read more
------------------------------

[Strings - tutorial](https://docs.python.org/3/tutorial/introduction.html#strings)



Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
