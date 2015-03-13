Read files using with
==============================


```python
"""
Use with - as for reading and writing
With closes file automatically after the code in the statement has finished
"""

# read all lines into list
with open("test.txt") as fhand:
    all_lines = fhand.readlines()

# write line into file
with open("test.txt", "w") as fhand:
    fhand.write("This is a test.")

```



Reference and read more
------------------------------

[The with statement](https://docs.python.org/3/reference/compound_stmts.html#with)

[Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
