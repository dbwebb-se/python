previous = input("Write another word: ")
current = input("Write a word: ")

while True:
    if len(current) > len(previous):
        print("Current word is longer")
    else:
        print("Previous word is longer")

    previous = current
    current = input("Write a word: ")
