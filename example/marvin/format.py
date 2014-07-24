#!/usr/bin/env python3

import random
from datetime import date
from datetime import datetime

fhand = open("format.txt")
line = fhand.readline()

today = date.today()
now = datetime.now().strftime("%H:%M:%S")
moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
mood = random.choice(moods)
smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
smiley = random.choice(smilies)

print(line.format(date=today, time=now, mood=mood, smiley=smiley))