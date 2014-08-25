#!/usr/bin/env python3

import random

fhand = open("format.txt")
line = fhand.readline()

moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
mood = random.choice(moods)
smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
smiley = random.choice(smilies)

print(line.format(mood=mood, smiley=smiley))