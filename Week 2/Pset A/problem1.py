"""
Questions I would ask to help understand question:
1. What if lists and dictionaries don't match in size?
2. What if list and dictionary are empty should I return an empty dict?

Plan in plain English (pseudocode):
Iterate through both lists at the same time and create the dictionary to match each together.

Begin problem:
"""

def lineup(artists, set_times):
    
    lineup_dict = {}
    
    for artist, time in zip(artists, set_times):
        lineup_dict[artist] = time  
    return lineup_dict

#test
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))