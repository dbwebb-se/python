Built-in functions
==============================
Examples in Python 3


```python
"""
int()
"""
x = "42"
print(x, "is of type", type(x))
x = int(x)
print(x, "is of type", type(x))


"""
str()
"""
x = 42
print(x, "is of type", type(x))
x = str(x)
print(x, "is of type", type(x))


"""
float()
"""
x = 42
print(x, "is of type", type(x))
x = float(x)
print(x, "is of type", type(x))


"""
min()
"""
x = [1,2,3]
print("Min in", x, "is", min(x))


"""
max()
"""
x = [1,2,3]
print("Max in", x, "is", max(x))



"""
len()
"""
x = "Hello world!"
print("Lenght of", x, "is", len(x))


"""
ord()
"""
x = "a"
print(x, "has the unicode value of", ord(x))


"""
round()
"""
x = 1.6
print(x, "rounded is", round(x))


"""
range()
"""
print("This is a range of 10:", range(10))

# Range can be used to loop - more of range in range-tutorial
for x in range(10):
	print(x, end=",")
print("")


"""
type()
"""
x = "42"
print(x, "is of type", type(x))


"""
any()
"""
x = [1,2]
y = [2,3,4]
if any(a in x for a in y):
	print(x, "and", y, "have at least one value in common")



```


Reference and read more
------------------------------

[Built-in Functions](https://docs.python.org/3/library/functions.html)


Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
