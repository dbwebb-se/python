"""
Follower - Variable with a previous value. Can be used to compare old and new values
"""
previous = input("Enter a word: ") # follwer
current = input("Enter a word: ") # most recent holder

while True:
    if len(current) > len(previous):
        print("Current word is longer")
    else:
        print("Previous word is longer")
    
    previous = current
    current = input("Enter a word: ")
