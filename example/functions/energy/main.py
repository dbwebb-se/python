"""
Program calculating energy consumption and cost
by using the module energy_calculation
"""

# pylint: disable=consider-using-f-string

import energy_calculation

emil_time = 2.5 / 60
andreas_time = 3.5 / 60
mikael_time = 0.5 / 60
kenneth_time = 0.5 / 60

emil_energy = energy_calculation.calculate_energy(emil_time)
andreas_energy = energy_calculation.calculate_energy(andreas_time)
mikael_energy = energy_calculation.calculate_energy(mikael_time, 600)
kenneth_energy = energy_calculation.calculate_energy(kenneth_time, 600)

emil_cost = energy_calculation.calculate_cost(emil_energy)
andreas_cost = energy_calculation.calculate_cost(andreas_energy)
mikael_cost = energy_calculation.calculate_cost(mikael_energy)
kenneth_cost = energy_calculation.calculate_cost(kenneth_energy)

emil_string = f"Emil använder {emil_energy:.4f} kWh och detta kostar {emil_cost:.4f} kr"

andreas_string = "Andreas använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=andreas_energy,
    cost=andreas_cost
)

mikael_string = "Mikael använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=mikael_energy,
    cost=mikael_cost
)

kenneth_string = "Kenneth använder {energy:.4f} kWh och detta kostar {cost:.4f} kr".format(
    energy=kenneth_energy,
    cost=kenneth_cost
)

print(emil_string)
print(andreas_string)
print(mikael_string)
print(kenneth_string)
