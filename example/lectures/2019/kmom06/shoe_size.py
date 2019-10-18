"""
Dictionary assignment
"""
def calculate_average_shoe_size():
    """
    Calculate the average shoe size of input
    """
    info = {}
    while True:
        data = input("Enter name and shoe size: ").split(" ")
        if data[0] == "done":
            break
        info[data[0]] = int(data[1])
    total_shoe_size = 0
    for person in sorted(info, key=info.get, reverse=True):
        total_shoe_size += info[person]
        print(person + ": " + str(info[person]))
    print(total_shoe_size / len(info))

if __name__ == "__main__":
    calculate_average_shoe_size()
