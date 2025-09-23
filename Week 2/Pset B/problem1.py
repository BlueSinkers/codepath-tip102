"""
Questions I would ask to help understand question:
1. How do I get the population values of a list of dictionaries?
2. How do I sort off of the dictionary values?

Plan in plain English (pseudocode):
I will try to use the Python sorted function. If not, I would iterate through the list and keep trakc of the maximum population element with some variable defined outside.

Begin problem:
"""

def most_endangered(species_list):
    sorted_data = sorted(species_list, key=lambda x: x["population"])
    return sorted_data[0]["name"]

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))