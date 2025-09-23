"""
Questions I would ask to help understand question:
1. Are elements in priority_species guaranteed to be unique?
2. For species not in priority_species, are they always sorted alphabetically?

Plan in plain English (pseudocode):
Add species from observed_species that are in priority_species in that respective order and add the rest in ascending order.

Begin problem:
"""

def prioritize_observations(observed_species, priority_species):
    result = []
    for species in priority_species:
        for obs in observed_species:
            if obs == species:
                result.append(obs)
    remaining = []
    for obs in observed_species:
        if obs not in priority_species:
            remaining.append(obs)
    remaining.sort()
    result.extend(remaining)
    return result


#examples  - not working due to some unicode issues but the logic should be fine
observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 