numbers = ""
def f1():
    # 3
    global numbers
    numbers += "3"

def f2():
    global numbers
    f3()
    numbers += "2"
    f1()

def f3():
    global numbers
    numbers += "1"
    

f2()
print(numbers)

