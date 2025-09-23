"""
Questions I would ask to help understand question:
1. Does the journey always start at the first observation?
2. Are station_layout and observations guaranteed to have no duplicates?

Plan in plain English (pseudocode):
For each observation, find its index in station_layout, calc distance from current position, add to total, and update the current position.

Begin problem:
"""

def navigate_research_station(station_layout, observations):
    total_time = 0
    current_index = 0
    for obs in observations:
        next_index = station_layout.index(obs)
        total_time += abs(next_index - current_index)
        current_index = next_index
    return total_time

# Example usage:
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))