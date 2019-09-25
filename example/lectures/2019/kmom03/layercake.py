"""
Tårta module
"""
def layer_cake(
        color="green",
        filling1="raspberry jam",
        filling2="custard",
        number_of_layers=3):
    """
    Prints about our favorite layer cake
    """
    output = "My cake is a {color} {layers} layer cake filled with {filling1} and {filling2}"
    print(output.format(
        color=color,
        layers=number_of_layers,
        filling1=filling1,
        filling2=filling2,
    ))

layer_cake()
layer_cake("blue")
layer_cake("yellow", "blueberry jam")
layer_cake("purple", "banana", "strawberries")
layer_cake("purple", "banana", "strawberries", 42)
layer_cake(number_of_layers=16)
