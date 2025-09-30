
"""
Questions I would ask to help understand question:
1. Are empty strings considered symmetric? 
2. How are strings with odd lengths adjudicated?

Plan in plain English (pseudocode):
I will start one pointer on one end and the other on the other. If the pointers are the same as they get to the middle, then the title is symmetrical.

Begin problem:
"""

def is_symmetrical_title(title):
    
    title = title.replace(" ", "")
    left = 0
    right = len(title) -1 
    if right == -1:
        return True 
    
    while left < right:
        if title[left].upper() != title[right].upper():
            return False 
        left += 1
        right -= 1 
    
    return True 

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 