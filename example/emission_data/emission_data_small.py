"""
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
"""
# pylint: disable=bad-continuation
emission_1990 = {
 11: 58.077,
 30: 0.21,
 49: 162.835,
 54: 8.024,
 64: 4409.339,
 71: 0.839,
 88: 71.929,
 97: 3.02,
 100: 10.208,
 129: 4.401,
 140: 51.454,
 182: 33.876,
 194: 0.007,
 201: 123.106,
 205: 0.144,
 206: 6.887,
 208: 17.178}
emission_2005 = {
 11: 30.485,
 30: 0.307,
 49: 127.157,
 54: 19.409,
 64: 4249.995,
 71: 0.785,
 88: 59.758,
 97: 6.392,
 100: 19.755,
 129: 11.146,
 140: 55.403,
 182: 25.582,
 194: 0.005,
 201: 116.386,
 205: 0.227,
 206: 21.768,
 208: 11.388}
emission_2017 = {
 11: 32.544,
 30: 0.289,
 49: 109.756,
 54: 23.111,
 64: 3548.345,
 71: 0.636,
 88: 50.856,
 97: 12.505,
 100: 24.565,
 129: 28.462,
 140: 52.492,
 182: 28.377,
 194: 0.165,
 201: 95.35,
 205: 0.276,
 206: 12.503,
 208: 12.087}
country_data = {

 'Azerbaijan': {'area': 86600.0,
                'id': 11,
                'population': (7242758, 8538610, 9845316)},

 'Burundi': {'area': 27834.0,
             'id': 30,
             'population': (5438959, 7364857, 10827010)},
 'Czech Republic': {'area': 78866.0,
                    'id': 49,
                    'population': (10340877, 10258165, 10641032)},
 'Dominican Republic': {'area': 48315.0,
                        'id': 54,
                        'population': (7133491, 9097262, 10513111)},
 'European Union': {'area': 4233262.0,
                    'id': 64,
                    'population': (420477979, 435581949, 446131273)},
 'French Polynesia': {'area': 4167.0,
                      'id': 71,
                      'population': (199906, 258780, 276108)},
 'Hungary': {'area': 93030.0,
             'id': 88,
             'population': (10377135, 10085942, 9729822)},
 'Ivory Coast': {'area': 322463.0,
                 'id': 97,
                 'population': (11924873, 18354513, 24437475)},
 'Jordan': {'area': 89341.0,
            'id': 100,
            'population': (3565888, 5765639, 9785840)},
 'Myanmar': {'area': 676578.0,
             'id': 129,
             'population': (41335188, 48949931, 53382521)},
 'Norway': {'area': 385203.0,
            'id': 140,
            'population': (4247286, 4632359, 5296324)},
 'Syria': {'area': 185180.0,
           'id': 182,
           'population': (12446168, 18361178, 17095669)},
 'Turks and Caicos Islands': {'area': 0, 'id': 194, 'population': []},
 'Uzbekistan': {'area': 448978.0,
                'id': 201,
                'population': (20398347, 26427785, 31959774)},
 'Western Sahara': {'area': 266000.0,
                    'id': 205,
                    'population': (217258, 437516, 552617)},
 'Yemen': {'area': 527968.0,
           'id': 206,
           'population': (11709987, 20107416, 27834811)},
 'Zimbabwe': {'area': 390757.0,
              'id': 208,
              'population': (10432409, 12076697, 14236599)}}
