"""
One way flag - Variable that change it's value from True/False to False/True once.
"""
loop = True
while loop:
    word = input("A word: ")
    if "e" in word:
        loop = False
print("e was entered")
