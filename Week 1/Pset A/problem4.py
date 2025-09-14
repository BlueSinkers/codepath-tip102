
"""
Questions I would ask to help understand question:
1. What is in items?
2. What do I return given x?

Plan in plain English (pseudocode):
If statement if x is valid based on length of items and return the value if it's valid and None if it's not.

Begin problem:
"""

def get_item(items, x):
    if x < 0 or x >= len(items):
        print("None")
        return None
    else:   
        print(items[x])
        return items[x]
        

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)