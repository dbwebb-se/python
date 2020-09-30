def f1(numbers):
    numbers.append(4)

def f2(numbers):
    numbers.append(2)
    f4(numbers)

def f3(numbers):
    numbers.append(1)
    f2(numbers)
    f1(numbers)

def f4(numbers):
    numbers.append(3)

if __name__ == "__main__":
    numbers = [] 
    f3(numbers)
    print(numbers)
