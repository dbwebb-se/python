#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script showing definition and usage of functions in python.
For the article Funktioner, parametrar och returvärden.
"""

emil_time = 2.5 / 60
andreas_time = 3.5 / 60

emil_energy = 800 * emil_time / 1000
andreas_energy = 800 * andreas_time / 1000

print("Emil använder " + str(emil_energy) + " kWh")
print("Andreas använder " + str(andreas_energy) + " kWh")

price_per_kwh = 78.04

emil_cost = emil_energy * price_per_kwh / 100
andreas_cost = andreas_energy * price_per_kwh / 100

print("Emils lunch kostar " + str(emil_cost) + " kr")
print("Andreas lunch kostar " + str(andreas_cost) + " kr")



def calculate_energy(time_in_microwave, name):
    """
    Calculates the energy consumption i kWh
    And prints the consumption together with the name
    """
    energy = 800 * time_in_microwave / 1000
    print(name + " använder " + str(energy) + " kWh")

emil_time = 2.5 / 60
calculate_energy(emil_time, "Emil")

andreas_time = 3.5 / 60
calculate_energy(andreas_time, "Andreas")



def calculate_energy_effect(time_in_microwave, name, effect=800):
    """
    Calculates the energy consumption i kWh
    And prints the consumption together with the name
    """
    energy = effect * time_in_microwave / 1000
    print(name + " använder " + str(energy) + " kWh")

emil_time = 2.5 / 60
calculate_energy_effect(emil_time, "Emil")

andreas_time = 3.5 / 60
calculate_energy_effect(andreas_time, "Andreas")

kenneth_and_mikael_time = 0.5 / 60
calculate_energy_effect(kenneth_and_mikael_time, "Mikael", 600)
calculate_energy_effect(kenneth_and_mikael_time, "Kenneth", 600)



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
