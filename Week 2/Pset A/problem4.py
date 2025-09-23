"""
Questions I would ask to help understand question:
1. How do I find the same key value pairs?
2. How do I return the key value pairs as a dictionary?

Plan in plain English (pseudocode):
Iterate through the schedule finding the values that are very 

Begin problem:
"""

def identify_conflicts(venue1, venue2):
    conflicts = {}
    for key in venue1:
        if key in venue2 and venue1[key] == venue2[key]:
            conflicts[key] = venue1[key]
    return conflicts

#examples
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))