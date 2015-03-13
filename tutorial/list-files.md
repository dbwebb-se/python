files
==============================
Examples in Python 3


```python
"""
Open file
"""
fhand = open("test.txt")
print(fhand)


"""
Read whole file
"""
print(fhand.read())


"""
Return to start of file
"""
fhand.seek(0)

"""
Read lines
"""
print(fhand.readline())
print(fhand.readline())


"""
Read all lines
"""
fhand.seek(0)
for line in fhand:
    print(line, end="")
print()

"""
Close file
"""
fhand.close()


"""
Write file
"""
# Open the file with appending mode
fhand = open("test.txt", "a")
inp = input("Enter what you want to add to the file: ")
fhand.write("\n" + inp)
fhand.close()

# Open the file for reading
fhand = open("test.txt")
print(fhand.read())
fhand.close()

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

[Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

[The with statement](https://docs.python.org/3/reference/compound_stmts.html#with)

