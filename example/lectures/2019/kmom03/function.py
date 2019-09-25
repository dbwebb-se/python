"""
Introduction to functions and execution flow
"""
def f1():
    """
    print "hej"
    """
    print("hej")

def f2():
    """
    print "på"
    """
    f1()
    print("på")
    f3()

def f3():
    """
    print "dig"
    """
    print("dig")
f2()



def countdown():
    """
    countdown from 3 to 1
    """
    print(3)
    print(2)
    print(1)

print("countdown from 3 to 1")
countdown()
print("Again!!!")
countdown()
