"""
Disclaimer: Spaghetti code only written
for educational purposes.
Never do this at home.
"""

starting_point = "Karlskrona"
first_destination = "Osby"
second_destination = "Hillerød"

km_to_first_destination = 136
miles_to_first_destination = 136 * 0.621371

print("Going from " +
    starting_point +
    " to " +
    first_destination
)

print(str(miles_to_first_destination) +
    " miles to " +
    first_destination
)

degrees_celsius_at_first_destination = 13
weather_at_first_destination = "Raining"
degrees_fahrenheit_at_first_destination = 13 * (9/5) + 32

print(str(degrees_fahrenheit_at_first_destination) +
    " degrees and " +
    weather_at_first_destination +
    " in " +
    first_destination
)

print()
print("Going from " +
    first_destination +
    " to " +
    second_destination
)

km_to_second_destination = 141
miles_to_second_destination = 141 * 0.621371

print(str(miles_to_second_destination) +
    " miles to " +
    second_destination
)

degrees_celsius_at_second_destination = 16
weather_at_second_destination = "Sunny"
degrees_fahrenheit_at_second_destination = 16 * (9/5) + 32

print(str(degrees_fahrenheit_at_second_destination) +
    " degrees and " +
    weather_at_second_destination +
    " in " +
    second_destination
)
