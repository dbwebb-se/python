"""
Disclaimer: Spaghetti code only written
for educational purposes.

Never do this at home.
"""
import output
import conversions

def destination_information(start, destination, km, celsius, weather):
    """
    Print all information about a destination
    """
    miles_to_destination = conversions.km_to_miles(km)
    degrees_fahrenheit_at_destination = conversions.c_to_f(celsius)

    output.print_start_to_destination(start, destination)
    output.print_distance(miles_to_destination, destination)
    output.print_weather(
        degrees_fahrenheit_at_destination,
        weather,
        destination
    )



def main():
    """
    Main part of program
    """
    starting_point = "Karlskrona"

    first_destination = "Osby"
    km_to_first_destination = 136
    degrees_celsius_at_first_destination = 13
    weather_at_first_destination = "Raining"

    destination_information(
        starting_point,
        first_destination,
        km_to_first_destination,
        degrees_celsius_at_first_destination,
        weather_at_first_destination
    )

    print()

    second_destination = "Hillerød"
    km_to_second_destination = 141
    degrees_celsius_at_second_destination = 16
    weather_at_second_destination = "Sunny"
    destination_information(
        starting_point,
        second_destination,
        km_to_second_destination,
        degrees_celsius_at_second_destination,
        weather_at_second_destination
    )

if __name__ == "__main__":
    main()
