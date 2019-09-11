"""
Convert seconds to hours and seconds
"""

duration = int(input("Enter a duration in seconds: "))

hours = str(duration // (60*60))
seconds = str(duration % (60*60))

print(str(duration) + " seconds is " + hours + " hours and " + seconds + " seconds")
