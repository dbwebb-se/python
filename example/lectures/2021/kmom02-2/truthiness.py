"""
Shuffles word, uses truthiness
"""

import random

word = "elephant"
shuffle_word = ""

while word:
    letter_index = random.randint(0, len(word) - 1)
    
    shuffle_word = shuffle_word + word[letter_index]
    
    word = word[0:letter_index] + word[letter_index + 1:]
    
    print(shuffle_word)
