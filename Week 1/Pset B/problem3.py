
"""
Questions I would ask to help understand question:
1. How is this different from sorting a list?
2. Do I do anything with the deleted minimum?

Plan in plain English (pseudocode):
I will just sort the list using Python's inbuilt functions.

Begin problem:
"""

def delete_minimum_elements(numbers):
    return sorted(numbers)  

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
