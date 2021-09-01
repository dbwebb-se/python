"""
Omvandla sek to timmar och sek
"""
secs = int(input("Enter seconds: "))
hours = secs // (60*60)
secs_left = secs % (60*60)

print(str(secs) + " seconds is " + str(hours) + " hours and " + str(secs_left) + " seconds!")
