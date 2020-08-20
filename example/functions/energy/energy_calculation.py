"""
Functions used to calculate energy consumption and cost
"""

def calculate_energy(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    Returns the consumption
    """
    energy = effect * time_in_microwave / 1000
    return energy

def calculate_cost(energy, price_per_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_per_kwh / 100
    return cost
    
if __name__ == "__main__":
    print("Test av calculate energy:")
    print(calculate_energy(800))
    print("name: " + __name__)
