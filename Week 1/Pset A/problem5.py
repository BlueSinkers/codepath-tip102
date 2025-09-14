
"""
Questions I would ask to help understand question:
1. What am I summing up?
2. How do I handle an empty list or complciated lists?

Plan in plain English (pseudocode):
Iterate through the list and sum up all the values. If the list is empty, return 0.

Begin problem:
"""


def sum_honey(hunny_jars):
    total = 0
    for honey in hunny_jars:
        total = sum(hunny_jars)
    print(total)
    return total

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)