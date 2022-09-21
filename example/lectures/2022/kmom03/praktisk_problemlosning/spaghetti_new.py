"""
Disclaimer: Spaghetti code only written
for educational purposes.
Never do this at home.
"""

import calculations as c
import destination_data as data
from output import print_destination_info

def handle_destination(
    from_destination, to_destination,
    distance_in_km,
    degrees_cel, weather):
    """
    Converts data for the destination and presents the result
    """
    miles_to_first_destination = c.km_to_miles(distance_in_km)
    degrees_fahrenheit_at_first_destination = c.cel_to_fahr(degrees_cel)

    print_destination_info(from_destination, to_destination,
        miles_to_first_destination, degrees_fahrenheit_at_first_destination, data.weather_at_first_destination)

def main():
    """
    Main function for the module spaghetty.py
    """
    # First destination
    handle_destination(
        data.starting_point,
        data.first_destination,
        data.km_to_first_destination,
        data.degrees_celsius_at_first_destination,
        data.weather_at_first_destination
    )

    print()

    # Second destination
    handle_destination(
        data.first_destination,
        data.second_destination,
        data.km_to_second_destination,
        data.degrees_celsius_at_second_destination,
        data.weather_at_second_destination
    )


if __name__ == "__main__":
    main()
