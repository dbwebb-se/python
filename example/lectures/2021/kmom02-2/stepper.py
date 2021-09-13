"""
Stepper/Counter - Stepps or counts through a sequence of values.
Often heads to wards a certain value 
"""
counter = 0
result = 26
ADD = 7
MAX = 33
while counter < MAX:
    result += ADD
    counter += 1
print(result)
