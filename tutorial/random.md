random module
==============================
Examples in Python 3


```python
# Need to import module to get access to string
import random
"""
Random float between 0 och 1
"""
x = random.random()
print(x)


"""
Random integer between n1 and n2, including n1 and n2
"""
x = random.randint(1, 10)
print(x)


"""
Random integer from 0 to n-1 (not including n)
"""
x = random.randrange(10)
print(x)


"""
Random even int between 10 and 20
"""
x = random.randrange(10, 21, 2)
print(x)


"""
Random element from iterable range
"""
a = "Hello world"
x = random.choice(a)
print(x)


"""
Shuffle
"""
x = [1,2,3,4,5,6]
random.shuffle(x)
print(x)


```


Reference and read more
------------------------------

[random - Examples and Recipes](https://docs.python.org/3/library/random.html#examples-and-recipes)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
