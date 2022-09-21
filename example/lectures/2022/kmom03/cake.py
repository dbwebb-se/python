"""
Skapa en fil med namnet cake.py. 
I filen skapa en funktion layer_cake() som skriver ut en formaterat 
strang.
Funktionen ska ta emot 4 argument: 
farg, 2 sorters fyllning och antal lager.
 Alla argument ska ha ett förifylld värde.
Anropa sedan funktionen med 0, 1, 2, 3 och 4 argument samt med
 bara sista argumentet (antal lager) med hjalp av argument=varde
"""

def layer_cake(
    color="Petrol Blue",
    filling1="Passion fruit",
    filling2="Sugar",
    layers=4):
    """
    Print info about cake
    """
    print(f"My cake has the color {color} with the fillings {filling1} and {filling2}. It also has {layers} layers!")

if __name__ == "__main__":
    layer_cake()
    layer_cake("yellow")
    layer_cake("orange", "strawberry")
    layer_cake("orange", "pear", "apple")
    layer_cake("green", "pear", "grape", 10)
    layer_cake(layers=100)
