
"""
Questions I would ask to help understand question:
1. What happens if list of points is emptyu?
2. Why should we use stack here instead of summing list elements directly?

Plan in plain English (pseudocode):
Initialize stack and go through booth one by one pushing points from booth to stack. After visiting all booths, pop everything from stack and add to total and return total.

Begin problem:
"""

def collect_festival_points(points):
    stack = []
    
    for point in points:
        stack.append(point)
    
    total = 0
    while stack:
        total += stack.pop()
    
    return total

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8]))