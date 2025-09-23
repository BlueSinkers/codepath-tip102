"""
Questions I would ask to help understand question:
1. What if the list only has 1 element?
2. What if the list is odd?

Plan in plain English (pseudocode):
When the list is not empty, continually remove the smalles and largest iterating through the list. Furthermore, calculate the average and store it in a set and return the size of that set (use sets to avoid duplicate issues).

Begin problem:
"""
def distinct_averages(species_populations):
    averages = set()
    populations = species_populations[:]
    
    while populations:
        min_pop = min(populations)
        max_pop = max(populations)
        avg = (min_pop + max_pop) / 2
        averages.add(avg)
        populations.remove(min_pop)
        populations.remove(max_pop)
        
    return len(averages)

#examples 
species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 