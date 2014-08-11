functions
==============================
Examples in Python 3


```python
"""
Define a simple function
"""
def test():
	print("This is a test")

test()


"""
Define a function with a parameter
"""
def test2(someText):
	print("Parameter was: " + someText)

test2("Hello world!")


"""
Define a function with a return
"""
def test3(someText, x):
	return someText * x

test_return = test3("Hello", 3)
print(test_return)


```


Reference and read more
------------------------------

[Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)

[Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)



Revision history
------------------------------

2014-07-17 (sylvanas) PA1 First try.
