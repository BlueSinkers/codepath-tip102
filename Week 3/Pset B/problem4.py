
"""
Questions I would ask to help understand question:
1. What happens if back appears when no booth has been visited?
2. How does stack structure naturally handle backtracking?

Plan in plain English (pseudocode):
Initialize stack to keep track of visited booths. Loop through each clue in list, if clue is number push onto stack. If clue is "back" and stack isn't empty, pop from stack. Return the stack.

Begin problem:
"""

def booth_navigation(clues):
    stack = []
    
    for clue in clues:
        if clue == "back":
            if stack:
                stack.pop()
        else:
            stack.append(clue)
    
    return stack

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))