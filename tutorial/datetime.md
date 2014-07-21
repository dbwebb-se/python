datetime
==============================
Examples in Python 3


```python
from datetime import date
from datetime import datetime
"""
Create todays date
"""
now = date.today()
print(now)


"""
Get year, month and day respectively
"""
print(now.year)
print(now.month)
print(now.day)


"""
Get day of the week
"""
print(now.weekday())


"""
Create a formatted string from date
"""
print(now.strftime("%A, %d %B %Y"))


"""
Create a date from year, month and day
"""
birthday = date(1952, 3, 11)
print(birthday)


"""
Get the timedifference between two dates
"""
age = now - birthday
print(age.days)


"""
Get datetime
"""
now = datetime.now()
print(now)


"""
Get current time using datetime
"""
time = datetime.now().time()
print(time)



```


Reference and read more
------------------------------

[datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

[date Objects](https://docs.python.org/3/library/datetime.html#date-objects)

[https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

[Dates and Times](https://docs.python.org/3/tutorial/stdlib.html#dates-and-times)

[timedelta Objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)


Revision history
------------------------------

2014-07-21 (sylvanas) PA1 First try.