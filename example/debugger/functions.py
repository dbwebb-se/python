#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script showing definition and usage of functions in python.
For the article Funktioner, parametrar och returvärden.
"""

def calculate_energy_return(time_in_microwave, effect=800):
    """
    Calculates the energy consumption i kWh
    Returns the consumption
    """
    energy = effect * time_in_microwave / 1000
    return energy

def calculate_cost(energy, price_p_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_p_kwh / 100
    return cost

emil_time = 2.5 / 60
emil_energy = calculate_energy_return(emil_time)
emil_cost = calculate_cost(emil_energy)

print("Emil använder " + str(emil_energy) + " kWh och detta kostar " + str(emil_cost) + " kr")

nice_string = f"Emil använder {emil_energy:.4f} kWh och detta kostar {emil_cost:.4f} kr"
print(nice_string)
