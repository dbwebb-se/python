math module
==============================
Examples in Python 3


```python
# Import module
import math

"""
Rounding floats
"""
# Ceiling
x = 4.2
y = math.ceil(x)
print(y)

# Floor
x = 7.8
y = math.floor(x)
print(y)


"""
Powers
"""
# logarithm
x = math.log(10)
print(x)

# Power (same as 2**4)
x = math.pow(2, 4)
print(x)

# Square root
x = math.sqrt(9)
print(x)


"""
Trigonometry
"""
# Euclidean norm - hypotenuse
x = math.hypot(3,4)
print(x)

# Sine of radians
x = math.sin(math.pi/2)
print(x)

# Tangent of radians
x = math.tan(math.pi/4)
print(x)

# Degreese from raidans
x = math.degrees(math.pi)
print(x)

# Radians from degrees
x = math.radians(180)
print(x)


"""
Contants
"""
print(math.pi)

print(math.e)



```


Reference and read more
------------------------------

[math — Mathematical functions](https://docs.python.org/3/library/math.html)


Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
