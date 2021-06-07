"""
After running this script. Open file and manually name the variables for the dictionaries.
"""

import csv
import pprint

filename = "emm.csv"

emm90 = {}
emm05 = {}
emm17 = {}
di_country = {}

def if_none(value):
    """
    Replace None values with -1
    """
    if value is None:
        return -1
    return value

with open(filename, 'r') as data:
    for idx, line in enumerate(csv.DictReader(data)):
        
        emm90[idx] = float(if_none(line["1990"]))
        emm05[idx] = float(if_none(line["2005"]))
        emm17[idx] = float(if_none(line["2017"]))
        di_country[line["country"]] = {
            "id": idx,
            "population": [],
            "area": 0,
        }
    # print(di_emm)

filename = "1990.csv"
with open(filename, 'r') as data:
    for idx, line in enumerate(csv.DictReader(data)):
        # print(line)
        if line["country"] in di_country:
            di_country[line["country"]]["population"].append(int(line["1990"]))
    # print(di_country)

filename = "2005.csv"
with open(filename, 'r') as data:
    for idx, line in enumerate(csv.DictReader(data)):
        # print(line)
        if line["country"] in di_country:
            di_country[line["country"]]["population"].append(int(line["2005"]))

filename = "2017.csv"
with open(filename, 'r') as data:
    for idx, line in enumerate(csv.DictReader(data)):
        print(line)
        if line["country"] in di_country:
            di_country[line["country"]]["population"].append(int(line["2017"]))
            di_country[line["country"]]["area"] = float(line["area"])
            di_country[line["country"]]["population"] = tuple(di_country[line["country"]]["population"])
                
    print(di_country)

# for x in di_emm.values():
#     del x["country"]

module_docstring = """\"\"\"
Contains data about countries Fossil CO2 emission (in megaton, multiply with 1 000 000),
area (in KM2) and population size.
There is one dictionary for each year of emission data, emission_1990, emission_2005 and emission_2017.
Each dictionary contain a key and value pair.
The key is an integer id that can be connected to a country in the dictionary "country_data".
The value is that countries CO2 emission (in megaton) for that year, 1990, 2005 or 2017 depending on
the variable with corresponding name. 

Example:
emission_1990 = {
    0: 2.546,
    1: 6.583,
}



The variable `country_data` is a nested dictionary, meaning a dictionary inside a dictionary.
Each countries data is a dictionary inside the dictionary. The country name is the key and the value is
a dictionary that has the follwing keys id, area and population. "id" is used to connect the key from 
the emission dictionaries to a country. "area" is the countries area in KM2 and population is a 
tuple with three elements. The first element is the population data for 1990, second is for 2005 and
the last is for 2017.

Example:
country_data = {
    'Afghanistan': 
    {
        'area': 652864.0,
        'id': 0,
        'population': (12412311, 25654274, 36296111)
    },
    'Albania': 
    {
        'area': 28748.0,
        'id': 1,
        'population': (3286070, 3086810, 2884169)
    },
}



Sources:
emission data: 
    https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions#Fossil_CO2_emissions_by_country/region
Country area: https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2015
Population size:
    https://www.populationpyramid.net/population-size-per-country/1990/
    https://www.populationpyramid.net/population-size-per-country/2005/
    https://www.populationpyramid.net/population-size-per-country/2017/
    https://data.worldbank.org/indicator/SP.POP.TOTL?locations=EU
\"\"\"
"""

with open("emission_data.py", "w") as f:
    f.write(module_docstring)
    f.write("# pylint: disable=bad-continuation\n")
    pprint.pprint(emm90, stream=f)
    pprint.pprint(emm05, stream=f)
    pprint.pprint(emm17, stream=f)
    pprint.pprint(di_country, stream=f)

# {
#     0: {
#         "1990": 6.583,
#         "2005": 4.196,
#         "2007": 5.026
#     }
# }
#
# {
#     "Albania": {
#         "id": 0,
#         "population": (3286070, 3086810, 2884169),
#         "areas": 10991
#     }
# }
