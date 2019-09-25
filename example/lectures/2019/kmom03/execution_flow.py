"""
Le executioner
"""

def f1():
    """
    f1
    """
    print(3)

def f2():
    """
    f2
    """
    print(1)
    f4()

def f3():
    """
    f3
    """
    f2()
    f1()
    print(4)

def f4():
    """
    f4
    """
    print(2)


f3()
