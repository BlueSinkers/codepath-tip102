
"""
Questions I would ask to help understand question:
1. What happens when one string is totally empty?
2. Does alphabetic order matter at all or is this just assorting the two characters together?

Plan in plain English (pseudocode):
Use two pointer with two pointers starting at the start of each words respectively. Continue the iterator through the words until we reach the end of the words. If characters are left over, add them to the combined word, and once done if had to, then return the final answer.

Begin problem:
""" 

def merge_schedules(schedule1, schedule2):
    merged = []
    i, j = 0, 0
    while i < len(schedule1) and j < len(schedule2):
        merged.append(schedule1[i])
        merged.append(schedule2[j])
        i += 1
        j += 1
    merged.extend(schedule1[i:])
    merged.extend(schedule2[j:])
    return "".join(merged)

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 