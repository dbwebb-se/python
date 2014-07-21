objects
==============================
Examples in Python 3


```python
"""
Object class
"""
class Shape(object):
	x = 0
	y = 0

print(Shape) # class '__main__.Shape'

"""
Object instance
"""
circle = Shape()

print(circle) 					# __main__.Shape object at 0x7f9cdf2f3278

"""
Add attribute to main object
"""
setattr(Shape, "name", "newShape")

print(circle.name) 				# newShape

"""
Add attribute to instance
"""
circle.z = 123

print(circle.z) 				# 123

"""
Method to print an objects own attributes
"""
# inside object class
def print(self):
	print(self.name, self.x, self.y, self.z)

circle.print() 					# newShape 0 0 123

"""
Method to change an objects own attributes
"""
# inside object class
def changeName(self, newName):
	self.name = newName

circle.changeName("anotherName")
print(circle.name) 				# anotherName

"""
Inititalize an object with attributes
"""
class Dog:
	kind = "Poodle" 			# global attribute
	def __init__(self, name):
		self.name = name 		# private for each instance 

dogOne = Dog("Aramis")
dogTwo = Dog("Athos")

print(dogOne.kind)				# Poodle
print(dogOne.name)				# Aramis

print(dogTwo.kind)				# Poodle
print(dogTwo.name)				# Athos

```


Reference and read more
------------------------------

[Not done](https://docs.python.org/3/tutorial/somethingsomethingsomething)



Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.
