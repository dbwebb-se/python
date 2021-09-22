"""
Funktions for printing data
"""

def print_start_to_destination(start, destination):
    """
    Print start and destination
    """
    print("Going from " +
        start +
        " to " +
        destination
    )


def print_distance(distance, destination):
    """
    print distance to destination
    """
    print(str(distance) +
        " miles to " +
        destination
    )

def print_weather(degrees, weather, destination):
    """
    print weather and temp at destination
    """
    print(str(degrees) +
        " degrees and " +
        weather +
        " in " +
        destination
    )

if __name__ == "__main__":
    print_start_to_destination("karlskrona", "osby")
