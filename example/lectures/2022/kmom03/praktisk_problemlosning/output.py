"""
Module for printing out information from spaghetty.py
"""

def print_route(from_dest, to_dest):
    """
    Prints out information from one destination to another
    """
    print("Going from " +
        from_dest +
        " to " +
        to_dest
    )

def print_distance(miles_to_first_destination, to_dest):
    """
    Prints distance in miles to destination
    """
    print(str(miles_to_first_destination) +
        " miles to " +
        to_dest
    )

def print_weather(degrees, weather, destination):
    """
    Prints weather information at destination
    """
    print(str(degrees) +
        " degrees and " +
        weather +
        " in " +
        destination
    )

def print_destination_info(
    from_destination, to_destination,
    miles_to_destination,
    degrees, weather):
    """
    Prints destination information
    """
    print_route(from_destination, to_destination)
    print_distance(miles_to_destination, to_destination)
    print_weather(degrees, weather, to_destination)

if __name__ == "__main__":
    print_route("Karlskrona", "Osby")
    print_distance(84.5, "Osby")
    print_weather(60.8, "Sunny", "Hillerød")
    
    print_destination_info("Karlskrona", "Osby", 84.5, 55.4, "Raining")
