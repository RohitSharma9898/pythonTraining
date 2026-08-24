"""
DATETIME MODULE

Used to work with dates and times.
"""

from datetime import datetime, date


# Current date and time

now = datetime.now()

print("Current date and time:", now)


# Current date

today = date.today()

print("Today's date:", today)


# Extract information

print("Year:", now.year)

print("Month:", now.month)

print("Day:", now.day)

print("Hour:", now.hour)

print("Minute:", now.minute)